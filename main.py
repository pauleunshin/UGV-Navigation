from pymavlink import mavutil, mavwp

master = mavutil.mavlink_connection('tcp:localhost:11520')

master.wait_heartbeat()


# wp = mavwp.MAVWPLoader()
# seq = 1
# frame = mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
# radius = 1
# for i in range(N):
#     wp.add(mavutil.mavlink.MAVLink_mission_item_message(master.target_system,
#                                                         master.target_component,
#                                                         seq,
#                                                         frame,
#                                                         mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
#                                                         0, 0, 0, radius, 0, 0,
#                                                         lat[i], lon[i], alt[i]))
#     seq += 1
#
# boundary = mavwp.MAVFenceLoader()
# seq2 = 1
# for p in range(M):
#     boundary.add(mavutil.mavlink.MAVLink_mission_item_message(master.target_system,
#                                                               master.target_component,
#                                                               seq2,
#                                                               frame,
#                                                               mavutil.mavlink.MAVLink_fence_point_message(status),
#                                                               0, 0 , 0, radius, 0, 0,
#                                                               lat[p], lon[p], alt[p]))
#     seq2 += 1
#
#
#
# master.waypoint_clear_all_send()
# master.waypoint_count_send(wp.count())
