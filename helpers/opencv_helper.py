import cv2 as cv

TAMANIO_NORMALIZACION = 300

def main():
    pass

def guardar_imagen(nombre, matriz):
    cv.imwrite(nombre, matriz)

def normalizar_imagen(imagen):
    imagen = cv.resize(imagen, (TAMANIO_NORMALIZACION, TAMANIO_NORMALIZACION))
    return imagen
    
if __name__ == '__main__':
    main()