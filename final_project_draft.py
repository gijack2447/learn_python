import json, requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
apikey = "134a631032499d98cc8d99fcfdcacbf7"

def main():
    """Main function to accept input and return weather data"""
    while True:
        city = input("\nInput a city, zip code, or type 'q' to quit: ")

        if city == 'q':
            quit()
        else:
            url = f"{base_url}?q={city}&units=imperial&APPID={apikey}"         
            response = requests.get(url)
            json_data = response.json()

            temp = json_data['main']['temp']
            print(f"The current temperature in {city.title()} is: {temp}")

            max_temp = json_data['main']['temp_max']
            print(f"The max temperature today in {city.title()} is: {max_temp}")

main()
