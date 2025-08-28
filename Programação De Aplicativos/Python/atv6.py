import time
n = int(input("Qual número você deseja para a contagem regressiva? "))
for i in range(n, 0, -1):
    print(i)
    time.sleep(1)
print("BOOM EXPLODIU!")
