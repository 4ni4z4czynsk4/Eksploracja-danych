import time

def sum_for(n=1_000_000):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def sum_list_comprehension(n=1_000_000):
    return sum([i for i in range(1, n+1)])

def sum_builtin(n=1_000_000):
    return sum(range(1, n+1))

# Pomiar czasu wykonania każdej funkcji
start = time.time()
sum_for()
end = time.time()
print(f"Czas pętli for: {end - start:.6f} s")

start = time.time()
sum_list_comprehension()
end = time.time()
print(f"Czas list comprehension: {end - start:.6f} s")

start = time.time()
sum_builtin()
end = time.time()
print(f"Czas wbudowanej sum(): {end - start:.6f} s")
# Wnioski:
# 1. Najwolniejsza metoda to pętla for, ponieważ działa w czystym Pythonie.
# 2. List comprehension jest nieco szybsze, ale nadal musi utworzyć listę w pamięci.
# 3. Najszybsza jest wbudowana funkcja sum(range()), bo działa w C i nie tworzy listy.
