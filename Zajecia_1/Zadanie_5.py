import numpy as np
import matplotlib.pyplot as plt

# 1. Definicja funkcji gęstości prawdopodobieństwa
def normal_pdf(x, mu, sigma):

  return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2))

# 2. Wizualizacja funkcji dla różnych parametrów
# Generowanie wartości x dla wykresu
x_values = np.linspace(-10, 10, 1000)

# Pary wartości mu i sigma
params = [(0, 1), (0, 2), (2, 1)]

plt.figure(figsize=(10, 6))

for mu, sigma in params:
  # Obliczanie wartości y dla danej pary mu i sigma
  y_values = normal_pdf(x_values, mu, sigma)
  # Rysowanie wykresu
  plt.plot(x_values, y_values, label=f'$\mu = {mu}, \sigma = {sigma}$')

# 3. Oznaczenia na wykresie
plt.title('Funkcja gęstości prawdopodobieństwa rozkładu normalnego')
plt.xlabel('x')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.legend()
plt.grid(True)
plt.show()
