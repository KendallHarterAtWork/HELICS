/*
Copyright © 2017-2018,
Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Sustainable Energy, LLC
All rights reserved. See LICENSE file and DISCLAIMER for more details.
*/

#include <boost/test/unit_test.hpp>
#include <boost/test/data/test_case.hpp>
#include <boost/test/floating_point_comparison.hpp>
#include <vector>

#include "helics/chelics.h"
#include "helics/helics-config.h"

#define CE(command)                                                                                               \
    helicsErrorClear (&err);                                                                                      \
    command;                                                                                                      \
	BOOST_CHECK_MESSAGE (err.error_code == helics_ok, err.message)

#define HELICS_SIZE_MAX 512

extern const std::vector<std::string> core_types;
extern const std::vector<std::string> core_types_single;

typedef helics_federate (*FedCreator) (char const *, helics_federate_info_t, helics_error *err);

struct FederateTestFixture
{
    FederateTestFixture ();
    ~FederateTestFixture ();

    helics_broker AddBroker (const std::string &core_type_name, int count);
    helics_broker AddBroker (const std::string &core_type_name, const std::string &initialization_string);

    void SetupTest (FedCreator ctor,
                    const std::string &core_type_name,
                    int count,
                    helics_time_t time_delta = helics_time_zero,
                    const std::string &name_prefix = "fed")
    {
        ctype = core_type_name;
        helics_broker broker = AddBroker (core_type_name, count);
        BOOST_CHECK (nullptr != broker);
        AddFederates (ctor, core_type_name, count, broker, time_delta, name_prefix);
    }

    std::vector<helics_federate> AddFederates (FedCreator ctor,
                                               std::string core_type_name,
                                               int count,
                                               helics_broker broker,
                                               helics_time_t time_delta = helics_time_zero,
                                               const std::string &name_prefix = "fed")
    {
        bool hasIndex = hasIndexCode (core_type_name);
        int setup = (hasIndex) ? getIndexCode (core_type_name) : 1;
        if (hasIndex)
        {
            core_type_name.pop_back ();
            core_type_name.pop_back ();
        }

        std::string initString = std::string ("--broker=");
        initString += helicsBrokerGetIdentifier (broker);
        initString += " --broker_address=";
        initString += helicsBrokerGetAddress (broker);

        if (!extraCoreArgs.empty ())
        {
            initString.push_back (' ');
            initString.append (extraCoreArgs);
        }

        helics_federate_info_t fi = helicsCreateFederateInfo ();
        CE (helicsFederateInfoSetCoreTypeFromString (fi, core_type_name.c_str (), &err));
        CE (helicsFederateInfoSetTimeProperty (fi, TIME_DELTA_PROPERTY, time_delta, &err));

        std::vector<helics_federate> federates_added;

        switch (setup)
        {
        case 1:
        default:
        {
            auto init = initString + " --federates " + std::to_string (count);
            auto core = helicsCreateCore (core_type_name.c_str (), NULL, init.c_str (), &err);
            BOOST_REQUIRE_EQUAL (err.error_code, 0);
            CE (helicsFederateInfoSetCoreName (fi, helicsCoreGetIdentifier (core), &err));
            size_t offset = federates.size ();
            federates.resize (count + offset);
            for (int ii = 0; ii < count; ++ii)
            {
                auto name = name_prefix + std::to_string (ii + offset);
                auto fed = ctor (name.c_str (), fi, &err);
                BOOST_CHECK_EQUAL (err.error_code, 0);
                federates[ii + offset] = fed;
                federates_added.push_back (fed);
            }
            helicsCoreFree (core);
        }
        break;
        case 2:
        {  // each federate has its own core
            size_t offset = federates.size ();
            federates.resize (count + offset);
            for (int ii = 0; ii < count; ++ii)
            {
                auto init = initString + " --federates 1";
                auto core = helicsCreateCore (core_type_name.c_str (), NULL, init.c_str (), &err);
                BOOST_REQUIRE_EQUAL (err.error_code, 0);
                CE (helicsFederateInfoSetCoreName (fi, helicsCoreGetIdentifier (core), &err));

                auto name = name_prefix + std::to_string (ii + offset);
                auto fed = ctor (name.c_str (), fi, &err);
                BOOST_CHECK_EQUAL (err.error_code, 0);
                federates[ii + offset] = fed;
                federates_added.push_back (fed);
                helicsCoreFree (core);
            }
        }
        break;
        case 3:
        {
            auto subbroker = AddBroker (core_type_name, initString + " --federates " + std::to_string (count));
            auto newTypeString = core_type_name;
            newTypeString.push_back ('_');
            newTypeString.push_back ('2');
            for (int ii = 0; ii < count; ++ii)
            {
                AddFederates (ctor, newTypeString, 1, subbroker, time_delta, name_prefix);
            }
        }
        break;
        case 4:
        {
            auto newTypeString = core_type_name;
            newTypeString.push_back ('_');
            newTypeString.push_back ('2');
            for (int ii = 0; ii < count; ++ii)
            {
                auto subbroker = AddBroker (core_type_name, initString + " --federates 1");
                AddFederates (ctor, newTypeString, 1, subbroker, time_delta, name_prefix);
            }
        }
        break;
        }
        helicsFederateInfoFree (fi);
        return federates_added;
    }

    helics_federate GetFederateAt (int index)
    {
        if (index < static_cast<int> (federates.size ()))
        {
            return federates.at (index);
        }
        return nullptr;
    }

    std::vector<helics_broker> brokers;
    std::vector<helics_federate> federates;
    std::string extraCoreArgs;
    std::string extraBrokerArgs;
    helics_error err;

    std::string ctype;

  private:
    bool hasIndexCode (const std::string &type_name);
    int getIndexCode (const std::string &type_name);
};
