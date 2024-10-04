# Integração OpenWeatherMap & GitHub Gist

Este projeto é uma solução para o aplicação integrada com o OpenWeatherMap e o Github para que seja
possível enviar um comentário em um Gist com a temperatura atual e a previsão dotempo dos próximos cinco dias (média diária) de uma cidade. 

Ele integra a API/SDK do OpenWeatherMap e a API do GitHub Gist para obter previsões meteorológicas e postar essas informações como comentários em um Gist.

## 2. Estrutura do Projeto

```
/OpenWeatherMap
│
├── app
│   ├── __init__.py
│   ├── __pycache__/
│   ├── gist_service.py
│   └── weather_sdk.py
│
├── .env
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

## Funcionalidades

- **Previsão do Tempo**: Busca as condições climáticas atuais e a previsão de 5 dias usando a API do OpenWeatherMap.
- **Integração com o GitHub Gist**: Publica um comentário com as informações meteorológicas em um Gist utilizando a API do GitHub.
- **Aplicação Dockerizada**: Roda dentro de um container Docker com suporte ao Docker Compose.

## Configuração

### Pré-requisitos

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados na sua máquina.
- Chaves de API para o OpenWeatherMap e GitHub.

##explicar mais sobre a obtenção dos tokens.

### Configure suas variáveis de ambiente. 

Crie um arquivo ```.env``` com suas chaves de API:

```
OWM_API_KEY=sua_chave_api_openweathermap
GITHUB_API_KEY=sua_chave_api_github
```

### Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/AndreAlvesdeAguiar/OpenWeatherMap.git
   cd OpenWeatherMap
   ```
