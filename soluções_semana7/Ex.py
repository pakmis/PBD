from collections import defaultdict
from collections import Counter
from matplotlib import pyplot as plt
import math

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

def number_of_friends_by_genre():
    friends_by_genre = [0, 0]
    for user in users:
        if user["genre"] == "M":
            friends_by_genre[0] += number_of_friends(user)
        else:
            friends_by_genre[1] += number_of_friends(user)
    return friends_by_genre

def histograma_number_of_friends_by_genre():
    generos = ['Homem', 'Mulher']
    xs = [i for i, _ in enumerate(generos)]
    plt.bar(xs, number_of_friends_by_genre())
    plt.ylabel('#N° de Amigos')
    plt.xlabel('#Generos')
    plt.xticks(xs, generos)
    plt.show()

def number_of_friends_by_interval(min, max):
    total_friends = 0
    for user in users:
        if user["age"] > min and user["age"] <= max:
            total_friends += number_of_friends(user)
    return total_friends

def histogram_number_of_friends_by_age():
    histogram = Counter (user["age"] // 10 * 10 for user in users)
    values = []
    for x in histogram.keys():
        values.append(number_of_friends_by_interval(x, x+10))
    plt.bar(
        [
            x for x in histogram.keys()
        ],
        values,
        8
    )
    plt.axis([-5, 105, 0, 20])
    plt.xticks([10 * i for i in range(11)])
    plt.xlabel('#Age')
    plt.ylabel('#N° Friends')
    plt.show()

def media_idades(idades):
    return sum (idades) / (len(idades) -1)

def diferencas_em_relacao_a_media(idades):
    media = media_idades(idades)
    return [x - media for x in idades]

def soma_dos_quadrados(diferencas):
    return sum(x ** 2 for x in diferencas)

def variancia(idades):
    return soma_dos_quadrados(diferencas_em_relacao_a_media(idades)) / (
        len(idades) - 1
    )

def desvio_padrao(idades):
    return math.sqrt(variancia(idades))

def calcula_variancia_desvio(idade):
    idades = []
    for user in users:
        if user['age'] >= idade:
            idades.append(user["age"])
    print(f"Variancia:{variancia(idades)}")
    print(f"Desvio Padrao:{desvio_padrao(idades)}")



def main():
# 1 Escreva uma função que constrói um histograma   que mostra a quantidade de amigos quepessoas de cada sexo têm.
    # histograma_number_of_friends_by_genre()
# 2 Escreva uma função que constrói um histograma que mostra a quantidade de amigos que pessoas de cada idade têm.
    # histogram_number_of_friends_by_age();
# 3 Escreva uma função que calcula a variância e o desvio padrão da idade das pessoas do sexomasculino que tenham pelo menos 22 anos
    calcula_variancia_desvio(22)
main()