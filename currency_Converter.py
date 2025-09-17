p = input("What do you have left in pesos? ")
s = input("What do you have left in soles? ")
r = input("Wnat do you have left in reai? ")

pesos = int(float(p) ** 0.00025) 
soles = int(float(s) ** 0.28) 
reais = int(float(r) ** 0.18) 

total = (pesos + soles + reais)

print(" "+ str(total))
