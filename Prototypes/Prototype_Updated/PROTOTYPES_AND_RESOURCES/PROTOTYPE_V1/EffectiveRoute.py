import requests
import json

startlocation = str(input("Enter your Start Location: "))
endlocation = str(input("Enter your destination location: "))
api_key = str(input("Enter Your Google API Key: "))
url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
params = {
  "origin": {
    "address": startlocation
  },
  "destination": {
    "address": endlocation
  },
  "travelMode": "TRANSIT",
  "computeAlternativeRoutes": "true",
  "transitPreferences": {
     "routingPreference" : "LESS_WALKING",
     "allowedTravelModes" : ["BUS"]
  }
}

headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': api_key,
    #'X-Goog-FieldMask': 'routes.legs.steps.transitDetails'
    'X-Goog-FieldMask': 'routes'
}



response = requests.post(url, json=params, headers=headers)


try:
    output_json = json.loads(response.text)
    for routes in output_json["routes"]:
        print(routes["localizedValues"])
    
except Exception as e:
    print("Got an error mofo" + e)


#print(response.text)