import sys
import time
import random
import actividad8_Marcos_Herrero as act

p = 11
d = 10001
f = [random.randint(0,p-1) for i in range(d)] + [random.randint(1,p-1)]
g = [random.randint(0,p-1) for i in range(d)] + [random.randint(1,p-1)]
print("Ini")
h2 = act.mult_pol_mod(f,g,p)
print("Fin")
