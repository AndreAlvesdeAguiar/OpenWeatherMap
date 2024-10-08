import os
from github import Github
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

class GistService:
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.g = Github(self.github_token)

    def add_comment_to_gist(self, gist_id, comment):
        gist = self.g.get_gist(gist_id)
        gist.create_comment(comment)
        return comment