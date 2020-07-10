import random
from collections import Counter
 
import math
 
 
class Pessoa:
    def __init__(self, idade, sexo, salario, intencao_de_voto):
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
        self.intencao_de_voto = intencao_de_voto
 
    def __str__(self):
        return f"idade: {self.idade}, sexo: {self.sexo}, salario: {self.salario}, Intenção de voto: {self.intencao_de_voto}"
 
    def __eq__(self, other):
        return self.intencao_de_voto == other.intencao_de_voto
 
    def __hash__(self):
        return 1
 
 
def gera_base(n):
    l = []
    for i in range(n):
        idade = random.randint(18, 35)
        sexo = random.choice(["M", "F"])
        salario = 1200 + random.random() * 1300
        intencao_de_voto = random.choice(["Haddad", "Bolsonaro"])
        p = Pessoa(idade, sexo, salario, intencao_de_voto)
        l.append(p)
    return l
 
 
def rotulo_de_maior_frequencia(pessoas):
    frequencias = Counter(pessoas)
    mais_frequentes = frequencias.most_common(1)
    return mais_frequentes[0][0]
 
 
def rotulo_de_maior_frequencia_sem_empate(pessoas):
    frequencias = Counter(pessoas)
    rotulo, frequencia = frequencias.most_common(1)[0]
    qtde_de_mais_frequentes = len(
        [count for count in frequencias.values() if count == frequencia]
    )
    if qtde_de_mais_frequentes == 1:
        return rotulo
    return rotulo_de_maior_frequencia_sem_empate(pessoa[:-1])
 
 
def rotulo_de_maior_frequencia_sem_empate_teste():
    base = gera_base(10)
    print(
        "====================================Base======================================"
    )
    for p in base:
        print(p)
    print(
        "====================================Rótulo de maior frequência======================================"
    )
    print(rotulo_de_maior_frequencia_sem_empate(base))
 
 
def distance(p1, p2):
    i = math.pow((p1.idade - p2.idade), 2)
    s = math.pow((500 if p1.sexo == "M" else 0) - (500 if p2.sexo == "M" else 0), 2)
    sal = math.pow((p1.salario - p2.salario), 2)
    return math.sqrt(i + s + sal)
 
 
def knn(k, observacoes_rotuladas, nova_observacao):
    ordenados_por_distancia = sorted(
        observacoes_rotuladas, key=lambda obs: distance(obs, nova_observacao)
    )
    k_mais_proximos = ordenados_por_distancia[:k]
    resultado = rotulo_de_maior_frequencia(k_mais_proximos)
    return resultado.intencao_de_voto
 
 
def knn_test():
    base = gera_base(10)
    print("===================Base===================")
    for p in base:
        print(p)
    print("==================Resultado=================")
    p = Pessoa(19, "M", 1700, None)
    p.intencao_de_voto = knn(5, base, p)
    print(p)

def leave_one_out():   
    base = gera_base(100)
    match = 0
    not_match = 0

    for user in base:
        intencao_de_voto = knn(5, base[:-1], user)
        if(intencao_de_voto != user.intencao_de_voto):
            not_match += 1
        else:
            match += 1
        
    print('KNN Executed: ', not_match + match)
    match = (match / len(base)) * 100
    not_match = not_match / len(base) * 100

    print(f'Match: {match}% | Not Match {not_match}%')
 
 
def main():
    # knn_test()
    leave_one_out()
    # rotulo_de_maior_frequencia_sem_empate_teste()
 
 
main()