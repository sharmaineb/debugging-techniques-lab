import os
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file


################################################
## SETUP
################################################

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')


################################################
## ROUTES
################################################

@app.route('/')
def home():
    """Displays the homepage with forms for current or historical data."""
    context = {
        'min_date': (datetime.now() - timedelta(days=5)),
        'max_date': datetime.now()
    }
    return render_template('home.html', **context)

def get_letter_for_units(units):
    """Returns a shorthand letter for the given units."""
    return 'F' if units == 'imperial' else 'C' if units == 'metric' else 'K'

@app.route('/results')
def results():
    """Displays results for current weather conditions."""
    city = request.args.get('users_city')
    units = request.args.get('requested_units')

    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid': API_KEY,
        'q': city,
        'units': units
    }

    print(f"API Request Params: {params}")

    response = requests.get(url, params=params)

    if not response.ok:
        print(f"Error in API request. Status Code: {response.status_code}")
        return render_template('results.html', city='City Name Not Available')

    try:
        result_json = response.json()
    except Exception as e:
        print(f"Error parsing JSON response: {e}")
        print(f"Response content: {response.content}")
        return render_template('results.html', city='City Name Not Available')

    print(result_json)  
    
    context = {
        'date': datetime.now(),
        'city': result_json.get('name', 'City Name Not Available'),
        'description': result_json.get('weather', [{'description': 'Weather Data Not Available'}])[0]['description'],
        'temp': result_json.get('main', {}).get('temp', 'Temperature Data Not Available'),
        'humidity': result_json.get('main', {}).get('humidity', 'Humidity Data Not Available'),
        'wind_speed': result_json.get('wind', {}).get('speed', 'Wind Speed Data Not Available'),
        'units_letter': get_letter_for_units(units)
    }

    return render_template('results.html', **context)


if __name__ == '__main__':
    app.run()