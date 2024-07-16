# Script para determinar el rango de una VLAN

# Función para determinar el rango de VLAN
def determinar_rango_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "VLAN en el rango normal."
    elif 1006 <= vlan_id <= 4094:
        return "VLAN en el rango extendido."
    else:
        return "Número de VLAN fuera de rango."

# Solicitar al usuario que ingrese el número de VLAN
vlan_id = int(input("Por favor, ingrese el número de VLAN: "))

# Determinar y mostrar el rango de la VLAN
resultado = determinar_rango_vlan(vlan_id)
print(resultado)

