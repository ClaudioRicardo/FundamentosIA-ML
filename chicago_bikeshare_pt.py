# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

'''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Para imprimir as primeira 20 amostras optei por usar um for simples com range de 0 a 20
    e utilizei o indice i  parar numerar a listas
'''
for i in range(0,20):
  print("{} - ".format(i+1),data_list[i])

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

'''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Seguindo o padrão da questão anterior para imprimir a coluna referente a ogenero indiquei
    o indice da coluna 6
'''

for i in range(0,20):
  print("{} - ".format(i+1),data_list[i][6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem




def column_to_list(data, index):
    '''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com
    
    Criei a função column_to_list

    Essa função recebe a lista de dados originais e a percorre coletando os dados da coluna especificada 
    pelo parametro index e adiciona esses valores em uma nova lista que será retornada ao
    final do processo.

    Argumentos:
       data: lista com as amostras coletadas do arquivo
       index: Indice da coluna cujos dados é desejado criar uma lista.
    Retorna:
       Uma lista com os valores da coluna indicada por index.

    '''
    column_list = []
    for row in data:
        column_list.append(row[index])
      
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list[:20], -2))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.

'''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Para contabilizar os generos masculino e feminino usei um for 
    que percorrerá a lista retornada pela função column_to_list com index correspondendo  
    a coluna gênero.

    para cada interação eu verifico se é do genero masculino ou feminino e somo +1 as 
    suas respectivas variaveis caso correspondam a um dos dois grupos.

    usei o metodo lower para evitar problemas de comparação de string 
    de entrada como por exemplo ("Female" e "female" ou "Male" e "male")

'''
male = 0
female = 0

for gender in column_to_list(data_list, 6):
  if(gender.lower()=="male"):
      male += 1
  elif(gender.lower()=="female"):
      female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

def count_gender(data_list):
    '''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Fazendo uso do codigo que criei para o exemplo anterior eu criei a função 
    count_gender que recebe a lista de dados originais e retorna uma lista com o somatório
    dos gêneros masculino e feminino respctivamente.

    Argumentos:
       data_list: lista com as amostras coletadas do arquivo
       
    Retorna:
       Uma lista com os valores do somatório de gêneros masculino e feminino respectivamente.

    '''
    male = 0
    female = 0
    for gender in column_to_list(data_list, 6):
        if(gender.lower()=="male"):
            male += 1
        elif(gender.lower()=="female"):
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

def most_popular_gender(data_list):
    '''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    most_popular_gender recebe a lista original e utilizar count_gender para pegar os somatórios
    dos gêneros e compara-lós para dizer se um deles é maior ou se são iguais.

    Argumentos:
       data: lista com as amostras coletadas do arquivo
    Retorna:
       Uma uma string que indica qual dos gêneros tem maior quantidade ou se são iguais
       "Male","Female" ou "Equal"
    '''
    answer = ""
    cgender = count_gender(data_list)

    if(cgender[0] > cgender[1]):
        answer = "Male"  
    elif(cgender[0] < cgender[1]):
        answer = "Female"  
    else:
        answer = "Equal"  

    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")


def count_user_type(data_list):
    '''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Baseado na ativida anterior eu criei uma função para contabilizar os tipo de usuarios
    e gerar um gráfico similar ao exercício anterior.

    Argumentos:
       data: lista com as amostras coletadas do arquivo
    Retorna:
       Uma lista com os somatórios dos tipos customer,dependet ,subscriber respectivamente
    '''
    customer = 0
    subscriber = 0
    dependent = 0
    for utypes in column_to_list(data_list, -3):
        if(utypes.lower()=="customer"):
            customer += 1
        elif(utypes.lower()=="subscriber"):
            subscriber += 1
        elif(utypes.lower()=="dependent"):
            dependent += 1    

    return [customer,dependent,subscriber]



# Se tudo está rodando como esperado, verifique este gráfico!

