from json.tool import main
import urllib.request , json , os , sys , platform
from datetime import datetime

if len(sys.argv) == 1:
	try:
		req_ip = urllib.request.urlopen('http://ip-api.com/json/')
		req_ip_json = json.loads(req_ip.read())
		print('\nRequested IP: '+req_ip_json['query'])
		print('Search status: '+req_ip_json['status'])
		print('Country: '+ req_ip_json['country'])
		print('Country code: ' + req_ip_json['countryCode'])
		print('Region: '+req_ip_json['region'])
		print('Region Name: ' + req_ip_json['regionName'])
		print('City: '+req_ip_json['city'])
		print('Zip: ' + req_ip_json['zip'])
		print('latitude: '+str(req_ip_json['lat']))
		print('longitude: '+str(req_ip_json['lon']))
		print('Timezone: '+str(req_ip_json['timezone']))
		print('ISP: '+req_ip_json['isp'])
		print('Organisation: '+req_ip_json['org'])
		print(req_ip_json['as'])
	except:
		print("[-] Error occured")

elif len(sys.argv) == 2:
	try:
		req_ip = urllib.request.urlopen('http://ip-api.com/json/'+ sys.argv[1])
		req_ip_json = json.loads(req_ip.read())
		print('\nRequested IP: '+req_ip_json['query'])
		print('Search status: '+req_ip_json['status'])
		print('Country: '+ req_ip_json['country'])
		print('Country code: ' + req_ip_json['countryCode'])
		print('Region: '+req_ip_json['region'])
		print('Region Name: ' + req_ip_json['regionName'])
		print('City: '+req_ip_json['city'])
		print('Zip: ' + req_ip_json['zip'])
		print('latitude: '+str(req_ip_json['lat']))
		print('longitude: '+str(req_ip_json['lon']))
		print('Timezone: '+str(req_ip_json['timezone']))
		print('ISP: '+req_ip_json['isp'])
		print('Organisation: '+req_ip_json['org'])
		print(req_ip_json['as'])
	except:
		print("[-] Error occured")
