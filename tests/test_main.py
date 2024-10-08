class MockWeatherSDK:
    def get_weather(self, cidade):
        return {
            "main": {"temp": 25.0},  # Ajuste a temperatura aqui para 25.0°C como esperado no teste
            "weather": [{"description": "overcast clouds"}]
        }
    
    def get_forecast(self, cidade):
        return {
            "list": [
                {"dt": 1696531200, "main": {"temp": 25.0}},  # Hoje
                {"dt": 1696617600, "main": {"temp": 20.8}},  # Dia 1
                {"dt": 1696704000, "main": {"temp": 19.9}},  # Dia 2
                {"dt": 1696790400, "main": {"temp": 23.5}},  # Dia 3
                {"dt": 1696876800, "main": {"temp": 19.4}},  # Dia 4
                {"dt": 1696963200, "main": {"temp": 17.8}},  # Dia 5
                {"dt": 1697049600, "main": {"temp": 17.1}},  # Dia 6
            ]
        }
