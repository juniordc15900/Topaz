import unittest
import requests
import json

 
def get_username(username: str) -> dict:

    resposta = requests.get(
            f'https://api.github.com/users/{username}')
    return resposta.json()

class User: 

    def __init__(self, username: str):
        self.username = username
        self.resposta = get_username(username)
        # Se o limite de requisições for excedido, o código retorna somente a chave 'message'
        try:
            self.id = self.resposta['id']
            self.login = self.resposta['login']
            self.name = self.resposta['name']
            self.repos = self.resposta['public_repos']
            self.followers = self.resposta['followers']
            self.following = self.resposta['following']
            self.avatar_url = self.resposta['avatar_url']
            self.html_url = self.resposta['html_url']
        except:
            self.message = self.resposta['message']
        
        
    

class TestMethods(unittest.TestCase):

    # Teste para verificar se a requisição foi aceita e o objeto é diferente de None
    def test_user_object(self):
        response = get_username('juniordc15900')
        self.assertNotEqual(response, None)
    

    def test_username_parameters(self):
        parameters = ['id','login','public_repos','followers','following','avatar_url', 'html_url']

        # Utilizando meu username do GitHub
        response = get_username('juniordc15900')
        for parameter in parameters:
            # Testa se todos os parâmetros contém no response
            self.assertIn(parameter, response)

        # Testa se o parâmetro 'id' é um inteiro
        self.assertEqual(type(response['id']), int)

        # Testa se meu nome bate com o nome do usuário
        expected_name = 'Alessandro Junior'
        self.assertEqual(response['name'], expected_name)
            

if __name__ == "__main__":
    
    user = User('githubuser')
    print('Algumas Informações do Usuário: \n ')
    try:
        if user.message:
            print('    Limite de requisições excedido')
            print(f'    Mensagem de erro: {user.message}')
            
    except:
        print(f'    Id: {user.id}')
        print(f'    Login: {user.login}')
        print(f'    Nome: {user.name}')
        print(f'    Url: {user.html_url}')
        unittest.main()
