from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import time
import socket
import exceptions
import argparse

# Connect to rover
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect',
                    help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()
connection_string = args.connect

# SITL -- Comment out if connecting to actual UGV
import dronekit_sitl

sitl = dronekit_sitl_start_default()
connection_string = sitl.connection_string()

print("Connecting to UGV")
vehicle.connect(connection_string, wait_ready=True)


# Functions
def arm():
    while not vehicle.is_armable:
        print("Waiting to become armable")
        time.sleep(1)

    print("Motors armed")
    vehicle.armed = True
    while vehicle.armed==False:
        print("Waiting for drone to arm")
        time.sleep(1)

    return None


def clearmission(rover):
    cmds = rover.commands
    cmds.clear()
    rover.flush()

    cmds.download()
    cmds.wait_read()


def download_mission(rover):
    cmds = rover.commands
    cmds.download()
    cmds.wait_read()


def get_mission(rover):
    # --- Downloads mission#
    print("Downloading Mission")
    missionlist = []
    n_wp = 0

# Vehicle Execution
vehicle = connectMyCopter()
arm()
print("End of Script")

