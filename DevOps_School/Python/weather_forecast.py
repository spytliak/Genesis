#!/usr/bin/env python3

import sys, os
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

def get_weather(city, APIID):
    try:
        # needed for installing different languages for query results, default is eng
        config_dict = get_default_config()
        config_dict['language'] = 'eng'
        
        owm = OWM(APIID, config_dict)
        mgr = owm.weather_manager()
        
        observation = mgr.weather_at_place(city)
        w = observation.weather
        
        temperature = w.temperature('celsius')['temp']
        wind = w.wind()['speed']
        humidity = w.humidity

        print(
            'The weather in the {} is: \n'.format(city.upper()) +
            'temperature: {} °C \n'.format(temperature) +
            'wind: {} m/s \n'.format(wind) +
            'humidity: {} % \n'.format(humidity)
        )

    except Exception as e:
        print("Error: " + str(e))

def main():
    APIID = os.environ.get('APIID')
    # check APIID env
    if "APIID" in os.environ: 
        pass
    else:
        exit('Environment variable APIID (API key) does not exist. Please export APIID in your env')

    # check city
    if len(sys.argv) > 1:
       city = sys.argv[1]
    else: 
        city = input("Please enter a city: ")
    
    get_weather(city, APIID)


if __name__ == '__main__':
    main()
