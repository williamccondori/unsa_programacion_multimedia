import cv2 as cv
import math as mt
import copy as cp
import numpy as np
from skimage.feature import hog
from skimage import data, exposure
import helpers.nombres_helper as hnm
import helpers.calculo_helper as hca
import helpers.numpy_helper as hnp
import helpers.opencv_helper as hcv


class OtherOperator(object):
    def fourier(self, imagen):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        imagen_final = []
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def wavelets(self, imagen):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        imagen_final = []
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def border_detection(self, imagen):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        imagen_final = []
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def sift(self, imagen):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        sift = cv.SIFT()
        gray = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        kp = sift.detect(gray, None)
        imagen_final = cv.drawKeypoints(gray, kp)
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def hog(self, imagen, orientacion=0):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        fd, imagen_final = hog(imagen, orientations=orientacion, pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1), visualise=True, block_norm='L2-Hys')
        print(fd)
        imagen_final = exposure.rescale_intensity(imagen_final, in_range=(0, 10))
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, 255 * imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def selective_search(self, imagen):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        imagen_final = []
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)
