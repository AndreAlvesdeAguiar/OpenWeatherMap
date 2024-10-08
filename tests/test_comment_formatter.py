import pytest
from datetime import datetime, timedelta
from app.comment_formatter import CommentFormatter  # Ajuste o import conforme a localização da sua classe
from app.gist_service import GistService  # Ajuste o caminho conforme necessário

@pytest.fixture
def comment_formatter():
    return CommentFormatter()

def test_format_comment(comment_formatter):
    weather = {
        'main': {'temp': 25},
        'weather': [{'description': 'clear sky'}]
    }
    
    forecast = {
        'list': [
            {'dt': (datetime.utcnow() + timedelta(days=1)).timestamp(), 'main': {'temp': 27}},
            {'dt': (datetime.utcnow() + timedelta(days=2)).timestamp(), 'main': {'temp': 28}},
            {'dt': (datetime.utcnow() + timedelta(days=3)).timestamp(), 'main': {'temp': 26}},
            {'dt': (datetime.utcnow() + timedelta(days=4)).timestamp(), 'main': {'temp': 24}},
            {'dt': (datetime.utcnow() + timedelta(days=5)).timestamp(), 'main': {'temp': 23}},
        ]
    }
    
    cidade = "São Paulo"
    
    comment = comment_formatter.format_comment(weather, forecast, cidade)
    
    assert "25°C e céu limpo" in comment
    assert "Média para os próximos dias:" in comment
    assert "27°C em" in comment  # Verifica se a média de 27°C do dia seguinte está presente
    assert "28°C em" in comment  # Verifica se a média de 28°C do dia após o dia seguinte está presente
    assert "26°C em" in comment  # Verifica se a média de 26°C do terceiro dia está presente
    assert "24°C em" in comment  # Verifica se a média de 24°C do quarto dia está presente
    assert "23°C em" in comment  # Verifica se a média de 23°C do quinto dia está presente

if __name__ == "__main__":
    pytest.main()
