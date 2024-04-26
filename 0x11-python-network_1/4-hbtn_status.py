#!/usr/bin/python3
import requests

def fetch_status():
    # URL to fetch status from
    url = "https://alx-intranet.hbtn.io/status"
    
    # Make a GET request to the URL
    response = requests.get(url)
    
    # Get the content of the response and ensure it is of type 'str'
    content = response.text
    
    # Print the formatted output
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

if __name__ == "__main__":
    fetch_status()
