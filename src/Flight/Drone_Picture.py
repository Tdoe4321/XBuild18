from api_library import DroneController
import time
import json
import sys
from requests import get, put 

def Picture():
	global lat
	lat = 0

	global lon
	lon = 0
	drone1 = DroneController('b4d793f9680ba50d385e185b619eec0c0752347d', 'HNCnaCYD')

	token = 'b4d793f9680ba50d385e185b619eec0c0752347d'	#replace the value with your personal access token within single quotes(')
	VehicleID = 'HNCnaCYD'	#replace this with the vehicle ID within single quotes (')
	token = token.replace(" ", "")
	VehicleID = VehicleID.replace(" ", "")

	headers = {'Authorization':'Token ' + token, 'VehicleID': VehicleID}

	result = get('https://dev.flytbase.com/rest/ros/get_global_namespace', headers = headers)
	result = json.loads(result.content)
	namespace = result["param_info"]["param_value"]

	lon = drone1.get_global_position()["longitude"]
	lat = drone1.get_global_position()["latitude"]

	f= open("latLon.txt","w+")
	f.write("%f\n" % (lat))
	f.write("%f\n" % (lon))
	f.close()

	print lat
	print lon

def main():
    Picture()

if __name__ == '__main__':
    main()

