import numpy as np
import matplotlib.pyplot as plt
import calculator

# --- Nhập biểu thức hàm số ---
expr = input("Nhập biểu thức hàm số f(x) = ")

# --- Khoảng vẽ ---
x_min = float(input("Nhập giá trị x_min: "))
x_max = float(input("Nhập giá trị x_max: "))
dx = 0.001

# --- Tính giá trị ---
x_values = []
y_values = []

x = x_min
while x <= x_max:
    y = calculator.calc(expr.replace("x", f"({x})"))
    x_values.append(x)
    y_values.append(y)
    x += dx

# --- Vẽ đường liền ---
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, color='red', linewidth=1)
plt.title(f"Đồ thị f(x) = {expr}")
plt.xlabel("x")
plt.ylabel("y")

# --- Giữ tỉ lệ hình hợp lý ---
# Giới hạn x
x_min, x_max = min(x_values), max(x_values)
dx = (x_max - x_min) * 0.1


# Giới hạn y
y_min, y_max = min(y_values), max(y_values)
dy = (y_max - y_min) * 0.1


#Cho cả hai trục có cùng tỉ lệ
bounded_below = min(y_min - dy, x_min - dx)
bounded_above = max(y_max + dy, x_max + dx)
plt.xlim(bounded_below, bounded_above)
plt.ylim(bounded_below, bounded_above)

# Giữ tỉ lệ 1:1
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)

plt.show()
