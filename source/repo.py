import json

class Repo:

    @staticmethod
    def get_suggestions():
        """ Leitura das sugestões """
        with open('../data/suggestions.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    @staticmethod
    def print_suggestions():
        """ Imprimir as sugestões """
        dt = Repo.get_suggestions()
        result = ""
        for key, value in dt.items():
            result += f"Para {key} a melhor sugestão é: {value}\n"
        return result
