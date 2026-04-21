from datetime import datetime
from typing import List


class Historico:
    def __init__(self):
        self._operacoes: List[str] = []

    def registrar(self, descricao: str) -> None:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._operacoes.append(f"[{timestamp}] {descricao}")

    def listar(self) -> List[str]:
        return list(self._operacoes)