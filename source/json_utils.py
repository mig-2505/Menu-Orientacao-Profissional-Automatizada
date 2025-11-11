import json
import os

class Manager:

    @staticmethod
    def _solve_path(file_path):
        """Converte caminho relativo em absoluto, baseado na raiz do projeto (fora de /source)."""
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_dir, file_path)

    @staticmethod
    def read_json(file_path):
        """Lê um arquivo JSON e retorna o conteúdo (ou lista/dict vazio se não existir)."""
        full_path = Manager._solve_path(file_path)
        if not os.path.exists(full_path):
            return []
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def save_json(file_path, data):
        """Salva dados (lista ou dicionário) em um arquivo JSON formatado."""
        full_path = Manager._solve_path(file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
