import pendulum
import socket
from geopy.geocoders import Nominatim
from flask import Flask, redirect, render_template,url_for
app = Flask(__name__)
ist = pendulum.timezone('Asia/Calcutta')
time_ist=pendulum.now(ist)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
geolocator = Nominatim(user_agent="geoapiExercises")
Latitude = "18.5204"
Longitude = "73.8567"
location = geolocator.reverse(Latitude+","+Longitude)
address = location.raw['address']
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
@app.route("/")
@app.route("/pucsd")
def pucsd():
    return render_template("pucsd.html",val1=time_ist,val2=ip,val3=hostname,val4=city,val5=state,val6=country)
#print("Current Time in IST : " + time_ist)
#print("Your Computer Name is:" + hostname)
#print("Your Computer IP Address is:" + ip)
#print("City :" ,city)
#print("Region :",state)
#print("Country :",country)

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run(debug=True)
