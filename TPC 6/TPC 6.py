# TPC 6 -> Aplicação de Gestão de Alunos numa Turma

# A aplicação deve ser composta pelas seguintes funções:
    # Criação de uma turma
    # Inserção de um novo aluno na turma
    # Lista de todos os alunos registados na turma
    # Consulta de um aluno por id
    # Guardar a turma num ficheiro
    # Carregamento da informação da turma dum ficheiro

# Estrutura dos dados

# Turma -> [aluno 1, aluno 2, aluno 3, ...]
# Aluno -> (nome, id, [nota tpc, nota projeto, nota teste])
# Nome -> string
# Id -> inteiro
# Nota tpc -> inteiro
# Nota projeto -> inteiro
# Nota teste -> inteiro

# ---------------------------- Criar o menu da aplicação ----------------------------

def menu():
    print('\n Menu')
    print('1) Criar turma')
    print('2) Inserir um novo aluno')
    print('3) Lista de alunos registados na turma')
    print('4) Consultar aluno por id')
    print('5) Guardar turma num ficheiro')
    print('6) Carregar turma dum ficheiro')
    print('0) Sair')

# ---------------------------- Funções da aplicação ----------------------------

# Opção 1
def Criar_turma(turma):

    nome = input('Introduza o nome do aluno: ')
    id = int(input('Introduza o id do aluno: '))
    nota_tpc = int(input('Introduza a nota dos tpcs do aluno: '))
    nota_projeto = int(input('Introduza a nota do projeto do aluno: '))
    nota_teste = int(input('Introduza a nota do teste do aluno: '))

    aluno = (nome, id, [nota_tpc, nota_projeto, nota_teste])

    turma.append(aluno)
    return turma

# Opção 2
def Inserir_aluno(turma):

    nome = input('Introduza o nome do aluno: ')
    id = int(input('Introduza o id do aluno: '))
    nota_tpc = int(input('Introduza a nota dos tpcs do aluno: '))
    nota_projeto = int(input('Introduza a nota do projeto do aluno: '))
    nota_teste = int(input('Introduza a nota do teste do aluno: '))

    aluno = (nome, id, [nota_tpc, nota_projeto, nota_teste])

    for a in turma:
        if a[1] == aluno[1]:
            print(f'O registo para o aluno com id {aluno[1]} já existe')
            return
    turma.append(aluno)
    print(f'Registo adicionado com sucesso: {aluno}')
    return

# Opção 3
def Listar(turma):

    print('-----------------')
    print('Alunos')
    print('-----------------')
    for aluno in turma:
        nome, id, notas = aluno  # Desempacotar o tuplo
        print(f'Nome: {nome}, ID: {id}, Notas: {notas}')
    return

# Opção 4
def Consulta(turma, id):
    i = 0
    id = int(input('Introduza o id do aluno: '))
    for i, aluno in enumerate(turma): # i corresponde ao índice de cada aluno dentro da turma
        if aluno[1] == id:
            print(f'Nome: {aluno[0]}, ID: {id}, Notas: {aluno[2]}')
            return
    print(f'Aluno com id {id} não encontrado na turma')

# Opção 5
def Guardar_turma(turma, fnome):
    
    with open(fnome, 'w') as file:
        for nome, id, notas in turma: # Aluno fica formatado como 'nome,id::nota1,nota2,nota3'
            notas_str = ",".join(map(str, notas))
            linha = f'{nome},{id}::{notas_str}\n'
            file.write(linha)
    print(f'Turma guardada em {fnome}')

# Opção 6
def Carregar_turma(fnome):

    turma = []
    file = open(fnome,'r')
    for linha in file:
        if linha != '': # Identifica linhas com texto
            dados = linha.split('::') # Dividimos as linhas do ficheiro nos dados do tuplo
            nome_id = dados[0].split(',')
            nome = nome_id[0]
            id = int(nome_id[1])
            notas = list(map(int, dados[1].split(',')))
            aluno = (nome, id, notas)
            turma.append(aluno)
    return turma

# ---------------------------- Programa Principal ----------------------------

# Variável onde vamos armazenar os dados da turma
turma = []

opção = -1

while opção != 0:
    menu()
    opção = int(input('Selecione a opção desejada: '))

    if opção == 1:
        Criar_turma(turma)
    elif opção == 2:
        Inserir_aluno(turma)
    elif opção == 3:
        Listar(turma)
    elif opção == 4:
        Consulta(turma, id)
    elif opção == 5:
        Guardar_turma(turma, 'turma.txt')
    elif opção == 6:
        Carregar_turma('turma.txt')
print('Até à próxima!')
