from sqlite3 import connect
from flask import Flask
from flask_cors import CORS
from flask import request
from flask import json
import requests
app = Flask(__name__)
CORS(app)


def connectToBookingApi(url,phone):
    payload = {}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJub25jZSI6IlBoZW5qV1RIbEZId0ZQbk93UGFfSEUwUVhrMFlkbUI3N2hRMjdia2pnNFUiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83YmFiZTNmZS04NzQ4LTQwOTgtYWRmNS04NmU0NjQwMjQ2ZDcvIiwiaWF0IjoxNjU2MTA0NzIyLCJuYmYiOjE2NTYxMDQ3MjIsImV4cCI6MTY1NjEwODk1NywiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhUQUFBQWJFZHZoR1dZMXVTS1pQdVViS2lnVTBVNFBkWHA0YjdhYkNqdHZqdHRSdm9DVm4xM2lCbnVuWlJyZTNVK1RITWFMb0JvRk1iclV2cFJGSDZ1NnJxdWQ3MWh5WEtlWm9MQldRQVVraE1zTmZBPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiYmFjay1lbmQtZmxhc2siLCJhcHBpZCI6IjVhYmQxNDVkLTZmYmItNDA5ZC1hY2NlLThjZTg3ZmM3ZTM2ZiIsImFwcGlkYWNyIjoiMSIsImZhbWlseV9uYW1lIjoiQmVycmFjaGRpIiwiZ2l2ZW5fbmFtZSI6Ik1vaGFtZWQiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMDUuMTU2LjE2MC4yMCIsIm5hbWUiOiJNb2hhbWVkIEJlcnJhY2hkaSIsIm9pZCI6IjM0MzQ2NzYyLTI1NDItNGU5OS1hMzYyLTY4MGU0MTgyNTUyYiIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMjAzNzQ0QThDIiwicmgiOiIwLkFYa0FfdU9yZTBpSG1FQ3Q5WWJrWkFKRzF3TUFBQUFBQUFBQXdBQUFBQUFBQUFDVUFNYy4iLCJzY3AiOiJCb29raW5ncy5SZWFkLkFsbCBDYWxlbmRhcnMuUmVhZCBDYWxlbmRhcnMuUmVhZFdyaXRlIG9wZW5pZCBwcm9maWxlIFVzZXIuRXhwb3J0LkFsbCBVc2VyLlJlYWQgZW1haWwiLCJzdWIiOiJTc3Eyd1pLaTlwVU1qOVpIRHh2YThkWk1JSThFVWJGV1R5d2ppazdCY0p3IiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkFGIiwidGlkIjoiN2JhYmUzZmUtODc0OC00MDk4LWFkZjUtODZlNDY0MDI0NmQ3IiwidW5pcXVlX25hbWUiOiJNb2hhbWVkQmVycmFjaGRpQElNQUdJTkU3NDYub25taWNyb3NvZnQuY29tIiwidXBuIjoiTW9oYW1lZEJlcnJhY2hkaUBJTUFHSU5FNzQ2Lm9ubWljcm9zb2Z0LmNvbSIsInV0aSI6InI1ZXg1akFlMDBPTFIwbkU1dmRNQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjYyZTkwMzk0LTY5ZjUtNDIzNy05MTkwLTAxMjE3NzE0NWUxMCIsImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoieE83RXh2VkJhVGRhZjhhVE94Vm1ISExETHQxWDBKY0RkNHlpMEJZVjkzZyJ9LCJ4bXNfdGNkdCI6MTY1NDY5ODYwMH0.GNGh2LfuC7IT8X7Bgkqijp99XWwTKFsvEml-qp5SM62AQ7rPtA_poPVwWfKsUKyIrr2f4fV5IAi-G-Ao27cO5Zs-bIZWWt0wTASQVQGBzuqvunJo3MyoGmsCVJXbkU99yMC05PSC3pdBp2tuc-wXyBBVwig-Kd2Y8VxZqrt77dZq5M7JfuErJrrpYhs-1_15N0mfHPgVuapUX79tYbuNX64B-KOn0oW9EvV4hdqYKrpB0NkMSU6w-5D-d2ZNL7DYndS6lypYvX0Vcd9Gh-Apf3yD31UhZpHHTychRQm5ktwZXAkecJcRlX7SQh-2I36exg-HUA92OjT5peZsE4cvOw'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    
    lenght = len(response.json()['value'])
    index = 0
    result = False
    fullname = ''
    email = ''
    phone = ''
    subject = ''
    timeStart = ''
    timeEnd = ''
    tab = []

    #Test if a client have a appointment
    print(request.args.get('phone'))
    while index < lenght:
        if request.args.get('phone') in response.json()['value'][index]['bodyPreview']:
            result = True
            #Extract personnel data 
           
            for line in response.json()['value'][index]['bodyPreview'].splitlines():
                if 'Nom' in line:
                    fullname = line.split(':')[1]
                if 'Adresse de courrier' in line:
                    email = line.split(':')[1]
                if 'Numéro de téléphone' in line:
                    phone = line.split(':')[1]
            
            #Extract service data
            subject = response.json()['value'][index]['subject']
            start = response.json()['value'][index]['start']['dateTime']
            end = response.json()['value'][index]['end']['dateTime']

            #Add result to response object
            dict ={"fullname":fullname, "phone":phone, "email":email, "subject":subject, "start":start, "end":end}
            tab.append(dict)
        index = index +1

        
                

    response = json.dumps(tab)
    response2 = app.response_class(
        response=response,
        status=200,
        mimetype='application/json'
    )
    
    return response2


@app.route('/api/bookings/', methods=['GET'])
def getBookingPage():

    # Check if this person with a cin = ? is not have an appointment with thes service

    cin = request.args.get('cin')
    phone = request.args.get('phone')
    #return 'https://outlook.office365.com/owa/calendar/Passeportimagineservice@IMAGINE746.onmicrosoft.com/bookings/s/WH3PioqUfEW7gvE05qd9tg2'
    # connect to api
    return connectToBookingApi('https://graph.microsoft.com/v1.0/me/events?$select=subject,body,bodyPreview,organizer,attendees,start,end,location,subject',phone)
    


if __name__ == '__main__':
    app.run(debug=True)