import matplotlib.pyplot as plt
import numpy as np

# Generowanie danych
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = 2 * np.sin(x)

# Tworzenie wykresów obok siebie
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1) 
plt.plot(x, y1, color='blue')
plt.ylim(-2.1, 2.1)
plt.title('y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(1, 2, 2)  
plt.plot(x, y2, color='red')
plt.ylim(-2.1, 2.1)
plt.title('y = 2*sin(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()  
plt.show()
