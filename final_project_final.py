# Name: Jackie Gullette
# Class: Intro to Programming
# Date: 03/05/2023


# import json and requests libraries:
import json, requests

def main():

    """Main function to accept input and return weather data"""
    
    # store webservice url and API key as strings to combine into URL:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    apikey = "134a631032499d98cc8d99fcfdcacbf7"

    # while loop for multiple inputs
    z = True
    while z == True:
        city= input("\nInput city, zip, or press 'q' to quit: ")

        if city == 'q':
            quit()
        else:
            # try-except block, KeyError exception
            try: 
                # nested try-else block for invalid connection
                try:    
                    url = f"{base_url}?q={city}&units=imperial&APPID={apikey}"
                    
                    # requests library to retrieve information from web service using URL:         
                    response = requests.get(url)
                    json_data = response.json()

                # connection unsuccessful                        
                except requests.exceptions.RequestException as err:
                    print('Connection to webservice unsuccessful.')
                    break
                
                # connection successful
                print("\nSuccessful response from OpenWeather: ")
                
                # temp variable stores temp data from 'main', prints city/zip and current temp:
                temp = json_data['main']['temp']
                print(f"\nThe current temperature in {city.title()} is: {temp}")

                # max_temp variable stores maximum temperature from 'main', prints info:
                max_temp = json_data['main']['temp_max']
                print(f"The max temperature today in {city.title()} is: {max_temp}")
                 
            # Invalid city or zip:
            except KeyError:
                print("Thats not a valid city or zip!")
          

# call function main()

main()

# fa72611e-69fc-4390-80c9-e72fcbd2bb09