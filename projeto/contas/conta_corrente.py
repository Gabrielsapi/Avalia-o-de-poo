# contas/conta_corrente.py

from contas.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, cliente):
        super().__init__(cliente)

    def sacar(self, valor: float) -> bool:
        # Validação de valor inválido
        if valor <= 0:
            return False

        # Regra de negócio: não permitir saque com saldo insuficiente
        if valor > self._saldo:
            return False

        # Operação de saque
        self._saldo -= valor
        self._historico.registrar(f"Saque (Conta Corrente): R${valor:.2f}")
        return True