types = ["Customer","Dependent", "Subscriber"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo Usuario')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo Usuario')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Nem todos os campos Gender estão preenchidos, alguns estão vazios e isso gera uma diferença entre o total de amostras e a soma dos gêneros."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().

trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.


def calc_min(trip_list):
    '''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Para verificar  o menor valor da lista eu usei a seguite lógica:
    iniciei a variavel min_trip com o primeiro valor da lista.

    Em seguida percorri a lista fazer uma comparação para cada variavel

    1) - se o valor atual for MENOR que min_trip
            min_trip recebe valor atual
            (Fazendo isso eu garato que ao final das interações min_trip terá o valor MENOR)

    Argumentos:
       trip_list: lista com os dados da coluna trip_list_duration
    Retorna:
       Retorna o menor valor da lista        
    '''
    min_trip = float(trip_list[0]) 
    for val in trip_list:
        if float(val) < min_trip:    
            min_trip = round(float(val))
    return min_trip 


def calc_max(trip_list):
    '''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Para verificar o maior e o menor valor da lista eu usei a seguite lógica:
    iniciei as variaveis min_trip e max_trip com o primeiro valor da lista.

    Em seguida percorri a lista fazer uma comparação para cada variavel

    1) - se o valor atual for MAIOR que max_trip
            max_trip recebe valor atual         
            (Fazendo isso eu garato que ao final das interações max_trip terá o valor MAIOR)

    Argumentos:
       trip_list: lista com os dados da coluna trip_list_duration
    Retorna:
       Retorna o maior valor da lista                
    '''
    max_trip = float(trip_list[0])
    for val in trip_list:
        if float(val) > max_trip:    
            max_trip = round(float(val))    

    return max_trip


def calc_sum(any_int_list):
    '''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Percorre a lista somando seus valores e retornando o resultado da soma

    Argumentos:
       any_int_list: lista com valores inteiros
    Retorna:
       Retorna o somatório dos itens da lista                
    '''
    soma = 0
    for num in any_int_list:
        soma+= num

    return soma
        

def calc_mean(trip_list):
    '''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com    

    Para achar a média dos valores da lista eu somei todos os valores da lista
    e dividi pela quantidade de itens na lista.
    
    Argumentos:
       trip_list: lista com os dados da coluna trip_list_duration
    Retorna:
       Retorna o resultado da média. Soma de todos os valores da lista dividido 
       pela quantidade de valores na lista                
    '''
    return round(calc_sum( [int(td) for td in trip_list] )/len(trip_list))



def calc_median(trip_list):
 
    '''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Para fazer a mediana eu ordenei a lista trip_duration depois verifico se o tamanho da 
    lista é par um impar:
    se a for impar eu pego o valor do meio da lista  e esse valor é a mediana

    se for par eu pego os dois valores do meio somo os dois valores e divido por 2 para chegar a mediana  

    Argumentos:
       trip_list: lista com os dados da coluna trip_list_duration
    Retorna:
       Retorna o resultado do calculo da mediana da lista

    '''

    trip_list.sort(key=int)
    trip_dur_sort = [int(td) for td in trip_list]

    indx_meio = len(trip_dur_sort)//2

    if (len(trip_dur_sort) % 2) == 0:
        median_trip = (trip_dur_sort[indx_meio] + trip_dur_sort[indx_meio +1])//2 
    else:
        median_trip = trip_dur_sort[indx_meio]   

    return median_trip    



