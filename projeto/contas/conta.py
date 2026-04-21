from abc import ABC, abstractmethod
from operacoes.historico import Historico


class Conta(ABC):
    _sequencial = 1

    def __init__(self, cliente):
        self._id = Conta._sequencial
        Conta._sequencial += 1

        self._cliente = cliente
        self._saldo = 0.0
        self._historico = Historico()

    @property
    def id(self) -> int:
        return self._id

    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            return False

        self._saldo += valor
        self._historico.registrar(f"Depósito: R${valor:.2f}")
        return True

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    def obter_historico(self):
        return self._historico.listar()