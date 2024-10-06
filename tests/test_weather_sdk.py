import os
import pytest
from unittest.mock import patch
from app.weather_sdk import OpenWeatherSDK  # Altere para o caminho correto

class MockResponse:
    @staticmethod
    def json():
        return {
            'weather': [{'description': 'clear sky'}],
            'main': {'temp': 25.5}
        }

    @property
    def status_code(self):
        return 200

def test_get_weather():
    city = "Sao Paulo"
    
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse()
        
        sdk = OpenWeatherSDK()
        weather_data = sdk.get_weather(city)
        
        assert mock_get.called  # Verifica se o requests.get foi chamado
        assert 'weather' in weather_data  # Verifica se 'weather' está na resposta
        assert weather_data['main']['temp'] == 25.5  # Verifica se a temperatura está correta

def test_get_forecast():
    city = "Sao Paulo"
    
    class MockForecastResponse:
        @staticmethod
        def json():
            return {
                'list': [{'main': {'temp': 26.0}, 'weather': [{'description': 'partly cloudy'}]}]
            }

        @property
        def status_code(self):
            return 200
    
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockForecastResponse()
        
        sdk = OpenWeatherSDK()
        forecast_data = sdk.get_forecast(city)
        
        assert mock_get.called  # Verifica se o requests.get foi chamado
        assert 'list' in forecast_data  # Verifica se 'list' está na resposta
        assert forecast_data['list'][0]['main']['temp'] == 26.0  # Verifica se a temperatura da previsão está correta
