#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3
import requests

# Collect hundreds or thousands of news or more with Python and mediastack
r = requests.get("http://api.mediastack.com/v1/news?access_key=YOUR_ACCESS_KEY&categories=business,technology&limit=100")

responses = r.json()
responses

# Collect specific news with their index
responses['data'][0]
responses['data'][27]
responses['data'][100]

# Get specific data individually using API response objects?
responses['data'][0]['author']
responses['data'][0]['category']
responses['data'][0]['country']
responses['data'][0]['description']
responses['data'][0]['image']
responses['data'][0]['language']
responses['data'][0]['published_at']
responses['data'][0]['source']
responses['data'][0]['title']
responses['data'][0]['url']

