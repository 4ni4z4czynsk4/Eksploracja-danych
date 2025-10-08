# Część 1: Funkcje do obliczania średniej i mediany

def calculate_mean(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total_sum / count


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return 0
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid_index]
    else:
        return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2


# Część 2: Porównanie z numpy

import numpy as np

life_exp_top_15 = [81.8, 81, 82.6, 83, 81.8, 84.3, 82.8, 81.9, 82.2, 82, 82.7,
                   79.8, 83.3, 82]

# Wyniki z numpy
mean_with_numpy = np.mean(life_exp_top_15)
median_with_numpy = np.median(life_exp_top_15)

# Wyniki z własnych funkcji
mean_custom = calculate_mean(life_exp_top_15)
median_custom = calculate_median(life_exp_top_15)

# Wyświetlenie porównania
print(f"Średnia (numpy): {mean_with_numpy}")
print(f"Średnia (calculate_mean): {mean_custom}")

print(f"Mediana (numpy): {median_with_numpy}")
print(f"Mediana (calculate_median): {median_custom}")
