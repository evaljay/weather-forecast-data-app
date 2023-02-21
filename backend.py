import requests

API_KEY = "33c9e456aa70f1efe4d6af577feab3e2"

 
def get_data(place, forecast_days, kind):

    url = f"https://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    if kind == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data ]
    elif kind == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))


