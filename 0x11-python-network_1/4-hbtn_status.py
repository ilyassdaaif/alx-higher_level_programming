#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using the requests package.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    response_dict = response.json()

    print("Body response:")
    print("\t- type: {}".format(type(response_dict)))
    print("\t- content: {}".format(response_dict['status']))
