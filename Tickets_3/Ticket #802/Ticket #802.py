from flask import Flask, request

app = Flask(__name__)

@app.route("/weather")
def weather():
 city = request.args.get("city")

 if not city :
     return "Error: 'city' parameter is missing"

 return f"Sunny in {city}"
