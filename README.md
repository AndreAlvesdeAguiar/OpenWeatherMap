# Monitoramento do Tempo com OpenWeatherMap e GitHub Gist

Este projeto é uma solução para o aplicação integrada com o OpenWeatherMap e o Github para que seja
possível enviar um comentário em um Gist com a temperatura atual e a previsão dotempo dos próximos cinco dias (média diária) de uma cidade. 

Ele integra a API/SDK do OpenWeatherMap e a API do GitHub Gist para obter previsões meteorológicas e postar essas informações como comentários em um Gist.

## Estrutura do Projeto

```
/OpenWeatherMap
│
├── app
│   ├── __init__.py
│   ├── comment_formatter.py
│   ├── gist_service.py
│   └── weather_sdk.py
│
├── tests
│   ├── __init__.py
│   ├── test_comment_formatter.py
│   ├── test_weather_sdk.py
│   ├── test_gist_service.py
│   └── test_main.py
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

## Exemplo de uso

```
Exemplo de requisição:
GET /comentario/São Paulo
```

## Configuração

### Pré-requisitos
Antes de iniciar, você precisa ter o seguinte instalado em sua máquina:
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados na sua máquina.
- Chaves de API para o OpenWeatherMap e GitHub.

### Instalação
Clone o repositório:
```
git clone https://github.com/AndreAlvesdeAguiar/OpenWeatherMap.git
cd OpenWeatherMap
```

## Obtenção das Chaves de API

Para utilizar as APIs, você precisará de chaves de API que podem ser obtidas da seguinte forma:

    OpenWeatherMap[OWM_API_KEY]:
        Crie uma conta no OpenWeatherMap.
        Após a verificação do e-mail, faça login e acesse a seção "API Keys" no painel.
        Clique em "Create" para gerar uma nova chave de API e copie essa chave.

    GitHub[GITHUB_API_KEY]:
        Acesse GitHub e faça login.
        Vá para as configurações da sua conta e selecione "Developer settings".
        Clique em "Personal access tokens" e, em seguida, em "Tokens (classic)".
        Clique em "Generate new token", selecione os escopos necessários (como gist) e crie o token. Certifique-se de copiá-lo imediatamente.

    Gist[GIST_TOKEN]:
        Acesse a página de Gists no GitHub.
        Clique em "New gist" para criar um novo Gist.
        Preencha o título e a descrição do seu Gist e adicione o conteúdo desejado.
        Após criar o Gist, copie o URL do Gist gerado (ele terá um formato como https://gist.github.com/usuario/id_do_repositorio).

### Configure suas variáveis de ambiente. 

Crie um arquivo ```.env``` na raiz do projeto com suas chaves de API:

```
OWM_API_KEY=sua_chave_api_openweathermap
GITHUB_API_KEY=sua_chave_api_github
GIST_TOKEN=id_do_repositório gist
```

### Executando o Docker
Para subir a aplicação em um container Docker, execute o seguinte comando:
```
sudo docker-compose up --build
```

### Executando Testes no Docker
Verifique os containers em execução:
```
sudo docker ps
```

Entre no container usando o seguinte comando (substitua teste_caiena-app-1 pelo nome do seu container, se necessário):
```
sudo docker exec -it {NOME DO CONTAINER} /bin/bash
```
Navegue até a pasta de testes e Execute os testes:
```
cd /app/tests
pytest test_comment_formatter.py
pytest test_weather_sdk.py
pytest test_gist_service.py
pytest test_gist_service.py
pytest test_main.py
```
Executar todos os testes:
```
pytest
```

### Ngrok (Opcional)
O Ngrok é uma ferramenta que permite expor seu servidor local a um endereço público, facilitando o teste de webhooks ou o compartilhamento de sua aplicação em desenvolvimento com outras pessoas.

Para integrar o Ngrok à sua aplicação, descomente a seção correspondente no arquivo docker-compose.yml e adicione seu TOKEN_NGROK. É recomendável usar um arquivo ```.env``` para gerenciar suas variáveis de ambiente, assim como nas instruções anteriores.

```
  # ngrok:
  #   image: wernight/ngrok
  #   environment:
  #     - NGROK_PORT=app:8000  # Faz o ngrok se conectar ao serviço app na porta 8000
  #     - NGROK_AUTH={TOKEN_NGROK}  # Substitua pelo seu token de autenticação do ngrok
  #   ports:
  #     - "4040:4040"  # Porta para acessar o dashboard do ngrok
  #   depends_on:
  #     - app  # Certifique-se de que o app suba antes do ngrok
```
https://ngrok.com/docs/using-ngrok-with/docker/

### Formatação exemplo

```
34°C e nublado em <cidade> em 12/12. Média para os próximos dias: 32°C em 13/12, 25°C em 14/12, 29°C em 15/12, 33°C em 16/12 e 28°C em 16/12.
```
- Data - "DD/MM"
- Temperatura - Numeros inteiros
- Tradução nuvens - Inglês x Português 

### Descrições do Clima

| Descrição em Inglês       | Descrição em Português     |
|---------------------------|----------------------------|
| Clear sky                 | Céu limpo                  |
| Few clouds                | Poucas nuvens              |
| Scattered clouds          | Nuvens dispersas           |
| Broken clouds             | Parcialmente nublado       |
| Overcast clouds           | Nublado                    |

https://openweathermap.org/weather-conditions

