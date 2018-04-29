from api_library import DroneController
import time

droneHandle = DroneController('b4d793f9680ba50d385e185b619eec0c0752347d', 'HNCnaCYD')

print droneHandle.position_hold()
