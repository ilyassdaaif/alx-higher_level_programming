#!/usr/bin/python3
import requests

def fetch_status():
    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            print("Body response:$")
            print("\t- type: {}$".format(type(content)))
            print("\t- content: {}$".format(content))
        else:
            print(f"Failed to fetch data: HTTP {response.status_code}$")
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}$")

if __name__ == "__main__":
    fetch_status()
