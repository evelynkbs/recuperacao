# -*- coding: utf-8 -*-
"""validaçao.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17qWuvRxiCrMAcHcAzC0ij8CQw9ZoNvjn
"""

class Validacao:
    def __init__(self, nome, idade, sexo, numero_chamada, serie, ano_colegio, cidade, estado, pais):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.numero_chamada = numero_chamada
        self.serie = serie
        self.ano_colegio = ano_colegio
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

# Função para verificar se um número é positivo
def eh_positivo(numero):
    return numero > 0

# Função para verificar se um número é positivo, negativo ou zero
def tipo_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

# Função para validar se um número é par, ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Função para verificar se um número é primo
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Função para verificar se a idade está entre 0 e 100
def valida_idade(idade):
    return 0 <= idade <= 100

# Função para classificar idade em bebê, criança, adolescente, adulto ou idoso
def classifica_idade(nome, idade):
    if idade < 0:
        return "Idade inválida"
    elif idade < 2:
        return f"{nome} é um bebê"
    elif idade < 13:
        return f"{nome} é uma criança"
    elif idade < 20:
        return f"{nome} é um adolescente"
    elif idade < 65:
        return f"{nome} é um adulto"
    else:
        return f"{nome} é um idoso"

# Função para validar se uma string tem comprimento mínimo de 5 caracteres
def valida_comprimento_minimo(texto, min_comprimento=5):
    return len(texto) >= min_comprimento

# Função para retornar a quantidade de caracteres de uma string
def quantidade_caracteres(texto):
    return len(texto)

# Função para retornar a quantidade de elementos em um array (ou lista)
def quantidade_elementos(array):
    return len(array)

# Função para verificar se um número está dentro de um intervalo específico
def dentro_intervalo(numero, inicio, fim):
    return inicio <= numero <= fim

# Criando um objeto Validacao
objeto_validacao = Validacao("João", 25, "M", 10, "3A", 2024, "São Paulo", "SP", "Brasil")

# Exemplo de uso das funções de validação
print(eh_positivo(5))  # True
print(tipo_numero(-2))  # "negativo"
print(par_ou_impar(7))  # "ímpar"
print(eh_primo(11))  # True
print(valida_idade(45))  # True
print(classifica_idade("Maria", 3))  # "Maria é uma criança"
print(valida_comprimento_minimo("Python"))  # True
print(quantidade_caracteres("Hello, World!"))  # 13
print(quantidade_elementos([1, 2, 3, 4, 5]))  # 5
print(dentro_intervalo(25, 20, 30))  # True