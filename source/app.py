from profiles import Profiles
from source.recommendations import Recommendation

profile = Profiles()
recommendation = Recommendation(profile.users)

def main():
    while True:
        Profiles.print_menu()

        op = input("Digite uma opcão: ")

        if op == "1":
            name = input("Digite seu nome: ")
            profession = input("Digite sua profissão que quer: ")
            skills = input("Digite alguma habilidade sua: ").lower()
            profile.add_user(name, profession, skills)

        elif op == "2":
            profile.view_users()

        elif op == "3":
            name = input("Digite o nome que deseja procurar: ").lower()
            search_result = recommendation.search(name)

            if search_result:
                recommendation.recommendation(name)
                recommendation.check_recommendation(name)
            else:
                print("Nao foi possivel terminar.")

        elif op == "0":
            print("Saindo do programa...")
            break

        else:
            print("Digite uma opção válida")

if __name__ == "__main__":
    main()