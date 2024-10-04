import os
from github import Github
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

def add_comment_to_gist(gist_id, comment):
    github_token = os.getenv("GITHUB_TOKEN")  # Agora usando a variável de ambiente
    g = Github(github_token)
    gist = g.get_gist(gist_id)
    gist.create_comment(comment)
