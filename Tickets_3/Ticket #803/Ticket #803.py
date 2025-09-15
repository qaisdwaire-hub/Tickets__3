from flask import Flask,request

app = Flask(__name__)

@app.route("/weather")
def weather():
 city = request.args.get("city", "").strip()

 if not city:
   return "Error: 'city' parameter is missing"

 if not city.replace(" ","").isalpha():
   return "Error: 'city' parameter is invalid"

 return f"Sunny in {city}"