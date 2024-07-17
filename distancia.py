import googlemaps
from datetime import datetime

# Clave API de Google Maps (debes obtener una propia en Google Cloud)
API_KEY = 'TU_CLAVE_API_AQUI'

gmaps = googlemaps.Client(key=API_KEY)

def obtener_datos_viaje(origen, destino, modo):
    now = datetime.now()
    directions_result = gmaps.directions(origen,
                                         destino,
                                         mode=modo,
                                         departure_time=now)
    if directions_result:
        return directions_result[0]
    else:
        return None

def mostrar_narrativa_viaje(data):
    distance_km = data['legs'][0]['distance']['value'] / 1000
    distance_mi = distance_km * 0.621371
    duration = data['legs'][0]['duration']['text']
    
    print("\n--- Detalles del Viaje ---")
    print(f"Distancia: {distance_km:.2f} km / {distance_mi:.2f} millas")
    print(f"Duración del viaje: {duration}")
    print("Narrativa del viaje:")
    
    for step in data['legs'][0]['steps']:
        print(step['html_instructions'].replace('<b>', '').replace('</b>', '').replace('<div style="font-size:0.9em">', ' ').replace('</div>', ''))

def main():
    while True:
        print("\nIngrese 's' para salir en cualquier momento.")
        origen = input("Ciudad de Origen: ")
        if origen.lower() == 's':
            break
        destino = input("Ciudad de Destino: ")
        if destino.lower() == 's':
            break
        
        print("Seleccione el medio de transporte:")
        print("1. Conducción")
        print("2. Caminata")
        print("3. Bicicleta")
        print("4. Transporte público")
        
        opcion = input("Opción: ")
        if opcion.lower() == 's':
            break
        
        modos_transporte = {
            "1": "driving",
            "2": "walking",
            "3": "bicycling",
            "4": "transit"
        }
        
        modo = modos_transporte.get(opcion)
        
        if not modo:
            print("Opción no válida. Inténtelo de nuevo.")
            continue
        
        datos_viaje = obtener_datos_viaje(origen, destino, modo)
        
        if datos_viaje:
            mostrar_narrativa_viaje(datos_viaje)
        else:
            print("No se pudieron obtener los datos del viaje. Inténtelo de nuevo.")
        
if __name__ == "__main__":
    main()

