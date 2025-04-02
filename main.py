from bs4 import BeautifulSoup
from flask import Flask ,render_template
import requests

# url for scrapped data from weather website
url = "https://www.timeanddate.com/weather/pakistan/peshawar/ext"
respone = requests.get(url=url)
data = respone.text
# now get specfic data which i want
soup = BeautifulSoup(data, "html.parser")
# scrapped 7 days
days = soup.find_all("span", class_="smaller soft")
# seven days temperature
temperature = soup.find_all("td")
temperature_list = [tem.get_text() for tem in temperature]
weather_list = [tem.get_text() for tem in temperature]


temperature_list=[temperature_list[i] for i in range(1, 74, 12)]
print(temperature_list)

weather_list=[weather_list[i] for i in range(2,75,12)]
print(weather_list)
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html" ,days=days, temperature_list=temperature_list, weather_list=weather_list)

print(f"  days = {temperature_list[1]}")

if __name__=="__main__":
  app.run(debug=True)
