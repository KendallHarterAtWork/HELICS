# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_helics')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_helics')
    _helics = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_helics', [dirname(__file__)])
        except ImportError:
            import _helics
            return _helics
        try:
            _mod = imp.load_module('_helics', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _helics = swig_import_helper()
    del swig_import_helper
else:
    import _helics
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

helics_ok = _helics.helics_ok
helics_invalid_object = _helics.helics_invalid_object
helics_invalid_argument = _helics.helics_invalid_argument
helics_discard = _helics.helics_discard
helics_terminated = _helics.helics_terminated
helics_warning = _helics.helics_warning
helics_invalid_state_transition = _helics.helics_invalid_state_transition
helics_invalid_function_call = _helics.helics_invalid_function_call
helics_error = _helics.helics_error
helics_true = _helics.helics_true
helics_false = _helics.helics_false
no_iteration = _helics.no_iteration
force_iteration = _helics.force_iteration
iterate_if_needed = _helics.iterate_if_needed
next_step = _helics.next_step
iteration_error = _helics.iteration_error
iteration_halted = _helics.iteration_halted
iterating = _helics.iterating
helics_startup_state = _helics.helics_startup_state
helics_initialization_state = _helics.helics_initialization_state
helics_execution_state = _helics.helics_execution_state
helics_finalize_state = _helics.helics_finalize_state
helics_error_state = _helics.helics_error_state
helics_pending_init_state = _helics.helics_pending_init_state
helics_pending_exec_state = _helics.helics_pending_exec_state
helics_pending_time_state = _helics.helics_pending_time_state
helics_pending_iterative_time_state = _helics.helics_pending_iterative_time_state
helics_custom_filter = _helics.helics_custom_filter
helics_delay_filter = _helics.helics_delay_filter
helics_randomDelay_filter = _helics.helics_randomDelay_filter
helics_randomDrop_filter = _helics.helics_randomDrop_filter
helics_reroute_filter = _helics.helics_reroute_filter
helics_clone_filter = _helics.helics_clone_filter
class data_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, data_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, data_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["data"] = _helics.data_t_data_set
    __swig_getmethods__["data"] = _helics.data_t_data_get
    if _newclass:
        data = _swig_property(_helics.data_t_data_get, _helics.data_t_data_set)
    __swig_setmethods__["length"] = _helics.data_t_length_set
    __swig_getmethods__["length"] = _helics.data_t_length_get
    if _newclass:
        length = _swig_property(_helics.data_t_length_get, _helics.data_t_length_set)

    def __init__(self):
        this = _helics.new_data_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _helics.delete_data_t
    __del__ = lambda self: None
data_t_swigregister = _helics.data_t_swigregister
data_t_swigregister(data_t)

class message_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, message_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, message_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["time"] = _helics.message_t_time_set
    __swig_getmethods__["time"] = _helics.message_t_time_get
    if _newclass:
        time = _swig_property(_helics.message_t_time_get, _helics.message_t_time_set)
    __swig_setmethods__["data"] = _helics.message_t_data_set
    __swig_getmethods__["data"] = _helics.message_t_data_get
    if _newclass:
        data = _swig_property(_helics.message_t_data_get, _helics.message_t_data_set)
    __swig_setmethods__["length"] = _helics.message_t_length_set
    __swig_getmethods__["length"] = _helics.message_t_length_get
    if _newclass:
        length = _swig_property(_helics.message_t_length_get, _helics.message_t_length_set)
    __swig_setmethods__["original_source"] = _helics.message_t_original_source_set
    __swig_getmethods__["original_source"] = _helics.message_t_original_source_get
    if _newclass:
        original_source = _swig_property(_helics.message_t_original_source_get, _helics.message_t_original_source_set)
    __swig_setmethods__["source"] = _helics.message_t_source_set
    __swig_getmethods__["source"] = _helics.message_t_source_get
    if _newclass:
        source = _swig_property(_helics.message_t_source_get, _helics.message_t_source_set)
    __swig_setmethods__["dest"] = _helics.message_t_dest_set
    __swig_getmethods__["dest"] = _helics.message_t_dest_get
    if _newclass:
        dest = _swig_property(_helics.message_t_dest_get, _helics.message_t_dest_set)
    __swig_setmethods__["original_dest"] = _helics.message_t_original_dest_set
    __swig_getmethods__["original_dest"] = _helics.message_t_original_dest_get
    if _newclass:
        original_dest = _swig_property(_helics.message_t_original_dest_get, _helics.message_t_original_dest_set)

    def __init__(self):
        this = _helics.new_message_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _helics.delete_message_t
    __del__ = lambda self: None
message_t_swigregister = _helics.message_t_swigregister
message_t_swigregister(message_t)


def helicsGetVersion():
    return _helics.helicsGetVersion()
helicsGetVersion = _helics.helicsGetVersion

def helicsIsCoreTypeAvailable(type):
    return _helics.helicsIsCoreTypeAvailable(type)
helicsIsCoreTypeAvailable = _helics.helicsIsCoreTypeAvailable

def helicsCreateCore(type, name, initString):
    return _helics.helicsCreateCore(type, name, initString)
helicsCreateCore = _helics.helicsCreateCore

def helicsCreateCoreFromArgs(type, name, argc, argv):
    return _helics.helicsCreateCoreFromArgs(type, name, argc, argv)
helicsCreateCoreFromArgs = _helics.helicsCreateCoreFromArgs

def helicsCreateBroker(type, name, initString):
    return _helics.helicsCreateBroker(type, name, initString)
helicsCreateBroker = _helics.helicsCreateBroker

def helicsCreateBrokerFromArgs(type, name, argc, argv):
    return _helics.helicsCreateBrokerFromArgs(type, name, argc, argv)
helicsCreateBrokerFromArgs = _helics.helicsCreateBrokerFromArgs

def helicsBrokerIsConnected(broker):
    return _helics.helicsBrokerIsConnected(broker)
helicsBrokerIsConnected = _helics.helicsBrokerIsConnected

def helicsCoreIsConnected(core):
    return _helics.helicsCoreIsConnected(core)
helicsCoreIsConnected = _helics.helicsCoreIsConnected

def helicsBrokerGetIdentifier(broker, identifier, maxlen):
    return _helics.helicsBrokerGetIdentifier(broker, identifier, maxlen)
helicsBrokerGetIdentifier = _helics.helicsBrokerGetIdentifier

def helicsCoreGetIdentifier(core, identifier, maxlen):
    return _helics.helicsCoreGetIdentifier(core, identifier, maxlen)
helicsCoreGetIdentifier = _helics.helicsCoreGetIdentifier

def helicsBrokerGetAddress(broker, address, maxlen):
    return _helics.helicsBrokerGetAddress(broker, address, maxlen)
helicsBrokerGetAddress = _helics.helicsBrokerGetAddress

def helicsCoreDisconnect(core):
    return _helics.helicsCoreDisconnect(core)
helicsCoreDisconnect = _helics.helicsCoreDisconnect

def helicsBrokerDisconnect(broker):
    return _helics.helicsBrokerDisconnect(broker)
helicsBrokerDisconnect = _helics.helicsBrokerDisconnect

def helicsCoreFree(core):
    return _helics.helicsCoreFree(core)
helicsCoreFree = _helics.helicsCoreFree

def helicsBrokerFree(broker):
    return _helics.helicsBrokerFree(broker)
helicsBrokerFree = _helics.helicsBrokerFree

def helicsCreateValueFederate(fi):
    return _helics.helicsCreateValueFederate(fi)
helicsCreateValueFederate = _helics.helicsCreateValueFederate

def helicsCreateValueFederateFromJson(json):
    return _helics.helicsCreateValueFederateFromJson(json)
helicsCreateValueFederateFromJson = _helics.helicsCreateValueFederateFromJson

def helicsCreateMessageFederate(fi):
    return _helics.helicsCreateMessageFederate(fi)
helicsCreateMessageFederate = _helics.helicsCreateMessageFederate

def helicsCreateMessageFederateFromJson(json):
    return _helics.helicsCreateMessageFederateFromJson(json)
helicsCreateMessageFederateFromJson = _helics.helicsCreateMessageFederateFromJson

def helicsCreateCombinationFederate(fi):
    return _helics.helicsCreateCombinationFederate(fi)
helicsCreateCombinationFederate = _helics.helicsCreateCombinationFederate

def helicsCreateCombinationFederateFromJson(json):
    return _helics.helicsCreateCombinationFederateFromJson(json)
helicsCreateCombinationFederateFromJson = _helics.helicsCreateCombinationFederateFromJson

def helicsFederateInfoCreate():
    return _helics.helicsFederateInfoCreate()
helicsFederateInfoCreate = _helics.helicsFederateInfoCreate

def helicsFederateInfoLoadFromArgs(fi, argc, argv):
    return _helics.helicsFederateInfoLoadFromArgs(fi, argc, argv)
helicsFederateInfoLoadFromArgs = _helics.helicsFederateInfoLoadFromArgs

def helicsFederateInfoFree(fi):
    return _helics.helicsFederateInfoFree(fi)
helicsFederateInfoFree = _helics.helicsFederateInfoFree

def helicsFederateInfoSetFederateName(fi, name):
    return _helics.helicsFederateInfoSetFederateName(fi, name)
helicsFederateInfoSetFederateName = _helics.helicsFederateInfoSetFederateName

def helicsFederateInfoSetCoreName(fi, corename):
    return _helics.helicsFederateInfoSetCoreName(fi, corename)
helicsFederateInfoSetCoreName = _helics.helicsFederateInfoSetCoreName

def helicsFederateInfoSetCoreInitString(fi, coreInit):
    return _helics.helicsFederateInfoSetCoreInitString(fi, coreInit)
helicsFederateInfoSetCoreInitString = _helics.helicsFederateInfoSetCoreInitString

def helicsFederateInfoSetCoreTypeFromString(fi, coretype):
    return _helics.helicsFederateInfoSetCoreTypeFromString(fi, coretype)
helicsFederateInfoSetCoreTypeFromString = _helics.helicsFederateInfoSetCoreTypeFromString

def helicsFederateInfoSetCoreType(fi, coretype):
    return _helics.helicsFederateInfoSetCoreType(fi, coretype)
helicsFederateInfoSetCoreType = _helics.helicsFederateInfoSetCoreType

def helicsFederateInfoSetFlag(fi, flag, value):
    return _helics.helicsFederateInfoSetFlag(fi, flag, value)
helicsFederateInfoSetFlag = _helics.helicsFederateInfoSetFlag

def helicsFederateInfoSetOutputDelay(fi, outputDelay):
    return _helics.helicsFederateInfoSetOutputDelay(fi, outputDelay)
helicsFederateInfoSetOutputDelay = _helics.helicsFederateInfoSetOutputDelay

def helicsFederateInfoSetTimeDelta(fi, timeDelta):
    return _helics.helicsFederateInfoSetTimeDelta(fi, timeDelta)
helicsFederateInfoSetTimeDelta = _helics.helicsFederateInfoSetTimeDelta

def helicsFederateInfoSetInputDelay(fi, inputDelay):
    return _helics.helicsFederateInfoSetInputDelay(fi, inputDelay)
helicsFederateInfoSetInputDelay = _helics.helicsFederateInfoSetInputDelay

def helicsFederateInfoSetTimeOffset(fi, timeOffset):
    return _helics.helicsFederateInfoSetTimeOffset(fi, timeOffset)
helicsFederateInfoSetTimeOffset = _helics.helicsFederateInfoSetTimeOffset

def helicsFederateInfoSetPeriod(fi, period):
    return _helics.helicsFederateInfoSetPeriod(fi, period)
helicsFederateInfoSetPeriod = _helics.helicsFederateInfoSetPeriod

def helicsFederateInfoSetMaxIterations(fi, maxIterations):
    return _helics.helicsFederateInfoSetMaxIterations(fi, maxIterations)
helicsFederateInfoSetMaxIterations = _helics.helicsFederateInfoSetMaxIterations

def helicsFederateInfoSetLoggingLevel(fi, logLevel):
    return _helics.helicsFederateInfoSetLoggingLevel(fi, logLevel)
helicsFederateInfoSetLoggingLevel = _helics.helicsFederateInfoSetLoggingLevel

def helicsFederateFinalize(fed):
    return _helics.helicsFederateFinalize(fed)
helicsFederateFinalize = _helics.helicsFederateFinalize

def helicsFederateFree(fed):
    return _helics.helicsFederateFree(fed)
helicsFederateFree = _helics.helicsFederateFree

def helicsCloseLibrary():
    return _helics.helicsCloseLibrary()
helicsCloseLibrary = _helics.helicsCloseLibrary

def helicsFederateEnterInitializationMode(fed):
    return _helics.helicsFederateEnterInitializationMode(fed)
helicsFederateEnterInitializationMode = _helics.helicsFederateEnterInitializationMode

def helicsFederateEnterInitializationModeAsync(fed):
    return _helics.helicsFederateEnterInitializationModeAsync(fed)
helicsFederateEnterInitializationModeAsync = _helics.helicsFederateEnterInitializationModeAsync

def helicsFederateIsAsyncOperationCompleted(fed):
    return _helics.helicsFederateIsAsyncOperationCompleted(fed)
helicsFederateIsAsyncOperationCompleted = _helics.helicsFederateIsAsyncOperationCompleted

def helicsFederateEnterInitializationModeComplete(fed):
    return _helics.helicsFederateEnterInitializationModeComplete(fed)
helicsFederateEnterInitializationModeComplete = _helics.helicsFederateEnterInitializationModeComplete

def helicsFederateEnterExecutionMode(fed):
    return _helics.helicsFederateEnterExecutionMode(fed)
helicsFederateEnterExecutionMode = _helics.helicsFederateEnterExecutionMode

def helicsFederateEnterExecutionModeAsync(fed):
    return _helics.helicsFederateEnterExecutionModeAsync(fed)
helicsFederateEnterExecutionModeAsync = _helics.helicsFederateEnterExecutionModeAsync

def helicsFederateEnterExecutionModeComplete(fed):
    return _helics.helicsFederateEnterExecutionModeComplete(fed)
helicsFederateEnterExecutionModeComplete = _helics.helicsFederateEnterExecutionModeComplete

def helicsFederateEnterExecutionModeIterative(fed, iterate, outIterate):
    return _helics.helicsFederateEnterExecutionModeIterative(fed, iterate, outIterate)
helicsFederateEnterExecutionModeIterative = _helics.helicsFederateEnterExecutionModeIterative

def helicsFederateEnterExecutionModeIterativeAsync(fed, iterate):
    return _helics.helicsFederateEnterExecutionModeIterativeAsync(fed, iterate)
helicsFederateEnterExecutionModeIterativeAsync = _helics.helicsFederateEnterExecutionModeIterativeAsync

def helicsFederateEnterExecutionModeIterativeComplete(fed, outIterate):
    return _helics.helicsFederateEnterExecutionModeIterativeComplete(fed, outIterate)
helicsFederateEnterExecutionModeIterativeComplete = _helics.helicsFederateEnterExecutionModeIterativeComplete

def helicsFederateGetState(fed, state):
    return _helics.helicsFederateGetState(fed, state)
helicsFederateGetState = _helics.helicsFederateGetState

def helicsFederateGetCoreObject(fed):
    return _helics.helicsFederateGetCoreObject(fed)
helicsFederateGetCoreObject = _helics.helicsFederateGetCoreObject

def helicsFederateRequestTime(fed, requestTime):
    return _helics.helicsFederateRequestTime(fed, requestTime)
helicsFederateRequestTime = _helics.helicsFederateRequestTime

def helicsFederateRequestTimeIterative(fed, requestTime, iterate, outIterate):
    return _helics.helicsFederateRequestTimeIterative(fed, requestTime, iterate, outIterate)
helicsFederateRequestTimeIterative = _helics.helicsFederateRequestTimeIterative

def helicsFederateRequestTimeAsync(fed, requestTime):
    return _helics.helicsFederateRequestTimeAsync(fed, requestTime)
helicsFederateRequestTimeAsync = _helics.helicsFederateRequestTimeAsync

def helicsFederateRequestTimeComplete(fed):
    return _helics.helicsFederateRequestTimeComplete(fed)
helicsFederateRequestTimeComplete = _helics.helicsFederateRequestTimeComplete

def helicsFederateRequestTimeIterativeAsync(fed, requestTime, iterate):
    return _helics.helicsFederateRequestTimeIterativeAsync(fed, requestTime, iterate)
helicsFederateRequestTimeIterativeAsync = _helics.helicsFederateRequestTimeIterativeAsync

def helicsFederateRequestTimeIterativeComplete(fed, outIterate):
    return _helics.helicsFederateRequestTimeIterativeComplete(fed, outIterate)
helicsFederateRequestTimeIterativeComplete = _helics.helicsFederateRequestTimeIterativeComplete

def helicsFederateGetName(fed, str, maxlen):
    return _helics.helicsFederateGetName(fed, str, maxlen)
helicsFederateGetName = _helics.helicsFederateGetName

def helicsFederateSetTimeDelta(fed, time):
    return _helics.helicsFederateSetTimeDelta(fed, time)
helicsFederateSetTimeDelta = _helics.helicsFederateSetTimeDelta

def helicsFederateSetOutputDelay(fed, outputDelay):
    return _helics.helicsFederateSetOutputDelay(fed, outputDelay)
helicsFederateSetOutputDelay = _helics.helicsFederateSetOutputDelay

def helicsFederateSetInputDelay(fed, inputDelay):
    return _helics.helicsFederateSetInputDelay(fed, inputDelay)
helicsFederateSetInputDelay = _helics.helicsFederateSetInputDelay

def helicsFederateSetPeriod(fed, period, offset):
    return _helics.helicsFederateSetPeriod(fed, period, offset)
helicsFederateSetPeriod = _helics.helicsFederateSetPeriod

def helicsFederateSetFlag(fed, flag, flagValue):
    return _helics.helicsFederateSetFlag(fed, flag, flagValue)
helicsFederateSetFlag = _helics.helicsFederateSetFlag

def helicsFederateSetLoggingLevel(fed, loggingLevel):
    return _helics.helicsFederateSetLoggingLevel(fed, loggingLevel)
helicsFederateSetLoggingLevel = _helics.helicsFederateSetLoggingLevel

def helicsFederateGetCurrentTime(fed):
    return _helics.helicsFederateGetCurrentTime(fed)
helicsFederateGetCurrentTime = _helics.helicsFederateGetCurrentTime

def helicsCreateQuery(target, query):
    return _helics.helicsCreateQuery(target, query)
helicsCreateQuery = _helics.helicsCreateQuery

def helicsQueryExecute(query, fed):
    return _helics.helicsQueryExecute(query, fed)
helicsQueryExecute = _helics.helicsQueryExecute

def helicsQueryExecuteAsync(query, fed):
    return _helics.helicsQueryExecuteAsync(query, fed)
helicsQueryExecuteAsync = _helics.helicsQueryExecuteAsync

def helicsQueryExecuteComplete(query):
    return _helics.helicsQueryExecuteComplete(query)
helicsQueryExecuteComplete = _helics.helicsQueryExecuteComplete

def helicsQueryIsCompleted(query):
    return _helics.helicsQueryIsCompleted(query)
helicsQueryIsCompleted = _helics.helicsQueryIsCompleted

def helicsQueryFree(arg1):
    return _helics.helicsQueryFree(arg1)
helicsQueryFree = _helics.helicsQueryFree
HELICS_STRING_TYPE = _helics.HELICS_STRING_TYPE
HELICS_DOUBLE_TYPE = _helics.HELICS_DOUBLE_TYPE
HELICS_INT_TYPE = _helics.HELICS_INT_TYPE
HELICS_COMPLEX_TYPE = _helics.HELICS_COMPLEX_TYPE
HELICS_VECTOR_TYPE = _helics.HELICS_VECTOR_TYPE
HELICS_RAW_TYPE = _helics.HELICS_RAW_TYPE

def helicsFederateRegisterSubscription(fed, key, type, units):
    return _helics.helicsFederateRegisterSubscription(fed, key, type, units)
helicsFederateRegisterSubscription = _helics.helicsFederateRegisterSubscription

def helicsFederateRegisterTypeSubscription(fed, key, type, units):
    return _helics.helicsFederateRegisterTypeSubscription(fed, key, type, units)
helicsFederateRegisterTypeSubscription = _helics.helicsFederateRegisterTypeSubscription

def helicsFederateRegisterOptionalSubscription(fed, key, type, units):
    return _helics.helicsFederateRegisterOptionalSubscription(fed, key, type, units)
helicsFederateRegisterOptionalSubscription = _helics.helicsFederateRegisterOptionalSubscription

def helicsFederateRegisterOptionalTypeSubscription(fed, key, type, units):
    return _helics.helicsFederateRegisterOptionalTypeSubscription(fed, key, type, units)
helicsFederateRegisterOptionalTypeSubscription = _helics.helicsFederateRegisterOptionalTypeSubscription

def helicsFederateRegisterPublication(fed, key, type, units):
    return _helics.helicsFederateRegisterPublication(fed, key, type, units)
helicsFederateRegisterPublication = _helics.helicsFederateRegisterPublication

def helicsFederateRegisterTypePublication(fed, key, type, units):
    return _helics.helicsFederateRegisterTypePublication(fed, key, type, units)
helicsFederateRegisterTypePublication = _helics.helicsFederateRegisterTypePublication

def helicsFederateRegisterGlobalPublication(fed, key, type, units):
    return _helics.helicsFederateRegisterGlobalPublication(fed, key, type, units)
helicsFederateRegisterGlobalPublication = _helics.helicsFederateRegisterGlobalPublication

def helicsFederateRegisterGlobalTypePublication(fed, key, type, units):
    return _helics.helicsFederateRegisterGlobalTypePublication(fed, key, type, units)
helicsFederateRegisterGlobalTypePublication = _helics.helicsFederateRegisterGlobalTypePublication

def helicsPublicationPublish(pub, data, len):
    return _helics.helicsPublicationPublish(pub, data, len)
helicsPublicationPublish = _helics.helicsPublicationPublish

def helicsPublicationPublishString(pub, str):
    return _helics.helicsPublicationPublishString(pub, str)
helicsPublicationPublishString = _helics.helicsPublicationPublishString

def helicsPublicationPublishInteger(pub, val):
    return _helics.helicsPublicationPublishInteger(pub, val)
helicsPublicationPublishInteger = _helics.helicsPublicationPublishInteger

def helicsPublicationPublishDouble(pub, val):
    return _helics.helicsPublicationPublishDouble(pub, val)
helicsPublicationPublishDouble = _helics.helicsPublicationPublishDouble

def helicsPublicationPublishComplex(pub, real, imag):
    return _helics.helicsPublicationPublishComplex(pub, real, imag)
helicsPublicationPublishComplex = _helics.helicsPublicationPublishComplex

def helicsPublicationPublishVector(pub, data, len):
    return _helics.helicsPublicationPublishVector(pub, data, len)
helicsPublicationPublishVector = _helics.helicsPublicationPublishVector

def helicsSubscriptionGetValueSize(sub):
    return _helics.helicsSubscriptionGetValueSize(sub)
helicsSubscriptionGetValueSize = _helics.helicsSubscriptionGetValueSize

def helicsSubscriptionGetValue(sub, data, maxlen, actualLength):
    return _helics.helicsSubscriptionGetValue(sub, data, maxlen, actualLength)
helicsSubscriptionGetValue = _helics.helicsSubscriptionGetValue

def helicsSubscriptionGetString(sub, str, maxlen):
    return _helics.helicsSubscriptionGetString(sub, str, maxlen)
helicsSubscriptionGetString = _helics.helicsSubscriptionGetString

def helicsSubscriptionGetInteger(sub, val):
    return _helics.helicsSubscriptionGetInteger(sub, val)
helicsSubscriptionGetInteger = _helics.helicsSubscriptionGetInteger

def helicsSubscriptionGetDouble(sub):
    return _helics.helicsSubscriptionGetDouble(sub)
helicsSubscriptionGetDouble = _helics.helicsSubscriptionGetDouble

def helicsSubscriptionGetComplex(sub):
    return _helics.helicsSubscriptionGetComplex(sub)
helicsSubscriptionGetComplex = _helics.helicsSubscriptionGetComplex

def helicsSubscriptionGetVectorSize(sub):
    return _helics.helicsSubscriptionGetVectorSize(sub)
helicsSubscriptionGetVectorSize = _helics.helicsSubscriptionGetVectorSize

def helicsSubscriptionGetVector(sub, data, maxlen, actualSize):
    return _helics.helicsSubscriptionGetVector(sub, data, maxlen, actualSize)
helicsSubscriptionGetVector = _helics.helicsSubscriptionGetVector

def helicsSubscriptionSetDefault(sub, data, len):
    return _helics.helicsSubscriptionSetDefault(sub, data, len)
helicsSubscriptionSetDefault = _helics.helicsSubscriptionSetDefault

def helicsSubscriptionSetDefaultString(sub, str):
    return _helics.helicsSubscriptionSetDefaultString(sub, str)
helicsSubscriptionSetDefaultString = _helics.helicsSubscriptionSetDefaultString

def helicsSubscriptionSetDefaultInteger(sub, val):
    return _helics.helicsSubscriptionSetDefaultInteger(sub, val)
helicsSubscriptionSetDefaultInteger = _helics.helicsSubscriptionSetDefaultInteger

def helicsSubscriptionSetDefaultDouble(sub, val):
    return _helics.helicsSubscriptionSetDefaultDouble(sub, val)
helicsSubscriptionSetDefaultDouble = _helics.helicsSubscriptionSetDefaultDouble

def helicsSubscriptionSetDefaultComplex(sub, real, imag):
    return _helics.helicsSubscriptionSetDefaultComplex(sub, real, imag)
helicsSubscriptionSetDefaultComplex = _helics.helicsSubscriptionSetDefaultComplex

def helicsSubscriptionSetDefaultVector(sub, len):
    return _helics.helicsSubscriptionSetDefaultVector(sub, len)
helicsSubscriptionSetDefaultVector = _helics.helicsSubscriptionSetDefaultVector

def helicsSubscriptionGetType(sub, str, maxlen):
    return _helics.helicsSubscriptionGetType(sub, str, maxlen)
helicsSubscriptionGetType = _helics.helicsSubscriptionGetType

def helicsPublicationGetType(pub, str, maxlen):
    return _helics.helicsPublicationGetType(pub, str, maxlen)
helicsPublicationGetType = _helics.helicsPublicationGetType

def helicsSubscriptionGetKey(sub, str, maxlen):
    return _helics.helicsSubscriptionGetKey(sub, str, maxlen)
helicsSubscriptionGetKey = _helics.helicsSubscriptionGetKey

def helicsPublicationGetKey(pub, str, maxlen):
    return _helics.helicsPublicationGetKey(pub, str, maxlen)
helicsPublicationGetKey = _helics.helicsPublicationGetKey

def helicsSubscriptionGetUnits(sub, str, maxlen):
    return _helics.helicsSubscriptionGetUnits(sub, str, maxlen)
helicsSubscriptionGetUnits = _helics.helicsSubscriptionGetUnits

def helicsPublicationGetUnits(pub, str, maxlen):
    return _helics.helicsPublicationGetUnits(pub, str, maxlen)
helicsPublicationGetUnits = _helics.helicsPublicationGetUnits

def helicsSubscriptionIsUpdated(sub):
    return _helics.helicsSubscriptionIsUpdated(sub)
helicsSubscriptionIsUpdated = _helics.helicsSubscriptionIsUpdated

def helicsSubscriptionLastUpdateTime(sub):
    return _helics.helicsSubscriptionLastUpdateTime(sub)
helicsSubscriptionLastUpdateTime = _helics.helicsSubscriptionLastUpdateTime

def helicsFederateRegisterEndpoint(fed, name, type):
    return _helics.helicsFederateRegisterEndpoint(fed, name, type)
helicsFederateRegisterEndpoint = _helics.helicsFederateRegisterEndpoint

def helicsFederateRegisterGlobalEndpoint(fed, name, type):
    return _helics.helicsFederateRegisterGlobalEndpoint(fed, name, type)
helicsFederateRegisterGlobalEndpoint = _helics.helicsFederateRegisterGlobalEndpoint

def helicsEndpointSetDefaultDestination(endpoint, dest):
    return _helics.helicsEndpointSetDefaultDestination(endpoint, dest)
helicsEndpointSetDefaultDestination = _helics.helicsEndpointSetDefaultDestination

def helicsEndpointSendMessageRaw(endpoint, dest, data, len):
    return _helics.helicsEndpointSendMessageRaw(endpoint, dest, data, len)
helicsEndpointSendMessageRaw = _helics.helicsEndpointSendMessageRaw

def helicsEndpointSendEventRaw(endpoint, dest, data, len, time):
    return _helics.helicsEndpointSendEventRaw(endpoint, dest, data, len, time)
helicsEndpointSendEventRaw = _helics.helicsEndpointSendEventRaw

def helicsEndpointSendMessage(endpoint, message):
    return _helics.helicsEndpointSendMessage(endpoint, message)
helicsEndpointSendMessage = _helics.helicsEndpointSendMessage

def helicsEndpointSubscribe(endpoint, key, type):
    return _helics.helicsEndpointSubscribe(endpoint, key, type)
helicsEndpointSubscribe = _helics.helicsEndpointSubscribe

def helicsFederateHasMessage(fed):
    return _helics.helicsFederateHasMessage(fed)
helicsFederateHasMessage = _helics.helicsFederateHasMessage

def helicsEndpointHasMessage(endpoint):
    return _helics.helicsEndpointHasMessage(endpoint)
helicsEndpointHasMessage = _helics.helicsEndpointHasMessage

def helicsFederateReceiveCount(fed):
    return _helics.helicsFederateReceiveCount(fed)
helicsFederateReceiveCount = _helics.helicsFederateReceiveCount

def helicsEndpointReceiveCount(endpoint):
    return _helics.helicsEndpointReceiveCount(endpoint)
helicsEndpointReceiveCount = _helics.helicsEndpointReceiveCount

def helicsEndpointGetMessage(endpoint):
    return _helics.helicsEndpointGetMessage(endpoint)
helicsEndpointGetMessage = _helics.helicsEndpointGetMessage

def helicsFederateGetMessage(fed):
    return _helics.helicsFederateGetMessage(fed)
helicsFederateGetMessage = _helics.helicsFederateGetMessage

def helicsEndpointGetType(endpoint, str, maxlen):
    return _helics.helicsEndpointGetType(endpoint, str, maxlen)
helicsEndpointGetType = _helics.helicsEndpointGetType

def helicsEndpointGetName(endpoint, str, maxlen):
    return _helics.helicsEndpointGetName(endpoint, str, maxlen)
helicsEndpointGetName = _helics.helicsEndpointGetName

def helicsFederateRegisterSourceFilter(fed, type, target, name):
    return _helics.helicsFederateRegisterSourceFilter(fed, type, target, name)
helicsFederateRegisterSourceFilter = _helics.helicsFederateRegisterSourceFilter

def helicsFederateRegisterDestinationFilter(fed, type, target, name):
    return _helics.helicsFederateRegisterDestinationFilter(fed, type, target, name)
helicsFederateRegisterDestinationFilter = _helics.helicsFederateRegisterDestinationFilter

def helicsFederateRegisterCloningFilter(fed, deliveryEndpoint):
    return _helics.helicsFederateRegisterCloningFilter(fed, deliveryEndpoint)
helicsFederateRegisterCloningFilter = _helics.helicsFederateRegisterCloningFilter

def helicsCoreRegisterSourceFilter(core, type, target, name):
    return _helics.helicsCoreRegisterSourceFilter(core, type, target, name)
helicsCoreRegisterSourceFilter = _helics.helicsCoreRegisterSourceFilter

def helicsCoreRegisterDestinationFilter(core, type, target, name):
    return _helics.helicsCoreRegisterDestinationFilter(core, type, target, name)
helicsCoreRegisterDestinationFilter = _helics.helicsCoreRegisterDestinationFilter

def helicsCoreRegisterCloningFilter(fed, deliveryEndpoint):
    return _helics.helicsCoreRegisterCloningFilter(fed, deliveryEndpoint)
helicsCoreRegisterCloningFilter = _helics.helicsCoreRegisterCloningFilter

def helicsFilterGetTarget(filt, str, maxlen):
    return _helics.helicsFilterGetTarget(filt, str, maxlen)
helicsFilterGetTarget = _helics.helicsFilterGetTarget

def helicsFilterGetName(filt, str, maxlen):
    return _helics.helicsFilterGetName(filt, str, maxlen)
helicsFilterGetName = _helics.helicsFilterGetName

def helicsFilterSet(filt, property, val):
    return _helics.helicsFilterSet(filt, property, val)
helicsFilterSet = _helics.helicsFilterSet

def setString(filt, property, val):
    return _helics.setString(filt, property, val)
setString = _helics.setString

def helicsFilterAddDestinationTarget(filt, dest):
    return _helics.helicsFilterAddDestinationTarget(filt, dest)
helicsFilterAddDestinationTarget = _helics.helicsFilterAddDestinationTarget

def helicsFilterAddSourceTarget(filt, dest):
    return _helics.helicsFilterAddSourceTarget(filt, dest)
helicsFilterAddSourceTarget = _helics.helicsFilterAddSourceTarget

def helicsFilterAddDeliveryEndpoint(filt, dest):
    return _helics.helicsFilterAddDeliveryEndpoint(filt, dest)
helicsFilterAddDeliveryEndpoint = _helics.helicsFilterAddDeliveryEndpoint

def helicsFilterRemoveDestinationTarget(filt, dest):
    return _helics.helicsFilterRemoveDestinationTarget(filt, dest)
helicsFilterRemoveDestinationTarget = _helics.helicsFilterRemoveDestinationTarget

def helicsFilterRemoveSourceTarget(filt, dest):
    return _helics.helicsFilterRemoveSourceTarget(filt, dest)
helicsFilterRemoveSourceTarget = _helics.helicsFilterRemoveSourceTarget

def helicsFilterRemoveDeliveryEndpoint(filt, dest):
    return _helics.helicsFilterRemoveDeliveryEndpoint(filt, dest)
helicsFilterRemoveDeliveryEndpoint = _helics.helicsFilterRemoveDeliveryEndpoint
# This file is compatible with both classic and new-style classes.


