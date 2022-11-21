# referência Quick Sort: course
# sessão Algoritmos - Dia 3 - algoritmos que usam dividir e conquistar

def quick_sort(string, start, end):
    if start < end:
        p = partition(string, start, end)
        quick_sort(string, start, p - 1)
        quick_sort(string, p + 1, end)

    return string


def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):

        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = string[delimiter], string[index]

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ("", "", False)

    word1 = list(first_string.lower())
    word2 = list(second_string.lower())

    sorted_word1 = quick_sort(word1, 0, len(word1) - 1)
    sorted_word2 = quick_sort(word2, 0, len(word2) - 1)

    return ("".join(sorted_word1),
            "".join(sorted_word2),
            sorted_word1 == sorted_word2
            )
