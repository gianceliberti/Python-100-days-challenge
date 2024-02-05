# import requests

# parameters = {
#     "amount": 10,
#     "type": "boolean",
# }

# response = requests.get("https://opentdb.com/api.php", params=parameters)
# response.raise_for_status()
# data = response.json()
# question_data = data["results"]

import json
from urllib.request import urlopen
from urllib.parse import urlencode

# Definir los parámetros de la solicitud
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Codificar los parámetros en la URL
url = "https://opentdb.com/api.php?" + urlencode(parameters)

try:
    # Realizar la solicitud GET a la API
    with urlopen(url) as response:
        # Leer los datos de la respuesta y decodificarlos como JSON
        data = json.loads(response.read())

        # Obtener los datos de las preguntas
        question_data = data["results"]
        print(question_data)  # Esto es solo para verificar que las preguntas se han obtenido correctamente

except Exception as e:
    print("Error al obtener las preguntas:", e)
