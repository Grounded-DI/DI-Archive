
import matplotlib.pyplot as plt
import numpy as np

def generate_ulam_spiral(size):
    spiral = np.zeros((size, size), dtype=int)
    x, y = size // 2, size // 2
    dx, dy = 0, -1
    n = 1
    for _ in range(size * size):
        if 0 <= x < size and 0 <= y < size:
            spiral[y, x] = n
        if (x == y) or (x < y and x + y == size - 1) or (x > y and x + y == size):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
        n += 1
    return spiral

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

size = 201
spiral = generate_ulam_spiral(size)
prime_mask = np.vectorize(is_prime)(spiral)

plt.figure(figsize=(8, 8))
plt.imshow(prime_mask, cmap='Greys', interpolation='none')
plt.title("Ulam Spiral – Prime Numbers on Diagonals")
plt.axis('off')
plt.tight_layout()
plt.show()
