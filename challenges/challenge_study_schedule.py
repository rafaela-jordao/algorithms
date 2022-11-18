# permanence_period = lista de tuplas onde é armazenado os dados de entrada e saída de estudantes.
# cada tupla representa o período de permanência de uma pessoa estudante no sistema com seu horário de entrada e de saída.
# Nos arrays temos 6 estudantes:
# estudante             1       2       3       4       5       6
# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

# Req. 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

def study_schedule(permanence_period, target_time):
    count = 0

    for index in permanence_period:
        try:
            if index[0] <= target_time <= index[1]:
                count += 1
        except TypeError:
            return None

    return count

