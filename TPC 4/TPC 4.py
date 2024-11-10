# TPC 4 -> Aplicação de Manipulação de Listas de Inteiros

# A aplicação terá uma variável interna para guardar uma lista de números;
    # Na opção 1, deverá ser criada uma lista de números aleatórios entre 1 e 100 que será guardada na variável interna;
    # Na opção 2, deverá ser criada uma lista com números introduzidos pelo utilizador, que será guardada na variável interna;
    # Nestas primeiras opções, se a variável interna já tiver uma lista, esta será sobreposta/apagada pela nova lista;
    # Na opção 3, será calculada a soma dos elementos na lista no momento;
    # Na opção 4, será calculada a média dos elementos na lista no momento;
    # Na opção 5, será calculado o maior elemento da lista no momento;
    # Na opção 6, será calculado o menor elemento da lista no momento;
    # Na opção 7, a aplicação deverá indicar (Sim/Não) se a lista está ordenada por ordem crescente;
    # Na opção 8, a aplicação deverá indicar (Sim/Não) se a lista está ordenada por ordem decrescente;
    # Na opção 9, a aplicação irá procurar um elemento na lista, se o encontrar deverá devolver a sua posição, devolverá -1 se o elemento não estiver na lista;
    # Se o utilizador selecionar a opção 0, a aplicação deverá terminar mostrando a lista que está nesse momento guardada.

# ---------------------------- Criar o menu da aplicação  ----------------------------
def menu():
    print('Menu')
    print('1) Criar lista')
    print('2) Ler lista')
    print('3) Soma')
    print('4) Média')
    print('5) Maior')
    print('6) Menor')
    print('7) Está ordenada por ordem crescente')
    print('8) Está ordenada por ordem decrescente')
    print('9) Procurar um elemento')
    print('0) Sair')

# ---------------------------- Funções da aplicação  ----------------------------

v_interna = [] # Variável interna da aplicação onde serão guardadas as listas criadas

# Opção 1
def Cria_lista():

    from random import randint
    n = int(input('Escolha um número de elementos para a lista que deseja criar:'))
    res = []
    i = 1
    while i <= n:
        res.append(randint(1,100))
        i = i + 1
    return res

# Opção 2
def Le_lista():

    n = int(input('Introduza o número de elementos desejados para a lista:'))
    res = []
    i = 1
    while i <= n:
        res.append(int(input('Introduza o elemento desejado:')))
        i = i + 1
    return res

# Opção 3
def Soma(lista):

    soma = 0
    for x in lista:
        soma = soma + x
    return soma

# Opção 4
def Média(lista):

    res = 0
    for x in lista:
        res = res + x
    return (res/len(lista))

# Opção 5
def Maior(lista):

    res = lista[0]
    for x in lista:
        if x > res:
            res = x
    return res

# Opção 6
def Menor(lista):

    res = lista[0]
    for x in lista:
            if x < res:
                res = x
    return res

# Opção 7
def Ordem_crescente(lista):

    crescente = True
    i = 0
    res = ''
    while crescente and i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            crescente = False
            res = 'Não'
        else:
            i = i + 1
            res = 'Sim'
    return res

# Opção 8
def Ordem_decrescente(lista):

    decrescente = True
    i = 0
    res = ''
    while decrescente and i < len(lista) - 1:
        if lista[i] < lista[i + 1]:
            decrescente = False
            res = 'Não'
        else:
            i = i + 1
            res = 'Sim'
    return res

# Opção 9
def Procura(lista):

    x = int(input('Introduza o elemento da lista que deseja procurar'))
    limite_inicial = 0
    limite_final = len(lista) - 1
    encontrado = False

    while limite_inicial <= limite_final and not encontrado:
        meio = (limite_inicial + limite_final) // 2
        if lista[meio] == x:
            encontrado = True
            return meio
        elif lista[meio] < x:
            limite_inicial = meio + 1
        else:
            limite_final = meio - 1

    return meio if encontrado else -1  

# ---------------------------- Programa Principal ----------------------------

menu()
opção = int(input('Selecione a opção desejada:'))

while opção != 0:

    if opção == 1:
        v_interna = Cria_lista()
    elif opção == 2:
        v_interna = Le_lista()
    elif opção == 3:
        print(Soma(v_interna))
    elif opção == 4:
        print(Média(v_interna))
    elif opção == 5:
        print(Maior(v_interna))
    elif opção == 6:
        print(Menor(v_interna))
    elif opção == 7:
        print(Ordem_crescente(v_interna))
    elif opção == 8:
        print(Ordem_decrescente(v_interna))
    elif opção == 9:
        posição = Procura(v_interna)
        if posição == -1:
            print('O elemento que procura não se encontra na lista')
        else:
            print(f'O elemento que procura encontra-se na posição: {posição}')
    opção = int(input('Selecione a opção desejada:'))
print(v_interna)
print('Obrigado! Até à próxima!')