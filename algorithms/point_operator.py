import cv2 as cv
import math as mt
import copy as cp
import numpy as np
import helpers.nombres_helper as hnm
import helpers.calculo_helper as hca
import helpers.numpy_helper as hnp
import helpers.opencv_helper as hcv


class PointOperator(object):
    def thresholding(self, imagen, valor=127, tipo=0):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        ret, imagen_final = cv.threshold(imagen, valor, hca.MAX_VALUE, tipo)
        print(ret)
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def contrast_stretching(self, imagen, valor_minimo=0, valor_maximo=255, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        for i in range(len(imagen)):
            for j in range(len(imagen[i])):
                resultado = ((imagen[i, j] - valor_minimo) /
                             (valor_maximo - valor_minimo)) * hca.MAX_VALUE
                if limitar:
                    resultado = hca.limitar(resultado)
                imagen[i, j] = resultado
        imagen_final = imagen
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def histogram_equalization(self, imagen):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        imagen_final = cv.equalizeHist(imagen)
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def logarithm(self, imagen, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        c = hca.MAX_VALUE / (mt.log(1 + imagen.max()))
        for i in range(len(imagen)):
            for j in range(len(imagen[i])):
                resultado = c * (mt.log(1 + imagen[i, j]))
                if limitar:
                    resultado = hca.limitar(resultado)
                imagen[i, j] = resultado
        imagen_final = imagen
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def exponential(self, imagen, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        c = hca.MAX_VALUE / (mt.log(1 + imagen.max()))
        for i in range(len(imagen)):
            for j in range(len(imagen[i])):
                resultado = c * (mt.pow(1.01, imagen[i, j]) - 1)
                if limitar:
                    resultado = hca.limitar(resultado)
                imagen[i, j] = resultado
        imagen_final = imagen
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)

    def raise_to_power(self, imagen, constante=0, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        r = float(0.5)
        for i in range(len(imagen)):
            for j in range(len(imagen[i])):
                resultado = constante * (mt.pow(imagen[i, j], r))
                if limitar:
                    resultado = hca.limitar(resultado)
                imagen[i, j] = resultado
        imagen_final = imagen
        """
        Fin del algoritmo
        """
        hcv.guardar_imagen(hnm.ontener_nombre_archivo(
            nombre_imagen, True), hnp.unir_imagen(imagen_inicial, imagen_final))
        return hnm.ontener_nombre_archivo(nombre_imagen)
