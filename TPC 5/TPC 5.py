# TPC 5 -> Aplicação de Gestão de um Cinema

# A aplicação deve ser composta pelas seguintes funções:
    # Lista de todos os filmes a ser exibidos nas salas do cinema
    # Estado de disponibilidade de um lugar selecionado numa sala do cinema
    # Atualização da lista de lugares ocupados na sala do cinema após a venda de um bilhete
    # Apresentação do filme a ser exibido em cada sala do cinema e o número total de lugares disponíveis nessa sala
    # Inserção de uma nova sala à lista de salas existentes no cinema e verificação da possível prévia existência dessa sala

# Estrutura dos dados

# Cinema -> [sala 1, sala 2, sala 3, ...]
# Sala -> [num lugares, bilhetes vendidos, filme]
# Num lugares -> inteiro
# Bilhetes vendidos -> [inteiro]
# Filme -> string

# ---------------------------- Criar o menu da aplicação ----------------------------

def menu():
    print('Menu')
    print('1) Lista de filmes em exibição')
    print('2) Disponibilidade de um lugar específico na sala') # Tem de dar um boleano como resultado da função
    print('3) Bilhete vendido')
    print('4) Lugares disponíveis em cada sala')
    print('5) Procurar filme no cinema')
    print('6) Inserir uma nova sala')
    print('0) Sair')

# ---------------------------- Funções da aplicação ----------------------------

# Opção 6 --> Inserir nova sala, garantindo que não haja duplicação de salas
def Inserir_sala(cinema, sala):
    
    for s in cinema:
        if s[2] == sala[2]:  # Verifica se o filme já está associado a outra sala
            print(f'A sala com o filme "{sala[2]}" já existe.')
            return cinema
    cinema.append(sala)
    print(f'Sala adicionada com sucesso: {sala}')
    return cinema

# Opção 1 --> Listar Filmes em exibição
def Listar(cinema):
    
    print('-----------------')
    print('Filmes')
    print('-----------------')
    for sala in cinema:
        print(sala[2])
    return

# Opção 3 --> Registar venda de bilhetes
def Bilhete_vendido(cinema, filme, lugar):
    
    for sala in cinema:
        if sala[2] == filme:
            if lugar not in sala[1] and lugar <= sala[0]:
                sala[1].append(lugar)
                print(f'Lugar {lugar} vendido com sucesso para o filme "{filme}"!')
                return
            else:
                print(f'Lugar {lugar} já está ocupado ou é inválido.')
                return
    print(f'Filme "{filme}" não disponível')

# Opção 2 --> Verificar disponibilidade de um lugar
def Lugar_disponibilidade(cinema, filme, lugar):
    
    for sala in cinema:
        if sala[2] == filme:
            if lugar in sala[1]:
                print(f'Lugar {lugar} está ocupado.')
                return False
            elif lugar > sala[0]:
                print(f'Lugar {lugar} é inválido.')
                return False
            else:
                print(f'Lugar {lugar} está disponível.')
                return True
    print(f'Filme "{filme}" não disponível.')
    return False

# Opção 4 --> Listar lugares disponíveis em cada sala
def Listar_disponibilidade(cinema):
    
    print('Lugares disponíveis')
    print('Filmes ------- Lugares')
    for sala in cinema:
        lug_disponíveis = sala[0] - len(sala[1])
        print(f'{sala[2]} ------- {lug_disponíveis}')
    return

# Opção 5 --> Procurar um filme em exibição no cinema
def Procura(cinema, filme):
    
    res = -1
    i = 0
    for i, sala in enumerate(cinema): # i corresponde ao índice de cada sala dentro do cinema
        if sala[2] == filme:
            print(f'Filme "{filme}" encontrado na sala {i + 1}.')
            return i
    print(f'Filme "{filme}" não encontrado.')
    return res
# ---------------------------- Programa Principal ----------------------------

# Dados do cinema
cinema = [
    [200, [], 'Shrek 2'],
    [150, [], 'How To Lose a Guy In 10 Days'],
    [250, [], 'La La Land'],
    [200, [], 'Interstellar']
]

opção = -1
while opção != 0:
    menu()
    opção = int(input('Selecione a opção desejada: '))
    
    if opção == 1:
        Listar(cinema)
    elif opção == 2:
        filme = input('Introduza o nome do filme: ')
        lugar = int(input('Introduza o número do lugar: '))
        Lugar_disponibilidade(cinema, filme, lugar)
    elif opção == 3:
        filme = input('Introduza o nome do filme: ')
        lugar = int(input('Introduza o número do lugar que deseja: '))
        Bilhete_vendido(cinema, filme, lugar)
    elif opção == 4:
        Listar_disponibilidade(cinema)
    elif opção == 5:
        filme = input('Introduza o nome do filme: ')
        Procura(cinema, filme)
    elif opção == 6:
        num_lugares = int(input('Número de lugares da nova sala: '))
        filme = input('Nome do novo filme a exibir: ')
        nova_sala = [num_lugares, [], filme]
        cinema = Inserir_sala(cinema, nova_sala)
print('Até à próxima!')
