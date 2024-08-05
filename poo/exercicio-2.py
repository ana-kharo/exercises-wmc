# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

# Primeiramente irei criar uma classe abstrata com informações básicas. [Cliente]:

from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def telefone(self):
        return self._telefone
    
    @property
    def renda_mensal(self):
        return self._renda_mensal

    @abstractmethod
    def cheque_especial(self):
        pass

# Agora farei com que a classe [ClienteMulher] herde a classe [Cliente] e implementarei o [cheque_especial]:

class ClienteMulher(Cliente):
    def cheque_especial(self):
            return self._renda_mensal
        
# Agora a classe que também irá herdar de [Cliente] porém não terá direito ao [cheque_especial]:   

class ClienteHomem(Cliente):
    def cheque_especial(self):
            return(0)
        
# Agora irei criar a Classe de [ContaCorrente]:

class ContaCorrente:
    def __init__(self, *clientes):
            self._clientes = clientes
            self._saldo = 0
            self._operacoes = []

    @property
    def saldo(self):
        return self._operacoes

    def depositar(self, valor):
        self._saldo += valor
        self._operacoes.append(f'Depósito: +{valor}')

    def sacar(self, valor):
        max_cheque_especial = sum(cliente.cheque_especial() for cliente in self._clientes) 
        if self._saldo - valor >= -max_cheque_especial:
            self._saldo -= valor
            self._operacoes.append(f'Saque: -{valor}')
            return True
        else:
            print('Saldo insuficiente para efetuar o saque.')
            return False
        
    def listar_clientes(self):
        return [cliente.nome for cliente in self._clientes]    

# Agora irei trazer alguns exemplos práticos:

cliente1 = ClienteMulher("Ana", "12345-6789", 7000)
cliente2 = ClienteHomem("Matheus", "98765-4321", 3500)

conta = ContaCorrente(cliente1, cliente2)
conta.depositar(1000)
conta.sacar(500)
print(conta.saldo) 
print(conta.listar_clientes())  