#start by importing the modules broooo
import requests, webbrowser, os, sys, urllib3, json
from bs4 import BeautifulSoup as bs
# need this for suppressing warnings of insecure requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# heylab ="https://bio.cst.temple.edu/~tuf29449/"
# a = requests.get(heylab, verify=False)
# s = bs(a.text,'html.parser').prettify()
# print(s)

#this will set our working directory to be able to find the necessary documents
currentpath = os.getcwd()
newpath = os.chdir('/Users/gavinkoma/Documents/bio-python/week12')
currentpath2 = os.getcwd()

def main():
    initialrequest()
    return

def initialrequest():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    #response.content()
    print(response.status_code)

    #the data here is similar to a python dictionary and ensures that
    #the data is easily readible; think of it as a python dictionary
    #that is represented as strings

    print(response.json())

    json_response = response.json()

    dictionary = json.dumps(response.json(),sort_keys = True, indent = 4)
    print(dictionary)

    #we can also parse our data if wed like to
    longitude = json_response['iss_position']['longitude']
    latitude = json_response['iss_position']['latitude']
    print('Longitude: ', longitude)
    print('latitude: ', latitude)

main()
