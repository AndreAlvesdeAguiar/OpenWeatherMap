from fastapi import FastAPI, HTTPException
from app.weather_sdk import OpenWeatherSDK
from app.gist_service import GistService
from app.comment_formatter import CommentFormatter

app = FastAPI()

# Instanciar os serviços
weather_sdk = OpenWeatherSDK()
gist_service = GistService()
comment_formatter = CommentFormatter()

@app.get("/comentario/{cidade}")
def comentario(cidade: str):
    try:
        weather = weather_sdk.get_weather(cidade)
        forecast = weather_sdk.get_forecast(cidade)
        comment = comment_formatter.format_comment(weather, forecast, cidade)

        # Enviar o comentário ao Gist
        gist_id = "3278511ba592a171093015bb84810ddc"  # Seu ID do Gist
        gist_service.add_comment_to_gist(gist_id, comment)

        return {
            "message": f"Comentário sobre o clima em {cidade} postado com sucesso!",
            "comment": comment
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
