from typing import Dict


class Banco:
    def __init__(self):
        self._contas: Dict[int, object] = {}

    def adicionar_conta(self, conta) -> None:
        self._contas[conta.id] = conta

    def buscar_conta(self, conta_id: int):
        return self._contas.get(conta_id)

    def listar_contas(self):
        return list(self._contas.values())