/*

Copyright (C) 2017, Battelle Memorial Institute
All rights reserved.

This software was co-developed by Pacific Northwest National Laboratory, operated by the Battelle Memorial
Institute; the National Renewable Energy Laboratory, operated by the Alliance for Sustainable Energy, LLC; and the
Lawrence Livermore National Laboratory, operated by Lawrence Livermore National Security, LLC.

*/
#ifndef ACTION_MESSAGE_DEFINITIONS_
#define ACTION_MESSAGE_DEFINITIONS_
#pragma once

namespace helics
{
namespace action_message_def
{
const int32_t cmd_info_basis = 65536;

/** enumeration of globally recognized commands
@details they are explicitly numbered for debugging and to ensure the enumeration is constant
across different compilers*/
enum action_t : int32_t
{
	cmd_ignore = 0,

	cmd_disconnect = 3,  //!< command to disconnect a broker from a higher level broker
	cmd_init = 5,  //!< request entry to init mode
	cmd_init_grant = 7,  //!< grant entry to initialization mode
	cmd_init_not_ready = 8,  //!< retract an init ready command
	cmd_exec_request = 9,  //!< request an iteration or entry to execution mode
	cmd_exec_grant = 10,  //!< grant entry to exec mode or iterate
	cmd_exec_check = 12,  //!< command to run a check on execution entry
	cmd_register_route = 15,  //!< instructions to create a direct route to another federate
	cmd_route_ack = 16,  //!< acknowledge reply to a route registration
	cmd_stop = 20,  //!< halt execution
	cmd_terminate_immediately = 22, //!< immediate halt no-disconnect;
	cmd_fed_ack = 25,  //!<a reply with the global id or an error if the fed registration failed
	cmd_broker_ack = 27,  // a reply to the connect command with a global route id
	cmd_add_route = 32,  //!< command to define a route
	cmd_time_grant = 35,  //!< grant a time or iteration
	cmd_time_check = 36,  //!< command to run a check on whether time can be granted
	cmd_pub = 45,  //!< publish a value
	cmd_bye = 2000,  //!< message stating this is the last communication from a federate
	cmd_log = 55,  //!< log a message with the root broker
	cmd_warning = 9990,  //!< indicate some sort of warning
	cmd_error = 10000,  //!< indicate an error with a federate

	cmd_send_route = 75,  //!< command to define a route information
	cmd_subscriber = 85,  // !< command to send a subscriber
	cmd_add_dependency = 95,  //!< command to send a federate dependency information
	cmd_remove_dependency = 97,  //!< command to remove a dependency
	cmd_add_dependent = 98,  //!< command to add a dependent to a federate
	cmd_remove_dependent = 99,  //!< command to remove a dependent from a federates consideration
	cmd_reg_fed = 105,  //!< register a federate
						// commands that require the extra info allocation have numbers greater than cmd_info_basis
						cmd_time_request = cmd_info_basis + 10,  //!< request a time or iteration
						cmd_send_message = cmd_info_basis + 20,  //!< send a message
						cmd_send_for_filter = cmd_info_basis + 30,  //!< send a message to be filtered

						cmd_reg_broker = cmd_info_basis + 40,  //!< for a broker to connect with a higher level broker
						cmd_reg_pub = cmd_info_basis + 50,  //!< register a publication
						cmd_notify_pub = 50,  //!< notify of a publication
						cmd_reg_dst = cmd_info_basis + 60,  //!< register a destination filter
						cmd_notify_dst = 60,  //!< notify of a destination filter
						cmd_reg_sub = cmd_info_basis + 70,  //!< register a subscription
						cmd_notify_sub = 70,  //!< notify of a subscription
						cmd_reg_src = cmd_info_basis + 80,  //!< register a source filter
						cmd_notify_src = 80,  //!< notify of a source
						cmd_reg_end = cmd_info_basis + 90,  //!< register an endpoint
						cmd_notify_end = 90,  //!< notify of an endpoint

						cmd_protocol = 60000,  //!< cmd used in the protocol stacks and ignored by the core
						cmd_protocol_big = 0x0F00 + 60000  //!< cmd used in the protocol stacks with the additional info
};

}  //namespace action_message_def

#define CMD_IGNORE action_message_def::action_t::cmd_ignore
#define CMD_REG_BROKER action_message_def::action_t::cmd_reg_broker
#define CMD_DISCONNECT action_message_def::action_t::cmd_disconnect
#define CMD_INIT action_message_def::action_t::cmd_init
#define CMD_INIT_NOT_READY action_message_def::action_t::cmd_init_not_ready
#define CMD_INIT_GRANT action_message_def::action_t::cmd_init_grant
#define CMD_EXEC_REQUEST action_message_def::action_t::cmd_exec_request
#define CMD_EXEC_GRANT action_message_def::action_t::cmd_exec_grant
#define CMD_EXEC_CHECK action_message_def::action_t::cmd_exec_check
#define CMD_REG_ROUTE action_message_def::action_t::cmd_register_route
#define CMD_ROUTE_ACK action_message_def::action_t::cmd_route_ack
#define CMD_STOP action_message_def::action_t::cmd_stop
#define CMD_TERMINATE_IMMEDIATELY action_message_def::action_t::cmd_terminate_immediately
#define CMD_TIME_REQUEST action_message_def::action_t::cmd_time_request
#define CMD_TIME_GRANT action_message_def::action_t::cmd_time_grant
#define CMD_TIME_CHECK action_message_def::action_t::cmd_time_check
#define CMD_SEND_MESSAGE action_message_def::action_t::cmd_send_message
#define CMD_SEND_FOR_FILTER action_message_def::action_t::cmd_send_for_filter
#define CMD_PUB action_message_def::action_t::cmd_pub
#define CMD_LOG action_message_def::action_t::cmd_log
#define CMD_WARNING action_message_def::action_t::cmd_warning
#define CMD_ERROR action_message_def::action_t::cmd_error
#define CMD_REG_PUB action_message_def::action_t::cmd_reg_pub
#define CMD_NOTIFY_PUB action_message_def::action_t::cmd_notify_pub
#define CMD_REG_SUB action_message_def::action_t::cmd_reg_sub
#define CMD_NOTIFY_SUB action_message_def::action_t::cmd_notify_sub
#define CMD_REG_END action_message_def::action_t::cmd_reg_end
#define CMD_NOTIFY_END action_message_def::action_t::cmd_notify_end
#define CMD_REG_DST_FILTER action_message_def::action_t::cmd_reg_dst
#define CMD_NOTIFY_DST_FILTER action_message_def::action_t::cmd_notify_dst
#define CMD_REG_SRC_FILTER action_message_def::action_t::cmd_reg_src
#define CMD_NOTIFY_SRC_FILTER action_message_def::action_t::cmd_notify_src

#define CMD_ADD_DEPENDENCY action_message_def::action_t::cmd_add_dependency
#define CMD_REMOVE_DEPENDENCY action_message_def::action_t::cmd_remove_dependency
#define CMD_ADD_DEPENDENT action_message_def::action_t::cmd_add_dependent
#define CMD_REMOVE_DEPENDENT action_message_def::action_t::cmd_remove_dependent

#define CMD_REG_FED action_message_def::action_t::cmd_reg_fed
#define CMD_BROKER_ACK action_message_def::action_t::cmd_broker_ack
#define CMD_FED_ACK action_message_def::action_t::cmd_fed_ack
#define CMD_PROTOCOL action_message_def::action_t::cmd_protocol
#define CMD_PROTOCOL_BIG action_message_def::action_t::cmd_protocol_big
}  // namespace helics
#endif  // ACTION_MESSAGE_DEFINITIONS_
