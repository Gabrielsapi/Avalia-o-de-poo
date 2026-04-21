from contas.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            return False

        if valor > self._saldo:
            return False

        self._saldo -= valor
        self._historico.registrar(f"Saque (Conta Poupança): R${valor:.2f}")
        return True