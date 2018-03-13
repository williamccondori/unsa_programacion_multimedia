import cv2 as cv
import math as mt
import copy as cp
import numpy as np
from skimage import io
from skimage import transform as tf
import helpers.nombres_helper as hnm
import helpers.calculo_helper as hca
import helpers.numpy_helper as hnp
import helpers.opencv_helper as hcv


class GeometricOperator(object):
    def translate(self, imagen, valor_x=0, valor_y=0):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        filas, columnas = imagen.shape
        M = np.matrix([[1, 0, valor_x], [0, 1, valor_y]], np.float)
        imagen_final = cv.warpAffine(imagen, M, (columnas, filas))
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def scale(self, imagen, valor=0):
        nombre_imagen = hnm.generar_nombre_imagen()
        """
        Inicio del algoritmo
        """
        imagen_final = cv.resize(
            imagen, None, fx=valor, fy=valor, interpolation=cv.INTER_CUBIC)
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), imagen_final)
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def rotate(self, imagen, grados=0):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        filas, columnas = imagen.shape
        M = cv.getRotationMatrix2D((columnas/2, filas/2), grados, 1)
        imagen_final = cv.warpAffine(imagen, M, (columnas, filas))
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def shear(self, imagen, value=0):
        nombre_imagen = hnm.generar_nombre_imagen()
        """
        Inicio del algoritmo
        """
        imagen_shear = tf.AffineTransform(shear=value)
        imagen_final = tf.warp(imagen, inverse_map=imagen_shear)
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), 255 * imagen_final)
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def twirl(self, imagen, valor=0):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        filas, columnas = imagen.shape
        width = float(filas)
        height = float(columnas)
        resultado = cp.copy(imagen)
        for i in range(int(width)):
            for j in range(int(height)):
                x = (j / height)-0.5
                y = (i / width)-0.5

                angulo = mt.atan2(y, x)
                radio = mt.sqrt((x * x) + (y * y))
                angulo += radio * (valor / 10.0)

                xr = ((radio * mt.sin(angulo)) + 0.5) * width
                yr = ((radio * mt.cos(angulo)) + 0.5) * height

                k = min(width - 1, max(0.0, xr))
                m = min(height - 1, max(0.0, yr))
                imagen[i, j] = resultado[int(k), int(m)]
        imagen_final = imagen
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)
