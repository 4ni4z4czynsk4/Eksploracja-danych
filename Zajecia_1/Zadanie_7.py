import numpy as np
import matplotlib.pyplot as plt

# Parametry rozkładów normalnych (μ, σ)
params = [
    (0, 1),
    (0, 2),
    (2, 1)
]

# Liczba próbek losowych
n = 10000

# Tworzymy figure z trzema wykresami (3 wiersze, 1 kolumna)
fig, axes = plt.subplots(3, 1, figsize=(8, 12))
fig.tight_layout(pad=5.0)

# Iteracja po wykresach i parametrach
for ax, (mu, sigma) in zip(axes, params):
    # 1. Dane losowe
    data = np.random.normal(mu, sigma, n)

    # 2. Analityczna gęstość Gaussa
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

    # 3. Histogram z danymi wygenerowanymi
    ax.hist(data, bins=50, density=True, alpha=0.6, label='Dane wygenerowane')

    # 4. Wykres funkcji analitycznej
    ax.plot(x, pdf, 'r-', lw=2, label='Gęstość analityczna')

    # 5. Tytuł z parametrami μ i σ
    ax.set_title(f'Rozkład normalny: μ = {mu}, σ = {sigma}')

    # 6. Etykiety osi
    ax.set_xlabel('Wartości')
    ax.set_ylabel('Gęstość')

    # 7. Legenda i siatka
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)

# Wyświetlenie wykresu
plt.show()
