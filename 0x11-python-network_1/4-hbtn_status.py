#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using the requests package.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    data = response.json()

    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data['status'])
