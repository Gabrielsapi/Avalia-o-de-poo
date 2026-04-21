# Sistema de Caixa Eletrônico em Python

## Descrição

Este projeto consiste na implementação de um sistema de caixa eletrônico (ATM) desenvolvido em Python, utilizando os principais conceitos de Programação Orientada a Objetos (POO).

O sistema permite a criação e gerenciamento de contas bancárias, incluindo operações como depósito, saque, consulta de saldo e visualização de histórico de transações.

---

## Objetivo

Demonstrar, de forma prática, a aplicação dos seguintes conceitos de POO:

- Encapsulamento
- Herança
- Polimorfismo
- Abstração
- Agregação
- Composição

---

## Estrutura do Projeto

```
banco/
│
├── clientes/         # Classe Cliente
├── contas/           # Classes de contas (base e especializações)
├── operacoes/        # Histórico de operações
├── sistema/          # Classe Banco
└── main.py           # Interface principal
```

---

## Conceitos de POO Aplicados

### 1. Encapsulamento
Atributos privados (prefixo `_`) são utilizados para proteger os dados internos das classes. O acesso é feito por meio de propriedades (`@property`).

### 2. Herança
As classes `ContaCorrente` e `ContaPoupanca` herdam da classe abstrata `Conta`.

### 3. Polimorfismo
O método `sacar()` possui implementações diferentes em cada tipo de conta.

### 4. Abstração
A classe `Conta` é abstrata e define a estrutura básica para as contas.

### 5. Agregação
A classe `Banco` mantém uma coleção de contas.

### 6. Composição
Cada `Conta` possui um `Historico`, que não existe independentemente da conta.

---

## Funcionalidades

- Criar conta (corrente ou poupança)
- Depositar valores
- Realizar saques
- Consultar saldo
- Visualizar histórico de operações

---

## Regras de Negócio

- Não é permitido sacar valores negativos
- Não é permitido sacar valores maiores que o saldo disponível
- Conta corrente permite uso de limite
- Todas as operações são registradas no histórico
- Entradas inválidas são tratadas

---

## Como Utilizar o Sistema

Ao executar o programa, será exibido um menu interativo no terminal:

```
1 - Criar conta
2 - Depositar
3 - Sacar
4 - Consultar saldo
5 - Histórico
0 - Sair
```

### Criar Conta

- Informe nome e CPF
- Escolha o tipo de conta:
  - 1: Conta Corrente
  - 2: Conta Poupança
- O sistema retornará o ID da conta criada

### Depositar

- Informe o ID da conta
- Informe o valor do depósito

### Sacar

- Informe o ID da conta
- Informe o valor do saque
- O sistema validará saldo e regras específicas

### Consultar Saldo

- Informe o ID da conta
- O saldo será exibido

### Histórico

- Informe o ID da conta
- Todas as operações serão listadas com data e hora

---

## Exemplo de Uso

```
Sistema de Caixa Eletrônico
1 - Criar conta
...

Conta criada com ID 1

Depositar:
Valor: 100

Saldo atual: R$100.00
```

---

## Boas Práticas Utilizadas

- Separação de responsabilidades
- Código modular
- Baixo acoplamento
- Uso de tipagem
- Tratamento de exceções


