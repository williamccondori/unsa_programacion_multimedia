import numpy as np
import cv2 as cv

def main():
    pass

def obtener_imagen(archivo):
    archivo_leido = archivo.read()
    imagen_numpy = np.fromstring(archivo_leido, np.uint8)
    imagen = cv.imdecode(imagen_numpy, cv.IMREAD_GRAYSCALE)
    return imagen

if __name__ == '__main__':
    main()
