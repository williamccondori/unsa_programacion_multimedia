import cv2 as cv
import math as mt
import copy as cp
import numpy as np
import helpers.nombres_helper as hnm
import helpers.calculo_helper as hca
import helpers.numpy_helper as hnp
import helpers.opencv_helper as hcv


class LogicalOperator(object):
    def invert(self, imagen, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        for i in range(len(imagen)):
            for j in range(len(imagen[i])):
                resultado = 255 - imagen[i, j]
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

    def and_(self, imagen, imagen_dos=None, valor=0, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        if imagen_dos is None:
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] & valor
                    if limitar:
                        resultado = hca.limitar(resultado)
                    imagen[i, j] = resultado
            imagen_final = imagen
        else:
            imagen = hcv.normalizar_imagen(imagen)
            imagen_dos = hcv.normalizar_imagen(imagen_dos)
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] & imagen_dos[i, j]
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

    def or_(self, imagen, imagen_dos=None, valor=0, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        if imagen_dos is None:
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] | valor
                    if limitar:
                        resultado = hca.limitar(resultado)
                    imagen[i, j] = resultado
            imagen_final = imagen
        else:
            imagen = hcv.normalizar_imagen(imagen)
            imagen_dos = hcv.normalizar_imagen(imagen_dos)
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] | imagen_dos[i, j]
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
