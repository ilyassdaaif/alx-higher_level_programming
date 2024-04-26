#!/usr/bin/python3
import requests

def fetch_status():
    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        content = response.text
        print("Body response:$")
        print("\t- type: {}$".format(type(content)))
        print("\t- content: {}$")
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}$")

if __name__ == "__main__":
    fetch_status()
