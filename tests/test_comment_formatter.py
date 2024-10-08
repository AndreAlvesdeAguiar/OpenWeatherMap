from datetime import datetime, timedelta

class CommentFormatter:
    # Dicionário de tradução
    weather_descriptions = {
        "few clouds": "poucas nuvens",
        "scattered clouds": "nuvens dispersas",
        "broken clouds": "parcialmente nublado",
        "overcast clouds": "nublado",
    }

    def format_comment(self, weather, forecast, cidade):
        # Temperatura atual
        current_temp = int(weather['main']['temp'])  # Converte para inteiro
        
        # Obter a descrição em inglês e traduzir
        description = weather['weather'][0]['description']
        translated_description = self.weather_descriptions.get(description, description)  # Tradução

        # Formatar a data de hoje considerando UTC-3
        now_utc = datetime.utcnow()  # Obtém a hora atual em UTC
        now_local = now_utc - timedelta(hours=3)  # Converte para o horário de São Paulo
        today = now_local.strftime('%d/%m')

        # Inicializa a previsão dos próximos dias
        forecast_str = []
        daily_temperatures = {}

        # Coletar a previsão para o dia atual mais 5 dias
        for entry in forecast['list']:
            dt = datetime.fromtimestamp(entry['dt'])  # Conversão do timestamp para UTC
            dt_local = dt - timedelta(hours=3)  # Ajuste para o fuso horário de São Paulo
            day = dt_local.date()

            # Armazenar a temperatura em um dicionário
            if day not in daily_temperatures:
                daily_temperatures[day] = []
            daily_temperatures[day].append(int(entry['main']['temp']))  # Converte para inteiro

        # Calcular a média das temperaturas diárias e formatar a string
        forecast_days = sorted(daily_temperatures.keys())

        for day in forecast_days[:6]:  # Pega o dia atual e os próximos 5 dias
            avg_temp = sum(daily_temperatures[day]) / len(daily_temperatures[day])
            forecast_str.append(f"{int(avg_temp)}°C em {day.strftime('%d/%m')}")

        # Criar o comentário
        comment = (f"{current_temp}°C e {translated_description} em {cidade} em {today}. "
                   f"Média para os próximos dias: " + ", ".join(forecast_str) + ".")
        
        return comment
