import os
from dotenv import load_dotenv
import requests

# Carregar variáveis do .env
load_dotenv()

class OpenWeatherSDK:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/"

    def get_weather(self, city):
        url = f"{self.base_url}weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro ao obter dados do clima: {response.status_code}")

    def get_forecast(self, city):
        url = f"{self.base_url}forecast?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erro ao obter previsão do clima: {response.status_code}")
