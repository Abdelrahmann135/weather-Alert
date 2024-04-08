from twilio.rest import Client
import requests
LNG = "your lng"
LAT = "yor lat"
KEY = "cafd93a5c5xxxxxxxxxxxxxxxxxxxx"
PAR = {
    "lat": LNG,
    "lon": LAT,
    "appid": KEY,
    "cnt": 4,
}
USER_SID = "USbxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "3cdxxxxxxxxxxxxxxxxxxxxxxxxx"
END_POINT = "https://api.openweathermap.org/data/2.5/forecast?"
response = requests.get(
    url=END_POINT,
    params=PAR
)
data = response.json()

client = Client(USER_SID, AUTH_TOKEN)

for hour_data in data["list"]:
    idd = hour_data["weather"][0]["id"]
    if idd < 700:
        message = client.messages \
            .create(
                body="bring your umbrella, it will rain",
                from_="twilio number",
                to="your verified number"
                )
