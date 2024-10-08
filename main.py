# main.py

from fastapi import FastAPI, HTTPException
from app.gist_service import GistService

app = FastAPI()

# Instanciar o serviço
gist_service = GistService()

@app.get("/comentario/{cidade}")
def comentario(cidade: str):
    try:
        comment = gist_service.post_weather_comment(cidade)

        return {
            "message": f"Comentário sobre o clima em {cidade} postado com sucesso!",
            "comment": comment
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
