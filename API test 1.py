# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 00:15:38 2020

@author: TheKa
"""

import requests

response = requests.get("http://open-notify.org/")
print(response.status_code)
print(response.text)