min_trip = calc_min(trip_duration_list)
max_trip = calc_max(trip_duration_list)
mean_trip = calc_mean(trip_duration_list)
median_trip = calc_median(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

'''
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

    Para essa tarefa eu usei a função column_to_list para pegar os valores de start_stations
    depois usei set para excluir as repetições e vegar ao valores exato de start_stations

'''

Sstations = column_to_list(data_list, 3)
start_stations = set(Sstations)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
  Função de exemplo com anotações.
  Argumentos:
      param1: O primeiro parâmetro.
      param2: O segundo parâmetro.
  Retorna:
      Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
    """
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com
    Função de exemplo com anotações.
    Argumentos:
      column_list: Lista com a coluna que será trabalahda.
    Retorna:
      Duas listas. A primeira com os nomes dos tipos e a segunda com seus respectivos totais   
    """
    item_types = list(set(column_list))
    count_items = [0 for i in item_types]

    for item in column_list:
        count_items[item_types.index(item)]+=1

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------


input("Aperte Enter para continuar...")
print("\n Apartir desse pontos serão exibidos resultados de questões levantas pelo aluno.")
print("\n TAREFA EXTRA 1: Agrupar agrupar amostragem por faixa etária baseado no ano de aniversário")

'''
Questão EXTRA elaborada pelo aluno.
Autor: Claudio Azevedo
Email: claudwolf@hotmail.com

Um dado importante a ser considerado são as idades dos usuarios do serviço baseado em suas 
datas de nascimento

TODO EXTRA: Criar uma lista com as idades dos usuarios
            Verificar as quantidades de usuarios para 3 faixas etárias até 20 anos de idade, entre 20 e 40 anos de idade e maiores de 40 anos
            Gerar um gráfico para exibir os dados das faixas etárias.
'''
'''Obs.:Resolvi usar o ano de 2017 para calcular a idade dos usuarios no ano das amostragem.
Me parece mais correto,usar a data atual pode colocar usuarios em faixas diferentes. '''

ano_atual = 2017 
idade_int = lambda ano, ano_atual: ano_atual - int(float(ano)) if ano  else 0
age_list = [idade_int(idade,ano_atual) for idade in column_to_list(data_list,-1)]

'''
    0 -> <= 20
    1 -> > 20 and <=40
    2 ->  > 40
    3 -> usuarios que não informaram idade
'''
faixas = [ 0, 0, 0, 0]
for age in age_list:
    if age > 0:
        if age <= 20:
            faixas[0]+=1
        elif age > 20 and age <= 40:         
            faixas[1]+=1    
        elif age > 40:
            faixas[2]+=1
    else:
        faixas[3]+=1            
            
print("\nIdade <=20:",faixas[0],"\nIdade > 20 and Idade <= 40:",faixas[1] ,"\nIdade > 40:" ,faixas[2] ,"\nSem Idade:",faixas[3])
   
indfaixa = faixas.index(max(faixas))    

if indfaixa == 0:
    print("\nA faixa etária que mais fez uso do serviço foi Menor de 20 anos.")
elif indfaixa == 1:
    print("\nA faixa etária que mais fez uso do serviço foi Entre 20 e 40 anos.")
elif indfaixa == 2:
    print("\nA faixa etária que mais fez uso do serviço foi Maior de 40 anos")
elif indfaixa == 3:
    print("\nA faixa etária que mais fez uso do serviço foi a que não informou a idade.")   


types = ["menor/igual a 20","entre 20 e 40", "maior que 40","Sem Idade"]
quantity = faixas #count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)

plt.ylabel('Quantidade')
plt.xlabel('Faixa etária')
plt.xticks(y_pos, types)
plt.title('Quantidade por Faixa etária')
plt.show(block=True)


input("Aperte Enter para continuar...")
print("\n TAREFA EXTRA 2: A grupar dados por genero e faixas etárias")

'''Questão EXTRA elaborada pelo aluno.
    Autor: Claudio Azevedo
    Email: claudwolf@hotmail.com

TODO EXTRA: Baseado  na proposta anterior, cruzar os dados de gênero e faixa etária.
            
            
'''


fx_etaria_M = [0, 0, 0, 0]
fx_etaria_F = [0, 0, 0, 0]
list_genero = column_to_list(data_list,-2)
sem_genero_ano = 0
i = 0
#print(len(list_genero))
#print(len(age_list))
for genero in list_genero:

    if genero.lower() == "male":
        if age_list[i] > 0:
            if age_list[i] <= 20:
                fx_etaria_M[0]+=1
            elif age_list[i] > 20 and age_list[i] <= 40:         
                fx_etaria_M[1]+=1    
            elif age_list[i] > 40:
                fx_etaria_M[2]+=1
        else:
            fx_etaria_M[3]+=1

    elif genero.lower() == "female":
        if age_list[i]:
            if age_list[i] <= 20:
                fx_etaria_F[0]+=1
            elif age_list[i] > 20 and age_list[i] <= 40:         
                fx_etaria_F[1]+=1    
            elif age_list[i] > 40:
                fx_etaria_F[2]+=1
        else:
            fx_etaria_F[3]+=1
    else:
        sem_genero_ano+=1        
    
    i+=1    


indfaixaM = fx_etaria_M.index(max(fx_etaria_M))    

print("\nIdade <=20:",fx_etaria_M[0],"\nIdade > 20 and Idade <= 40:",fx_etaria_M[1] ,"\nIdade > 40:" ,fx_etaria_M[2] )

if indfaixaM == 0:
    print("\nA faixa etária Masculina que mais fez uso do serviço foi Menor de 20 anos.")
elif indfaixaM == 1:
    print("\nA faixa etária Masculina que mais fez uso do serviço foi Entre 20 e 40 anos.")
elif indfaixaM == 2:
    print("\nA faixa etária Masculina que mais fez uso do serviço foi Maior de 40 anos")
elif indfaixaM == 3:
    print("\nA faixa etária Masculina que mais fez uso do serviço foi a que não informou a idade.")   


indfaixaF = fx_etaria_F.index(max(fx_etaria_F))    

print("\nIdade <=20:",fx_etaria_F[0],"\nIdade > 20 and Idade <= 40:",fx_etaria_F[1] ,"\nIdade > 40:" ,fx_etaria_F[2] )

if indfaixaF == 0:
    print("\nA faixa etária Feminina que mais fez uso do serviço foi Menor de 20 anos.")
elif indfaixaF == 1:
    print("\nA faixa etária Feminina que mais fez uso do serviço foi Entre 20 e 40 anos.")
elif indfaixaF == 2:
    print("\nA faixa etária Feminina que mais fez uso do serviço foi Maior de 40 anos")
elif indfaixaF == 3:
    print("\nA faixa etária Feminina que mais fez uso do serviço foi a que não informou a idade.")   


print("\nSem idade e sem gênero:", sem_genero_ano)

genero_f_etarias = [
                    fx_etaria_M[0],
                    fx_etaria_F[0],
                    fx_etaria_M[1],
                    fx_etaria_F[1],
                    fx_etaria_M[2],
                    fx_etaria_F[2],
                    sem_genero_ano
                   ]

types = ["M\ny < 20","F\ny < 20","M\n20 < y <=40","F\n20 < y <=40","M\ny > 40","F\ny > 40","Sem Idade/Gênero"]
quantity = genero_f_etarias 
y_pos = list(range(len(types)))
m1 ,f1 ,m2 ,f2, m3 ,f3 ,semGA  = plt.bar(y_pos, quantity)
m1.set_facecolor('blue')
f1.set_facecolor('red')
m2.set_facecolor('blue')
f2.set_facecolor('red')
m3.set_facecolor('blue')
f3.set_facecolor('red')
semGA.set_facecolor('gray')


plt.ylabel('Quantidade')
plt.xlabel('Gênero / faixa etária')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero / faixa etária')
plt.show(block=True)

'''
    IMPORTANTE 

    Obs.: Se compararmos os dados dos valores dos gráficos de faixa etária  e o de Gênero/Faixa etária,
    vamos ver que os somatórios não batem.Isso ocorre por que alguns registros não tem dados 
    de gênero e de ano de nascimento.
'''