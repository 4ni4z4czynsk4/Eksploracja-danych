#Część 1: Funkcja add_list

def add_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Obie listy muszą mieć tę samą długość")
    return [x + y for x, y in zip(list1, list2)]

# Przykład użycia funkcji add_list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_list = add_list(list1, list2)
print(f"Wynik dodawania list: {result_list}")


#Część 2: Operacje na tablicach numpy

import numpy as np

# Tworzenie dwóch tablic numpy
array1 = np.array([1.5, 2.5, 3.5])
array2 = np.array([4.5, 5.5, 6.5])

# Dodawanie element po elemencie
result_array = array1 + array2
print(f"Wynik dodawania tablic numpy: {result_array}")
