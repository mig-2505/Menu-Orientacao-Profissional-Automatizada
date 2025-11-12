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

    def check_recommendation(self, name):
        """Verifica as habilidades do usuário procurado e recomenda áreas de atuação"""
        suggestions = Repo.get_suggestions()
        formatted_suggestions = Repo.print_suggestions()

        for user in self.users:
            if name.lower() in user['Name'].lower():
                skills_list = [s.strip().lower() for s in user['Skills'].split(',')]
                print(f"\nPara {user['Name']}:")
                found_any = False
                for skill in skills_list:
                    if skill in suggestions:
                        current = suggestions[skill]["current"]
                        future = suggestions[skill]["future"]
                        print(f"Habilidade: {skill}")
                        print(f"Profissão Atual: {current}")
                        print(f"Profissão do Futuro: {future}\n")
                        found_any = True
                    else:
                        print(f"Nenhuma recomendação encontrada para a habilidade '{skill}'.\n")
                if not found_any:
                    print("Algus exemplos de habilidades:")
                    print(formatted_suggestions)
                    print("...")
                break
        else:
            print(f"Nenhum usuário encontrado com o nome '{name}'.")
