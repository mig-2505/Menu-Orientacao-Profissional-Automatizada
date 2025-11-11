from models.model import Model
from source.repo import Repo
from source.json_utils import Manager

class Profiles:

    def __init__(self, file_json='data/users.json'):
        self.file_json = file_json
        self.users = Manager.read_json(self.file_json)
        self.suggestions = Repo.get_suggestions()

    def add_user(self, name, profession, skills):
        """Adiciona um usuário à lista"""
        user = Model.model_user(name, profession, skills)
        self.users.append(user)
        Manager.save_json(self.file_json, self.users)
        print("Usuario adicionado!")

    def view_users(self):
        """Lista todos os usuários cadastrados"""
        if not self.users:
            print("Nenhum usuario cadastrado ainda")
        else:
            print("\n=== Usuários cadastrados ===")
            for i in self.users:
                print(f"Nome: {i['Name']}")
                print(f"Profissão: {i['Profession']}")
                print(f"Habilidades: {i['Skills']}")
                print(f"Estágio: {i['Stage']}")
                print(f"Criado em: {i['CreatedAt']}")
                print()

    @staticmethod
    def print_menu():
        """ Exibir menu """
        print("\n=== Menu Orientacao Profissional Automatizada ===")
        print("[1] Adicionar - Usuario")
        print("[2] Listar Usuarios") 
        print("[3] Gerar Recomendação")
        print("[0] Sair")