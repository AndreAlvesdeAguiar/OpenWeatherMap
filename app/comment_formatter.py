from datetime import datetime, timedelta

class CommentFormatter:
    # Dicionário de tradução
    weather_descriptions = {
        "clear sky": "céu limpo",
        "few clouds": "poucas nuvens",
        "scattered clouds": "nuvens dispersas",
        "broken clouds": "parcialmente nublado",
        "overcast clouds": "nublado",
    }

    def format_comment(self, weather, forecast, cidade):
        # Inicializa o dicionário para armazenar as temperaturas
        daily_temperatures = {}

        # Coletar a temperatura atual com precisão de duas casas decimais
        current_temp = float(weather['main']['temp'])  # Armazena como float para manter precisão
        
        # Obter a descrição em inglês e traduzir
        description = weather['weather'][0]['description']
        translated_description = self.weather_descriptions.get(description, description)  # Tradução

        # Obter a data e hora atuais
        now_local = datetime.now()
        today = now_local.date()  # Captura a data atual

        # Inicializa a previsão dos próximos dias
        forecast_str = []

        # Coletar a previsão para os próximos 5 dias, incluindo o dia atual
        for entry in forecast['list']:
            dt = datetime.fromtimestamp(entry['dt']) - timedelta(hours=3)  # Ajuste para UTC-3
            day = dt.date()

            # Armazenar a temperatura em um dicionário
            if day not in daily_temperatures:
                daily_temperatures[day] = []
            daily_temperatures[day].append(float(entry['main']['temp']))  # Armazenar como float para precisão

        # Calcular a média das temperaturas diárias
        forecast_days = sorted(daily_temperatures.keys())  # Ordenar os dias

        for day in forecast_days:
            avg_temp = round(sum(daily_temperatures[day]) / len(daily_temperatures[day]), 2)  # Média com 2 casas decimais

            # Exibir a previsão dos próximos dias (sem o dia atual)
            if day != today and len(forecast_str) < 5:
                forecast_str.append(f"{int(avg_temp)}°C em {day.strftime('%d/%m')}")

        # Arredondar a temperatura atual para o comentário final
        current_temp_rounded = int(round(current_temp))

        # Criar o comentário
        comment = (f"{current_temp_rounded}°C e {translated_description} em {cidade} em {today.strftime('%d/%m')}. "
                   f"Média para os próximos dias: " + ", ".join(forecast_str) + ".")
        
        return comment
