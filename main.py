from fastapi import FastAPI, HTTPException
from app.weather_sdk import OpenWeatherSDK
from app.gist_service import add_comment_to_gist
from datetime import datetime

app = FastAPI()
weather_sdk = OpenWeatherSDK()

# Dicionário de tradução
weather_descriptions = {
    "few clouds": "poucas nuvens",
    "scattered clouds": "nuvens dispersas",
    "broken clouds": "parcialmente nublado",
    "overcast clouds": "nublado",
}

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
    # Temperatura atual
    current_temp = int(weather['main']['temp'])  # Converte para inteiro
    
    # Obter a descrição em inglês e traduzir
    description = weather['weather'][0]['description']
    translated_description = weather_descriptions.get(description, description)  # Tradução

    # Formatar a data de hoje
    today = datetime.now().strftime('%d/%m')

    # Inicializa a previsão dos próximos dias
    forecast_str = []
    daily_temperatures = {}

    # Coletar a previsão para os próximos 6 dias (incluindo hoje)
    for entry in forecast['list']:
        dt = datetime.fromtimestamp(entry['dt'])
        day = dt.date()
        
        # Armazenar a temperatura em um dicionário
        if day not in daily_temperatures:
            daily_temperatures[day] = []
        daily_temperatures[day].append(int(entry['main']['temp']))  # Converte para inteiro

    # Calcular a média das temperaturas diárias e formatar a string
    for day in sorted(daily_temperatures.keys()):
        avg_temp = sum(daily_temperatures[day]) / len(daily_temperatures[day])
        if len(forecast_str) < 5 and day != datetime.now().date():  # Ignorar o dia atual para a média
            forecast_str.append(f"{int(avg_temp)}°C em {day.strftime('%d/%m')}")  # Converte para inteiro

    # Criar o comentário
    comment = (f"{current_temp}°C e {translated_description} em {cidade} em {today}. "
               f"Média para os próximos dias: " + ", ".join(forecast_str) + ".")
    
    return comment
