from api_library import DroneController
import time

droneHandle = DroneController('TOKEN', 'VehiclelID')

print droneHandle.position_hold()
