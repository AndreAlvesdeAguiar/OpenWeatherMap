import pytest
from datetime import datetime, timedelta
from app.comment_formatter import CommentFormatter

@pytest.fixture
def formatter():
    return CommentFormatter()

def test_format_comment(formatter):
    # Exemplo de dados simulados
    weather = {
        'main': {'temp': 17},
        'weather': [{'description': 'broken clouds'}]
    }
    forecast = {
        'list': [
            {'dt': (datetime.utcnow() + timedelta(days=1)).timestamp(), 'main': {'temp': 18}},  # 1 dia depois de hoje
            {'dt': (datetime.utcnow() + timedelta(days=2)).timestamp(), 'main': {'temp': 19}},  # 2 dias depois de hoje
            {'dt': (datetime.utcnow() + timedelta(days=3)).timestamp(), 'main': {'temp': 21}},  # 3 dias depois de hoje
            {'dt': (datetime.utcnow() + timedelta(days=4)).timestamp(), 'main': {'temp': 22}},  # 4 dias depois de hoje
            {'dt': (datetime.utcnow() + timedelta(days=5)).timestamp(), 'main': {'temp': 20}},  # 5 dias depois de hoje
        ]
    }
    cidade = "São Paulo"
    comment = formatter.format_comment(weather, forecast, cidade)

    # Data de hoje no formato esperado (UTC-3)
    today = (datetime.utcnow() - timedelta(hours=3)).strftime('%d/%m')

    # Ajustar as datas previstas para o fuso UTC-3
    expected_comment = (f"17°C e parcialmente nublado em São Paulo em {today}. "
                        f"Média para os próximos dias: "
                        f"18°C em {(datetime.utcnow() - timedelta(hours=3) + timedelta(days=1)).strftime('%d/%m')}, "
                        f"19°C em {(datetime.utcnow() - timedelta(hours=3) + timedelta(days=2)).strftime('%d/%m')}, "
                        f"21°C em {(datetime.utcnow() - timedelta(hours=3) + timedelta(days=3)).strftime('%d/%m')}, "
                        f"22°C em {(datetime.utcnow() - timedelta(hours=3) + timedelta(days=4)).strftime('%d/%m')}, "
                        f"20°C em {(datetime.utcnow() - timedelta(hours=3) + timedelta(days=5)).strftime('%d/%m')}.")
    
    assert comment == expected_comment
