from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil


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