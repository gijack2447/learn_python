# Name: Jackie Gullette
# Class: Intro to Programming
# Date: 03/04/2023
# import json and requests libraries:
import json
import requests
# store webservice url and API key as strings to combine into URL:
base_url = "https://api.openweathermap.org/data/2.5/weather"
apikey = "134a631032499d98cc8d99fcfdcacbf7"

def main():
 
    """Main function to accept input and return weather data"""
    
    # while loop for multiple inputs
    
    while True:
        
        # Prompt user input:
        
        city = input("\nInput a city, zip code, or type 'q' to quit: ")
        
        # if-else statement to quit program with input 'q':
        
        if city == 'q':
        
            quit()
        
        else:
        
        # format url for get request using API key:
        
            url = f"{base_url}?q={city}&units=imperial&APPID={apikey}"
            
            # requests library to retrieve information from web service: 
            
            response = requests.get(url)
            
            # format data into json:
            
            json_data = response.json()
            
            # temp variable stores temp data from 'main', prints city/zip and current temp:
            
            temp = json_data['main']['temp']
            
            print(f"The current temperature in {city.title()} is: {temp})            } is: {temp}")
            
            # max_temp variable stores maximum temperature from 'main', prints info:
            
            max_temp = json_data['main']['temp_max']
                       
            print(f"The max temperature today in {city.title()} is: {max_temp}")

# call function main()
main()
# Add try-except block for invalid input
# print() statement prompting user to re-enter city/zip
# Add try-except block to validate connection to web service
# print() statement for successful connection to web service