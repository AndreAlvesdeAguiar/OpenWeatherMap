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
    
    # Formatar a data de hoje
    today = datetime.fromtimestamp(forecast['list'][0]['dt']).strftime('%d/%m')
    
    # Formatar previsão dos próximos dias
    forecast_str = []
    num_days = min(len(forecast['list']) // 8, 5)  # Calcula o número de dias disponíveis
    
    for i in range(1, num_days + 1):  # Pega a previsão para os próximos dias
        day_index = i * 8  # Cada 8 entradas representa um dia
        if day_index < len(forecast['list']):  # Verifica se o índice está dentro do limite
            day = forecast['list'][day_index]
            date = datetime.fromtimestamp(day['dt']).strftime('%d/%m')
            temp = day['main']['temp']
            forecast_str.append(f"{temp}°C em {date}")

    # Criar o comentário
    comment = (f"{current_temp}°C e {description} em {cidade} no dia {today}. "
               f"Média para os próximos dias: " + ", ".join(forecast_str) + ".")
    return comment
