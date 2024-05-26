import requests
from datetime import datetime

#create pixela endpoint
Endpoint = "https://pixe.la/v1/users"
Username = "akinduk"
Password = "fggpv445apggr"
GraphID = "study-graph"
date = datetime.today().date()

#set the required parameters
user_param = {
    "token": Password,
    "username": Username,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",
}
#create the header file for http requests

#send a post request to the server

respond = requests.post(url=Endpoint, json=user_param)
print(respond.text)

#create graph end point
graph_endpoint = f"{Endpoint}/{Username}/graphs"

#graph configuration

graph_config = {
  "id": GraphID,
  "name": "Study Hours",
  "unit": "hours",
  "type": "float",
  "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": Password,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

#create the data endpoint to send the data
data_endpoint = f"{Endpoint}/{Username}/graphs/{GraphID}"

data_config = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("Enter the amount of time spent on reading?"),

}
response = requests.post(url=data_endpoint, json=data_config, headers=headers)
print(response.text)

#update endpoint for updating the data
update_endpoint = f"{Endpoint}/{Username}/graphs/{GraphID}/{date.strftime('%Y%m%d')}"

new_data = {
    "quantity": "5",
}

response = requests.post(url=update_endpoint, json=new_data, headers=headers)
print(response.text)

#delete endpoint for deleting existing data
delete_endpoint = f"{Endpoint}/{Username}/graphs/{GraphID}/{date.strftime('%Y%m%d')}"
response = requests.post(url=delete_endpoint, headers=headers)
print(response.text)


