# test_gist_service.py

import os
import pytest
from app.gist_service import GistService

class MockGithub:
    def __init__(self, token):
        self.token = token
    
    def get_gist(self, gist_id):
        return MockGist()

class MockGist:
    def create_comment(self, comment):
        return comment

class MockWeatherSDK:
    def get_weather(self, city):
        return {"main": {"temp": 25}, "description": "Clear sky"}  # Inclui a chave 'main'
    
    def get_forecast(self, city):
        return [{"day": "2023-10-01", "temp": 22}, {"day": "2023-10-02", "temp": 24}]

def test_post_weather_comment(monkeypatch):
    # Mock do método os.getenv para retornar um token fake
    monkeypatch.setattr(os, 'getenv', lambda x: 'fake_token' if x == "GITHUB_TOKEN" else None)

    # Mock do Github
    monkeypatch.setattr('app.gist_service.Github', MockGithub)

    # Mock do OpenWeatherSDK
    mock_weather = {
        'weather': [{'description': 'Clear sky'}],
        'main': {'temp': 25}
    }
    mock_forecast = {
        'list': [
            {'dt': 1633046400, 'main': {'temp': 22}},  # Exemplo de timestamp
            {'dt': 1633132800, 'main': {'temp': 24}}   # Exemplo de timestamp
        ]
    }
    monkeypatch.setattr('app.gist_service.OpenWeatherSDK.get_weather', lambda self, city: mock_weather)
    monkeypatch.setattr('app.gist_service.OpenWeatherSDK.get_forecast', lambda self, city: mock_forecast)

    # Instanciar o serviço
    gist_service = GistService()

    # Chamar a função que estamos testando
    result = gist_service.post_weather_comment('São Paulo')
    assert result is not None
