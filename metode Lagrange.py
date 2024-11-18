import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def lagrange_interpolation(x, x_data, y_data):
    def L(k, x):
        result = 1
        for i in range(len(x_data)):
            if i != k:
                result *= (x - x_data[i]) / (x_data[k] - x_data[i])
        return result

    result = 0
    for k in range(len(x_data)):
        result += y_data[k] * L(k, x)
    return result

# Testing Interpolasi Langrange
x_test = np.linspace(5, 40, 100)
y_test_lagrange = [lagrange_interpolation(x, x_data, y_data) for x in x_test]

# Plot hasil interpolasi Lagrange menggunakan matplotlib
plt.figure(figsize=(12, 6))
plt.plot(x_data, y_data, 'o', label='Data')
plt.plot(x_test, y_test_lagrange, label='Interpolasi Polinom Lagrange')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)
plt.show()