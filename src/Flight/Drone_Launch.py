from api_library import DroneController
import time

drone1 = DroneController('b4d793f9680ba50d385e185b619eec0c0752347d', 'HNCnaCYD')
drone2 = DroneController('746821f921735b2510a5653f31ace5dded0bf7d1', 'wDwpZXns')
drone3 = DroneController('d7ef6762c83d16416b8f4f6ad93ede528546bb9b', 'jIuzqpPJ')

print "demo"

print "takeoff"
print drone1.take_off(5.0)
print drone2.take_off(5.0)
print drone3.take_off(5.0)

print "sleeping"
time.sleep(4.0)

