from collections import defaultdict

users = [
    {"id": 0, "name": "Hero", "genre": "M", "age": 18},
    {"id": 1, "name": "Dunn", "genre": "M", "age": 19},
    {"id": 2, "name": "Sue", "genre": "F", "age": 18},
    {"id": 3, "name": "Chi", "genre": "M", "age": 19},
    {"id": 4, "name": "Thor", "genre": "M", "age": 18},
    {"id": 5, "name": "Clive", "genre": "M", "age": 19},
    {"id": 6, "name": "Hicks", "genre": "M", "age": 18},
    {"id": 7, "name": "Devin", "genre": "M", "age": 19},
    {"id": 8, "name": "Kate", "genre": "F", "age": 18},
    {"id": 9, "name": "Klein", "genre": "M", "age": 19},
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 6), (6, 8), (7, 8), (8, 9)
]

genre_interest = [
    (0, 'F'), (1, 'F'), (2, 'M'), (3, 'BOTH'),
    (4, 'F'), (5, 'BOTH'), (6, 'NONE'), (7, 'F'), (8, 'M'), (9,'NONE')
]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Hadoop"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "Java"), (5, "Python"), (5, "R"),(5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"),  
]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def friends_of_user (user):
    m_friends = 0
    f_friends = 0
    for friend in user ["friends"]:
        if friend["genre"] == "M":
            m_friends += 1
        else:
            f_friends += 1
    return (m_friends, f_friends)

# for user in users:
#     print (f'{user["id"]}: {friends_of_user (user)}')

user_ids_by_genre_interest = defaultdict(list)
for user_id, interest in genre_interest:
    user_ids_by_genre_interest[interest].append(user_id)

genre_interests_by_user_id = defaultdict(list)

for user_id, interest in genre_interest:
    genre_interests_by_user_id[user_id].append(interest)

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def users_with_common_genre_interests (user):
    return set([
        interested_user_id
        for interest in genre_interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_genre_interest[interest]
        if interested_user_id != user["id"]
    ])

def users_with_common_interests (user):
    return set([
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    ])

def users_with_common_genre_interests_with_common_interests (user):
    return set([
        user_id
        for user_id in users_with_common_genre_interests (user)
        if user_id in users_with_common_interests(user)
    ])
# 2 Escreva uma função que faz sugestões de amizade de acordo com o atributo “interessado em”.
print (users_with_common_genre_interests(users[0]))

# 3 Escreva uma função que faz sugestões de amizade de acordo com o atributo “interessado em” ede acordo com interesses em comum.
print (users_with_common_genre_interests_with_common_interests(users[0]))