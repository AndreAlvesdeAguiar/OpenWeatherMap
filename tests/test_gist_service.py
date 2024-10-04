import os
import pytest
from app.gist_service import add_comment_to_gist

# Mock da resposta do Gist
class MockGist:
    def create_comment(self, comment):
        return comment  # Simulando a criação do comentário

class MockGithub:
    def __init__(self, token):
        self.token = token

    def get_gist(self, gist_id):
        return MockGist()  # Retornando uma instância mock do Gist

# Teste da função add_comment_to_gist
def test_add_comment_to_gist(monkeypatch):
    # Mock do método os.getenv para retornar um token fake
    monkeypatch.setattr(os, 'getenv', lambda x: 'fake_token' if x == "GITHUB_TOKEN" else None)

    # Mock do Github
    monkeypatch.setattr('app.gist_service.Github', MockGithub)

    # Chamar a função que estamos testando
    result = add_comment_to_gist('fake_gist_id', 'This is a comment.')

    # Verifica se o comentário foi realmente "adicionado"
    assert result == 'This is a comment.'  # Verifica se o comentário retornado está correto
