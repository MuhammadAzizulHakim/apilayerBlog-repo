#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3
import requests

# Collect 100 of news or more with Python and mediastack
# Language = en, Categories = Business, Technology
r = requests.get("http://api.mediastack.com/v1/news?access_key=YOUR_ACCESS_KEY&languages=en&categories=business,technology&limit=100")

responses = r.json()
responses

# Define the collected API responses
mediastackData = responses['data']

# Normalize or unnest the JSON response
from pandas.io.json import json_normalize
flatData = json_normalize(mediastackData)

# Create data frame, and save them to CSV
import pandas as pd
df = pd.DataFrame(flatData)
df.to_csv("mediastackSample.csv", encoding = 'utf-8', index = False)