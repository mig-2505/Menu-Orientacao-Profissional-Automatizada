from repo import Repo
from source.profiles import Profiles

class Recommendation(Profiles):

    def __init__(self, users):
        super().__init__()
        self.users = users

    def search(self, name):
        """ Busca o nome dentro da lista """
        for i in self.users:
            if name in i['Name'].lower():
                return i
        print("Nome nao cadastrado, tente novamente!")

    def recommendation(self, name):
        """ Mostra as habilidades do usuário procurado """
        for i in self.users:
            if name in i['Name'].lower():
                print(f"\nHabilidades de {i['Name']}: {i['Skills']}")
                return
        print("Usuario nao encontrado.")

    def check_recommendation(self, name):
        """ Verifica as habilidades do usuario procurado e recomenda áreas de atuação """
        suggestions = Repo.get_suggestions()
        formatted_suggestions = Repo.print_suggestions()
        for i in self.users:
            skills = i['Skills'].lower()
            if skills in suggestions:
                if name in i['Name'].lower():
                    print(f"\nPara {i['Name']}:")
                    print(f"Sua habilidade em '{skills}' combina com a área de {suggestions[skills]}.\n")
            else:
                print(f"\nPara {i['Name']}:")
                print(f"Nenhuma recomendação encontrada para a habilidade '{skills}'.")
                print(formatted_suggestions)