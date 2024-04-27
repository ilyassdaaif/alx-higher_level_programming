#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status using requests."""
import requests

if __name__ == "__main__":
    try:
        r = requests.get('https://intranet.hbtn.io/status')
        r.raise_for_status()  # Raises an HTTPError for bad responses
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
    except requests.exceptions.RequestException as e:
        print("Error fetching the URL: {}".format(e))
