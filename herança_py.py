# -*- coding: utf-8 -*-
"""herança.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17qWuvRxiCrMAcHcAzC0ij8CQw9ZoNvjn
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, valor):
        self.salario += valor


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def relatorio(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")
        print(f"Departamento: {self.departamento}")


# Demonstração de uso das classes
if __name__ == "__main__":
    # Criando um funcionário
    funcionario = Funcionario("João", 3000.00)
    print(f"Salário inicial do {funcionario.nome}: R$ {funcionario.salario:.2f}")

    # Aumentando o salário do funcionário
    funcionario.aumentar_salario(500.00)
    print(f"Salário após aumento do {funcionario.nome}: R$ {funcionario.salario:.2f}")

    # Criando um gerente
    gerente = Gerente("Maria", 5000.00, "Vendas")

    # Exibindo o relatório do gerente
    print("\nRelatório do Gerente:")
    gerente.relatorio()

    # Aumentando o salário do gerente
    gerente.aumentar_salario(1000.00)
    print("\nRelatório do Gerente após aumento de salário:")
    gerente.relatorio()