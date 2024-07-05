numero_vlan = input("Ingrese Numero de VLAN: ")

if numero_vlan.isdigit():
 numero_vlan = int(numero_vlan)
if numero_vlan >=1 and numero_vlan <=1005:
 print("Numero de vlan de Rango normal")
elif numero_vlan >=1006 and numero_vlan <=4094:
 print("Numero de vlan de rango extendido")
