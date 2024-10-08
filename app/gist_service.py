# gist_service.py

import os
from github import Github
from dotenv import load_dotenv
from app.weather_sdk import OpenWeatherSDK
from app.comment_formatter import CommentFormatter

# Carregar variáveis do .env
load_dotenv()

class GistService:
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.g = Github(self.github_token)
        self.weather_sdk = OpenWeatherSDK()
        self.comment_formatter = CommentFormatter()

    def post_weather_comment(self, cidade):
        # Obter o clima e a previsão
        weather = self.weather_sdk.get_weather(cidade)
        forecast = self.weather_sdk.get_forecast(cidade)

        # Formatar o comentário
        comment = self.comment_formatter.format_comment(weather, forecast, cidade)

        # Enviar o comentário ao Gist
        gist_id = "3278511ba592a171093015bb84810ddc"  # Seu ID do Gist
        gist = self.g.get_gist(gist_id)
        gist.create_comment(comment)
        
        return comment
