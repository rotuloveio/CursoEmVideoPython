# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.

# Copiado da solução do exercício.
import random

n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')

lista = [n1, n2, n3, n4]

print(f'O(a) escolhid(a) é {random.choice(lista)}.')
