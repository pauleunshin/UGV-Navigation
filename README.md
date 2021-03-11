# UGV-Navigation
Navigation code for the Unmanned Ground Vehicle in the UAV Forge 20-21 Project. 
Contains the scripts that will control the UGV's descent mechanism and navigation protocols. 

Current Objectives: DroneKit Port

Next Objectives: Apply Geofencing

# MavlinkOnly.py
This version attempts to bridge the UGV to mission planner only using Mavlink and the Pixhawk. The Pixhawk
is connected to a GCS using telemetry of choice

For our mission, we are using the RFD900x modems connected to the GCS and the Pixhawk off the
telemetry port. 

While this is pulled from previous years code, it is purely based on code provided by University of Colorado. 
This documentation can be found here. 
https://www.colorado.edu/recuv/2015/05/25/mavlink-protocol-waypoints

It does its job of bridging the connection and providing waypoint, but we must find ways to apply geofencing
on our own. 

https://mavlink.io/en/messages/common.html
This website hosts most if not all the current message types Mavlink supports, but does not provide the syntax to
properly write python code. This is with our preliminary research. There is possibly other way to write the code, but
the most common approach is through Dronekit connected through a Raspberry Pi.


# DroneKitVer.py
This version stores most of the scripting into a raspberry pi, connected locally to the Pixhawk. 

https://dronekit.io/

Geofencing data is presumably stored in vehicle.paramater. 



