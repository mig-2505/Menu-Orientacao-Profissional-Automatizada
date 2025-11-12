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
        count = 0
        limit = 3
        for skill, data in dt.items():
            if count >= limit:
                break
            current = data.get("current", "Não especificado")
            future = data.get("future", "Não especificado")
            result += (
            f"\nHabilidade: {skill}\n"
            f"  Profissão Atual: {current}\n"
            f"  Profissão do Futuro: {future}\n"
        )
            count += 1
        return result
