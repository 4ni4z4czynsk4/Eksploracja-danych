import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładów normalnych (μ, σ)
params = [
    (0, 1),
    (0, 2),
    (2, 1)
]

# Liczba próbek dla każdego rozkładu
n = 10000

# Ustawienia wykresu
plt.figure(figsize=(10, 6))

# Generowanie danych i rysowanie histogramów
for mu, sigma in params:
    data = np.random.normal(mu, sigma, n)
    plt.hist(
        data,
        bins=50,
        alpha=0.6,
        density=True,
        label=f'μ={mu}, σ={sigma}'
    )

# Opisy osi i tytuł
plt.xlabel('Wartości')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.title('Histogramy rozkładów normalnych dla różnych μ i σ')

# Legenda i siatka
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Wyświetlenie wykresu
plt.show()
