'''
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 '''
 
import cv2
import requests
from fractions import Fraction

url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
IMAGE_NAME = "image.png"


def download_image(url_image: str):
    response = requests.get(url_image)

    # Escribe un archivo IMAGE_NAME.
    with open(IMAGE_NAME, "wb") as file:
        file.write(response.content)

def ratio_net_image(url_image: str):
    # Descarga la imagen
    download_image(url_image)

    # Si la imagen puede ser procesada por Open-CV se procesa la imagen.
    if cv2.haveImageReader(IMAGE_NAME):
        # Lee la imagen desde el fichero
        img = cv2.imread(IMAGE_NAME)

        # Extrae el alto y ancho.
        dimension_image: tuple = img.shape #shape devuelve (ancho, largo, profundidad de pixeles (3: 3 bits de color por pixel))
        height: int = dimension_image[0]
        width: int = dimension_image[1]

        # Determina el ratio de la imagen como una fracción.
        fraction: tuple = Fraction(width, height).as_integer_ratio()
        aspect_ratio: str = f"{fraction[0]}:{fraction[1]}"

        print(f"La relación de aspecto de la imagen es: {aspect_ratio}. Sus dimensiones son: {width}x{height} px.")

    else:
        print("La imagen no puede ser procesada, compruebe que sea la URL de una imagen.")


ratio_net_image(url)