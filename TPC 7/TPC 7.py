# TPC 7 -> Aplicação de Gestão de Registos Metereológicos

# Estrutura dos dados

# Tabela Meteriológica -> [(Data, Temp Mínima, Temp Máxima, Precipitação)]
# Data -> (inteiro, inteiro, inteiro)
# Temp Mínima -> float
# Temp Máxima -> float
# Precipitação -> float

# ---------------------------- Criar o menu da aplicação ----------------------------
def menu():
    print('\n Menu')
    print('1) Média das temperaturas')
    print('2) Guardar tabela meteriológica')
    print('3) Carregar tabela meteriológica')
    print('4) Temperatura mínima mais baixa')
    print('5) Amplitude máxima')
    print('6) Dia com maior precipitação')
    print('7) Dias com precipitação superior a um limite')
    print('8) Maior período de calor')
    print('9) Mostrar gráfico metereológico')
    print('0) Sair')

# ---------------------------- Funções da aplicação ----------------------------

# Opção 1
def Média_temp(tab_meteo):

    res = []
    for previsão in tab_meteo:
        data, min, max, prec = previsão
        media = (min + max)/2
        res.append((data,media))
    return res

# Opção 2
def Guardar_tabela(tabela, fnome):

    file = open(fnome,'w')
    for previsao in tabela:
        data, min,max, prec = previsao
        file.write(str(data)+ '|' +  str(min) + '|' + str(max)+ '|' + str(prec))
        file.write('\n')
    file.close()

# Opção 3
def Carregar_tabela(fnome):

    res = []
    file = open(fnome,'r')
    for linha in file:
        previsão = linha.strip().split('),')
        if len(previsão) == 4:
            data = previsão[0]
            min, max, prec = map(float, previsão[1:])
            nova_previsão = (data, min, max, prec)
            res.append(nova_previsão)
    
    file.close()       
    return res

# Opção 4
def Min_temp(tab_meteo):
    
    i = 1
    mínima = tab_meteo[0][1]
    if tab_meteo[i][1] < mínima:
            mínima = tab_meteo[i][1]
            i = i + 1
    return mínima

# Opção 5
def Amplitude_temp(tab_meteo):

    res = []
    for previsão in tab_meteo:
        data, min, max, prec = previsão
        amplitude = max - min
        res.append((data, amplitude))
    return res 

# Opção 6
def Max_chuva(tab_meteo):

    máxima = tab_meteo[0][3]
    i = 1
    if tab_meteo[i][3] > máxima:
        máxima = tab_meteo[i][3]
        data_max = tab_meteo[i][0]
        i = i + 1
    return (data_max, máxima)   

# Opção 7
def Dias_chuvosos(tab_meteo, p):

    i = 0
    print('\nTabela meteorológica')
    print('-------------------------------------------')
    print('data                 |         precipitação')

    while i < len(tab_meteo):
        if tab_meteo[i][3] > p:
            print(f'{tab_meteo[i][0]}         |         {tab_meteo[i][3]}')
        i = i + 1
    return

# Opção 8
def Max_calor(tab_meteo, p):

    max_consecutivos = 0
    consecutivos_atual = 0  # Sequência atual de dias secos na tabela de registos

    for previsão in tab_meteo:
        prec = previsão[3]
        if prec < p:
            consecutivos_atual = consecutivos_atual + 1
        else:
            if consecutivos_atual > max_consecutivos:
                max_consecutivos = consecutivos_atual
            consecutivos_atual = 0  # Reiniciamos a contagem para a próxima sequência

    # Voltamos a confirmar se a última sequência foi a maior
    if consecutivos_atual > max_consecutivos:
        max_consecutivos = consecutivos_atual

    return max_consecutivos

# Opção 9

import matplotlib.pyplot as plt
def Gráfico(t):

    datas = [f'{data[0]} - {data[1]} - {data[2]}' for data, *_ in t]
    temp_min = [min for _,min, *_ in t]
    temp_max = [max for _,_,max, *_ in t]
    precs = [prec for _,_,_, prec in t]
    
    plt.plot(datas,temp_min, label = 'temp min') #recebe um x e um y
    plt.xlabel('Data')
    plt.ylabel('Temperatura ºC')
    plt.title('Temperatura mínima, máxima e precipitação')
    #plt.show()
    plt.plot(datas,temp_max, label = 'temp max') #recebe um x e um y
    #plt.show()
    plt.plot(datas,precs,label = 'precipitação') #recebe um x e um y
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.bar(datas,precs,label = 'precipitação')
    plt.legend()
    plt.show()
    
    return

# ---------------------------- Programa Principal ----------------------------

# Variável onde vamos armazenar os dados metereológicos
tab_meteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

opção = -1

while opção != 0:
    menu()
    opção = int(input('Selecione a opção desejada: '))

    if opção == 1:
        print(Média_temp(tab_meteo1))
    elif opção == 2:
        print(Guardar_tabela(tab_meteo1, 'meteorologia.txt'))
    elif opção == 3:
        print(Carregar_tabela('metereologia.txt'))
    elif opção == 4:
        print(Min_temp(tab_meteo1))
    elif opção == 5:
        print(Amplitude_temp(tab_meteo1))
    elif opção == 6:
        print(Max_chuva(tab_meteo1))
    elif opção == 7:
        print(Dias_chuvosos(tab_meteo1, 0))
    elif opção == 8:
        print(Max_calor(tab_meteo1, 0.6))
    elif opção == 9:
        print(Gráfico(tab_meteo1))
print('Até à próxima!')