from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil


#Connect to rover
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect',
                    help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()
connection_string = args.connect


#SITL -- Comment out if connecting to actual UGV
import dronekit_sitl
sitl=dronekit_sitl_start_default()
connection_string=sitl.connection_string()

print("Connecting to UGV")
vehicle.connect(connection_string, wait_ready=True)



#Arms Rover to Move at altitude of sea level
def arm(altitude):

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
    #--- Downloads mission#
    print("Downloading Mission")
    missionlist = []
    n_wp = 0