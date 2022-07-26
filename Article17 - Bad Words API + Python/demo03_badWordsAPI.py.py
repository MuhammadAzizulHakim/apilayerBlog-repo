import requests
 
url = "https://api.apilayer.com/bad_words?censor_character=censor_character"
 
payload = "You%20smell%20like%20shit.".encode("utf-8")
headers= {
  "apikey": "YOUR_API_KEY"
}
 
response = requests.request("POST", url, headers=headers, data = payload)
 
status_code = response.status_code
result = response.text