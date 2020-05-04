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

for user in users:
    print (f'{user["id"]}: {friends_of_user (user)}')