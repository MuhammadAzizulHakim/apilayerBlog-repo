import requests

url = "https://api.apilayer.com/text_to_emotion"

payload = "Be%20honest!%20How%20much%20coffee%20do%20you%20need%20to%20get%20you%20through%20the%20day%3F%20According%20to%20a%20study%2C%20the%20average%20developer%20consumes%20from%20two%20to%20five%20cups%20of%20coffee%20per%20day.%20Are%20you%20Team%20coffee%20or%20team%20tea%3F%0A%23API%20%23webdevelopment%20%23coding%20%23tech%20%23developers%20%23webscraping%20%23webscrapingapi%20%23webapi".encode("utf-8")
headers= {
  "apikey": "ptAYOkX8Rmq02C1pIrh1H4ddqwglGc2b"
}

response = requests.request("POST", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)