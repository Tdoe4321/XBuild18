from api_library import DroneController
import time
import json
import sys
from requests import get, put

def printResponse(msg, r):
	global armed
	#print json.loads(r.content)["longitude"]  
	armed = json.loads(r.content)["armed"]

def launchLand():
	global armed
	armed = False
	drone1 = DroneController('TOKEN', 'VehiclelID')
	token = 'TOKEN'	#replace the value with your personal access token within single quotes(')
	VehicleID = 'ID'	#replace this with the vehicle ID within single quotes (')
	token = token.replace(" ", "")
	VehicleID = VehicleID.replace(" ", "")

	headers = {'Authorization':'Token ' + token, 'VehicleID': VehicleID}

	result = get('https://dev.flytbase.com/rest/ros/get_global_namespace', headers = headers)
	result = json.loads(result.content)
	namespace = result["param_info"]["param_value"]

	printResponse( "flyt/state ", get('https://dev.flytbase.com/rest/ros/' + namespace + '/flyt/state', headers = headers))


	if (armed):
		print drone1.land(True)
		time.sleep(7)
	else:
		print drone1.take_off(2.0)
		time.sleep(6)

def main():
    launchLand()

if __name__ == '__main__':
    main()





