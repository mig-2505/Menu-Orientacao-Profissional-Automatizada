from datetime import date

class Model:

    @staticmethod
    def model_user(name, profession, skills):
        """Cria um dicionário representando um usuário"""
        return  {
            "Name": name,
            "Profession": profession,
            "Skills": skills,
            "Stage": "novo",
            "CreatedAt": date.today().isoformat()
        }