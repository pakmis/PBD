import math
import random

users = [
    {"id": 0, "name": "Hero", "genre": "F", "age": 22},
    {"id": 1, "name": "Dunn", "genre": "M", "age":20},
    {"id": 2, "name": "Sue", "genre": "F", "age": 18},
    {"id": 3, "name": "Chi", "genre": "M", "age":19},
    {"id": 4, "name": "Thor", "genre": "F", "age": 18},
    {"id": 5, "name": "Clive", "genre": "M", "age":23},
    {"id": 6, "name": "Hicks", "genre": "M", "age": 18},
    {"id": 7, "name": "Devin", "genre": "M", "age":21},
    {"id": 8, "name": "Kate", "genre": "F", "age": 18},
    {"id": 9, "name": "Klein", "genre": "F", "age":20},
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 6), (6, 8), (7, 8), (8, 9)
]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends (user):
    return len(user["friends"])

users_idades = []
users_friends = []

for user in users:
    users_idades.append(user["age"])
    users_friends.append(number_of_friends(user))

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def variance(v):
    mean = sum(v) / len(v)
    return [v_i - mean for v_i in v]

def covariance(x, y):
    n = len(x)
    return dot(variance(x), variance(y)) / (n - 1)

def covariance_test(x, y):
    print(f"covariance: {covariance(x, y)}")

def correlation(x, y):
    desvio_padrao_x = math.sqrt(sum_of_squares(variance(x)) / (len(x) - 1))
    desvio_padrao_y = math.sqrt(sum_of_squares(variance(y)) / (len(y) - 1))
    if desvio_padrao_x > 0 and desvio_padrao_y > 0:
        return covariance(x, y) / desvio_padrao_y / desvio_padrao_x
    return 0

def correlation_test(x, y):
    print(f"correlation: {correlation(x, y)}")

def generate_random_list_positive_covariance(number_of_elements):
    x =[]
    y =[]
    ux =0
    uy = 0
    for i in range(number_of_elements):
        while True:
            ux = random.randint(0, 50)
            uy = random.randint(50, 1000)
            if i == 0:
                x.append(ux)
                y.append(uy)
                break
            if (ux < x[i-1]) and (uy < y[i-1]):
                x.append(ux)
                y.append(uy)
                break

    print (x)
    print (y)
    correlation_test(x, y)

def generate_random_list_negative_covariance(number_of_elements):
    x =[]
    y =[]
    ux =0
    uy = 0
    for i in range(number_of_elements):
        while True:
            ux = random.randint(0, 50)
            uy = random.randint(50, 1000)
            if i == 0:
                x.append(ux)
                y.append(uy)
                break
            if (ux < x[i-1]) and (uy > y[i-1]):
                x.append(ux)
                y.append(uy)
                break

    print (x)
    print (y)
    correlation_test(x, y)

def generate_random_list_zero_covariance(number_of_elements):
    x =[]
    y =[]
    ux =0
    uy = 0
    for i in range(number_of_elements):
        while True:
            ux = random.randint(0, 10*number_of_elements)
            uy = random.randint(number_of_elements, 10*number_of_elements)
            if i == 0:
                x.append(ux)
                y.append(uy)
                break
            elif (ux > x[i-1]) and uy > y[i-1]:
                x.append(ux)
                y.append(y[i-1])
                break
            elif (ux < x[i-1]) and uy < y[i-1]:
                x.append(x[i-1])
                y.append(uy)
                break

    print (x)
    print (y)
    correlation_test(x, y)

def main():
    # 1 Escreva uma função que calcula a covariância entre idade e número de amigos.
    # covariance_test(users_friends, users_idades)
    # 2 Escreva uma função que calcula a correlação entre idade e número de amigos.
    # correlation_test(users_friends, users_idades)
    # 3 Escreva uma função que devolve uma tupla de duas listas. A primeira lista contém quantidadesde amigos que cada usuário da rede tem.
    #  A segunda, quantidades de minutos passados em médiana rede por cada usuário. Cada lista tem tamanho n, sendo n um valor recebido 
    # como parâmetro.Os dados devem ser gerados aleatoriamente. Faça três versões.
    #   3.1 Gere dados aleatoriamente garantindo correlação próxima de 1.
    # generate_random_list_positive_covariance(3)
    #   3.2 Gere dados aleatoriamente garantindo correlação próxima de -1.
    # generate_random_list_negative_covariance(3)
    #   3.3 Gere dados aleatoriamente garantindo correlação próxima de 0.
    # generate_random_list_zero_covariance(3)
    # 4 Escreva uma função de teste que mostra que os dados gerados no Exercício 3 estão de acordocom o solicitado.
    generate_random_list_positive_covariance(3)
    generate_random_list_negative_covariance(3)
    generate_random_list_zero_covariance(3)
main()