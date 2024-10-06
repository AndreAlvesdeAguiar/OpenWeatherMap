from fastapi import FastAPI, HTTPException
from app.weather_sdk import OpenWeatherSDK
from app.gist_service import add_comment_to_gist
from datetime import datetime

app = FastAPI()
weather_sdk = OpenWeatherSDK()

@app.get("/comentario/{cidade}")
def comentario(cidade: str):
    try:
        weather = weather_sdk.get_weather(cidade)
        forecast = weather_sdk.get_forecast(cidade)
        comment = format_comment(weather, forecast, cidade)
        gist_id = "3278511ba592a171093015bb84810ddc"  # Seu ID do Gist
        add_comment_to_gist(gist_id, comment)

        return {
            "message": f"Comentário sobre o clima em {cidade} postado com sucesso!",
            "comment": comment
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def format_comment(weather, forecast, cidade):
    current_temp = weather['main']['temp']
    description = weather['weather'][0]['description']
    today = datetime.now().strftime('%d/%m')
    forecast_str = []
    daily_temperatures = {}

    for entry in forecast['list']:
        dt = datetime.fromtimestamp(entry['dt'])
        day = dt.date()
        if day not in daily_temperatures:
            daily_temperatures[day] = []
        daily_temperatures[day].append(entry['main']['temp'])

    for day in sorted(daily_temperatures.keys()):
        avg_temp = sum(daily_temperatures[day]) / len(daily_temperatures[day])
        if len(forecast_str) < 6:
            forecast_str.append(f"{avg_temp:.1f}°C em {day.strftime('%d/%m')}")

    comment = (f"{current_temp:.1f}°C e {description} em {cidade} no dia {today}. "
               f"Média para os próximos dias: " + ", ".join(forecast_str) + ".")
    
    return comment

# Mocks para teste
class MockWeatherSDK:
    def get_weather(self, cidade):
        return {
            "main": {"temp": 25.0},  # Ajuste a temperatura aqui para a que é gerada no teste
            "weather": [{"description": "overcast clouds"}]
        }
    
    def get_forecast(self, cidade):
        return {
            "list": [
                {"dt": 1696531200, "main": {"temp": 16.9}},  # Hoje
                {"dt": 1696617600, "main": {"temp": 20.8}},  # Dia 1
                {"dt": 1696704000, "main": {"temp": 19.9}},  # Dia 2
                {"dt": 1696790400, "main": {"temp": 23.5}},  # Dia 3
                {"dt": 1696876800, "main": {"temp": 19.4}},  # Dia 4
                {"dt": 1696963200, "main": {"temp": 17.8}},  # Dia 5
                {"dt": 1697049600, "main": {"temp": 17.1}},  # Dia 6
            ]
        }

class MockGistService:
    @staticmethod
    def add_comment_to_gist(gist_id, comment):
        return "Comentário adicionado com sucesso"

def test_comentario():
    # Substitua as dependências por mocks
    global weather_sdk, add_comment_to_gist
    weather_sdk = MockWeatherSDK()
    add_comment_to_gist = MockGistService.add_comment_to_gist
    
    # Chama a função e verifica o retorno
    try:
        response = comentario("São Paulo")
        assert response["message"] == "Comentário sobre o clima em São Paulo postado com sucesso!"
        assert "25.0°C" in response["comment"]  # Verifique a temperatura correta
    except HTTPException as e:
        assert False, f"Erro inesperado: {e.detail}"
