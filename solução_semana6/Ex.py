from collections import Counter
from collections import defaultdict
from matplotlib import pyplot as plt

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends (user):
    return len(user["friends"])

def name_of_users (user):
    return user["name"]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"),(5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"),  
]

salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)
]

tenure_and_account_type = [
    (0.7, 'paid'),
    (1.9, 'unpaid'),
    (2.5, 'paid'),
    (4.2, 'unpaid'),
    (6, 'unpaid'),
    (6.5, 'unpaid'),
    (7.5, 'unpaid'),
    (8.1, 'unpaid'),
    (8.7, 'paid'),
    (10, 'paid')
]


# Ex 1 - Construa um gráfico de linha que mostra o número de amigos por usuário.
# num_friends = [number_of_friends(user) for user in users]
# names = [name_of_users(user) for user in users]
# xs = [i for i, _ in enumerate(users)]
# plt.plot(xs, num_friends, color="green", marker='o', linestyle="solid")
# plt.ylabel("Num of Friends")
# plt.xlabel("Users")
# plt.xticks([i for i, _ in enumerate(users)], names)

# plt.show()


# 2 Construa um gráfico de dispersão envolvendo salário e tempo de experiência.
# salaries = []
# tenures = []
# for s, t in salaries_and_tenures:
#     salaries.append(s)
#     tenures.append(t)

# names = [name_of_users(user) for user in users]

# plt.scatter (salaries, tenures);

# for name, salarie, tenure in zip (names, salaries, tenures):
#     plt.annotate(
#         name,
#         xy = (salarie, tenure),
#         xytext = (5, -5),
#         textcoords ="offset points"
#     ) 

# plt.title ("Salario vs. Tempo de Experiencia")
# plt.xlabel ("Valor do salario")
# plt.ylabel ("Tempo de experiencia")

# plt.show()

# 3 Construa um histograma envolvendo dados de pagantes e não pagantes.
# account_types = Counter([account_type for _ , account_type in tenure_and_account_type])
# plt.bar(['Pagantes', 'Não Pagantes'], [account_types['paid'], account_types['unpaid']])
# plt.xticks(['Pagantes', 'Não Pagantes'])
# plt.ylabel("Numero de Usuarios")

# plt.show()

# 4  Construa um histograma de palavras em interesses. 
# Por exemplo, a palavra learning podeaparecer em machine learning e em deep learning. 
# Quebre cada interesse em palavras para fazera contagem e montar o histograma.
# def has_space (s):
#     if (' ' in s):
#         return s.split()
#     else:
#         return s

# interests_mentions = [interest for _, interest in interests]

# word_mentions = []
# for interest in interests_mentions:
#     split = has_space(interest)
#     if (not (isinstance(split, str))):
#         for word in split:
#             word_mentions.append(word)
#     else:
#         word_mentions.append(split)

# print(dict(Counter(word_mentions)))

# words = []
# mentions = []
# for i, j in dict(Counter(word_mentions)).items():
#     words.append(i)
#     mentions.append(j)


# xs = [i for i, _ in enumerate(words)]
# plt.barh(xs, mentions)
# plt.xlabel("Num of Mentions")
# plt.ylabel("Words")
# plt.yticks([i for i, _ in enumerate(words)], words)

# plt.show()