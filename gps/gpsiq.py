import requests
import time

# Tu clave de API de LocationIQ
API_KEY = 'pk.7b2c8d29e5eded289dd39b94a03973e5'

def obtener_ubicacion_ip():
    """Obtiene la ubicación basada en la IP pública."""
    url = 'https://ipinfo.io/json'
    respuesta = requests.get(url)
    datos = respuesta.json()
    if 'loc' in datos:
        lat, lon = map(float, datos['loc'].split(','))
        return lat, lon
    else:
        return None

def obtener_direccion(lat, lon):
    """Obtiene la dirección basada en las coordenadas."""
    url = f'https://us1.locationiq.com/v1/reverse.php'
    params = {
        'key': API_KEY,
        'lat': lat,
        'lon': lon,
        'format': 'json'
    }
    respuesta = requests.get(url, params=params)
    datos = respuesta.json()
    if 'address' in datos:
        return datos['address']
    else:
        return None

def mostrar_ubicacion():
    """Obtiene y muestra la ubicación actual en tiempo real."""
    while True:
        ubicacion = obtener_ubicacion_ip()
        if ubicacion:
            lat, lon = ubicacion
            direccion = obtener_direccion(lat, lon)
            print(f'Ubicación actual:\nLatitud: {lat}\nLongitud: {lon}')
            if direccion:
                print('Dirección:')
                for clave, valor in direccion.items():
                    print(f'  {clave}: {valor}')
            else:
                print('Dirección no disponible.')
        else:
            print('No se pudo obtener la ubicación.')

        # Esperar 60 segundos antes de actualizar
        time.sleep(60)

if __name__ == '__main__':
    mostrar_ubicacion()
