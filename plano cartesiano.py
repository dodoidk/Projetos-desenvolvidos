print ("Plano cartesiano")
import math
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))
d = math.hypot(x2 - x1, y2 - y1)
print(f"A distância entre os pontos é: {d}")

