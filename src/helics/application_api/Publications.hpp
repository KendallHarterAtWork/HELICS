/*

Copyright (C) 2017, Battelle Memorial Institute
All rights reserved.

This software was co-developed by Pacific Northwest National Laboratory, operated by the Battelle Memorial
Institute; the National Renewable Energy Laboratory, operated by the Alliance for Sustainable Energy, LLC; and the
Lawrence Livermore National Laboratory, operated by Lawrence Livermore National Security, LLC.

*/
#ifndef _HELICS_PUBLICATION_H_
#define _HELICS_PUBLICATION_H_
#pragma once

#include "HelicsPrimaryTypes.h"
#include "ValueFederate.h"
#include "helicsTypes.hpp"
#include "boost/lexical_cast.hpp"

namespace helics
{

	class PublicationBase
	{
	protected:
		ValueFederate *fed = nullptr;  //!< the federate construct to interact with
		publication_id_t id;  //!< the internal id of the publication
	private:
		std::string key_;  //!< the name of the publication
		std::string units_;  //!< the defined units of the publication
		std::string type_;  //!< the type of the publication
	public:
		PublicationBase() = default;
		PublicationBase(ValueFederate *valueFed,
			const std::string &key,
			const std::string &type,
			const std::string &units = "")
			: fed(valueFed), key_(key), type_(type), units_(units)
		{
			id = fed->registerPublication(key_, type_, units_);
		}

		PublicationBase(interface_visibility locality,
			ValueFederate *valueFed,
			const std::string &key,
			const std::string &type,
			const std::string &units = "")
			: fed(valueFed), key_(key), type_(type), units_(units)
		{
			if (locality == GLOBAL)
			{
				id = fed->registerGlobalPublication(key, type, units);
			}
			else
			{
				id = fed->registerPublication(key, type, units);
			}
		}
		virtual ~PublicationBase() = default;
	
		publication_id_t getID() const { return id; }

		/** get the key for the subscription*/
		const std::string getKey() const { return fed->getPublicationName(id); }
		/** get the key for the subscription*/
		const std::string &getName() const { return key_; }
		/** get the key for the subscription*/
		const std::string &getType() const { return type_; }
		const std::string &getUnits() const { return units_; }
	};

class Publication:public PublicationBase
{
  private:
  
    double delta = -1.0;  //!< the minimum change to publish
    helicsType_t type;  //!< the type of publication
    bool changeDetectionEnabled = false;  //!< the change detection is enabled
    
    mutable defV prevValue;  //!< the previous value of the publication
  public:
    Publication () noexcept {};
    /**constructor to build a publication object
    @param[in] valueFed  the ValueFederate to use
    @param type_ the defined type of the publication
    @param[in] name the name of the subscription
    @param[in] units the units associated with a Federate
    */
    Publication (ValueFederate *valueFed, const std::string &key, helicsType_t type_, std::string units = ""):PublicationBase(valueFed, key, typeNameStringRef(type_),units), type(type_)
    {
        
    }
    /**constructor to build a publication object
    @param locality  set to global for a global publication or local for a local one
    @param[in] valueFed  the ValueFederate to use
    @param type_ the defined type of the publication
    @param[in] name the name of the subscription
    @param[in] units the units associated with a Federate
    */
	Publication(interface_visibility locality,
		ValueFederate *valueFed,
		std::string key,
		helicsType_t type_,
		std::string units = "")
		:PublicationBase(locality, valueFed, key, typeNameStringRef(type_), units),type(type_)
    {
       
    }

    /** send a value for publication
    @param[in] val the value to publish*/
    void publish (double val) const;
    void publish (int64_t val) const;
    void publish (const char *val) const;
    void publish (const std::string &val) const;
    void publish (const std::vector<double> &val) const;
    void publish (std::complex<double> val) const;
    /** secondary publish function to allow unit conversion before publication
    @param[in] val the value to publish
    @param[in] units  the units association with the publication
    */
    template <class X>
    void publish (const X &val, const std::string & /*units*/) const
    {
        // TODO:: figure out units
        publish (val);
    }
	
  private:
    bool changeDetected (const std::string &val) const;
    bool changeDetected (const std::vector<double> &val) const;
    bool changeDetected (const std::complex<double> &val) const;
    bool changeDetected (double val) const;
    bool changeDetected (int64_t val) const;
};

template <class X>
typename std::enable_if<helicsType<X> () != helicsType_t::helicsInvalid, std::unique_ptr<Publication>>::type
make_publication (ValueFederate *valueFed, const std::string &name, const std::string &units = "")
{
    return std::make_unique<Publication> (valueFed, helicsType<X> (), name, units);
}

template <class X>
typename std::enable_if<helicsType<X> () != helicsType_t::helicsInvalid, std::unique_ptr<Publication>>::type
make_publication (interface_visibility locality,
                  ValueFederate *valueFed,
                  const std::string &name,
                  const std::string &units = "")
{
    return std::make_unique<Publication> (locality, valueFed, name, helicsType<X> (),  units);
}

/** class to handle a publication */
template <class X>
class PublicationT:public PublicationBase
{
  public:
    PublicationT () = default;
    /**constructor to build a publication object
    @param[in] valueFed  the ValueFederate to use
    @param[in] name the name of the subscription
    @param[in] units the units associated with a Federate
    */
    PublicationT (ValueFederate *valueFed, const std::string &name, const std::string &units = "")
        : PublicationBase(valueFed,name,typeNameString<X>(),units)
    {
       
    }
    /**constructor to build a publication object
    @param[in] valueFed  the ValueFederate to use
    @param[in] name the name of the subscription
    @param[in] units the units associated with a Federate
    */
    PublicationT (interface_visibility locality, ValueFederate *valueFed, const std::string &name, const std::string &units = "")
        :PublicationBase(locality,valueFed,name,typeNameString<X>(),units)
    {
       
    }
    /** send a value for publication
    @param[in] val the value to publish*/
    virtual void publish (const X &val) const { fed->publish (id, val); }
    /** secondary publish function to allow unit conversion before publication
    @param[in] val the value to publish
    @param[in] units  the units association with the publication
    */
    virtual void publish (const X &val, const std::string & /*units*/) const
    {
        // TODO:: figure out units
        publish (val);
    }
};

/** class to handle a publication
but the value is only published in the change is greater than a certain level*/
template <class X>
class PublicationOnChange : public PublicationT<X>
{
  private:
    X publishDelta;  //!< the delta on which to publish a value
    mutable X prev;  //!< the previous value
  public:
    PublicationOnChange () = default;
    /**constructor to build a publishOnChange object
    @param[in] valueFed  the ValueFederate to use
    @param[in] name the name of the subscription
    @param[in] minChange  the minimum change required to actually publish the value
    @param[in] units the units associated with a Federate
    */
    PublicationOnChange (ValueFederate *valueFed,
                         const std::string &name,
                         const X &minChange,
                         const std::string &units = "")
        : PublicationT<X> (valueFed, name, units), publishDelta (minChange)
    {
        prev = X ();
    }
    /** send a value for publication
    @details the value is only published if it exceeds the specified level
    @param[in] val the value to publish*/
    virtual void publish (const X &val) const override
    {
        if (std::abs (val - prev) >= publishDelta)
        {
            prev = val;
            PublicationT<X>::publish (val);
        }
    }
};
} //namespace helics
#endif
