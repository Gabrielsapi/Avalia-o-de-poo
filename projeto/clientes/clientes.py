class Cliente:
    def __init__(self, nome: str, cpf: str):
        if not nome or not cpf:
            raise ValueError("Nome e CPF são obrigatórios.")

        self._nome = nome.strip()
        self._cpf = cpf.strip()

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf