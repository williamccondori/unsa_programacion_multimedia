import cv2 as cv
import math as mt
import copy as cp
import numpy as np
import helpers.nombres_helper as hnm
import helpers.calculo_helper as hca
import helpers.numpy_helper as hnp
import helpers.opencv_helper as hcv


class AritmethicOperator(object):
    def pixel_adition(self, imagen, imagen_dos=None, valor=0, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        if imagen_dos is None:
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] + valor
                    if limitar:
                        resultado = hca.limitar(resultado)
                    imagen[i, j] = resultado
            imagen_final = imagen
        else:
            imagen = hcv.normalizar_imagen(imagen)
            imagen_dos = hcv.normalizar_imagen(imagen_dos)
            print(len(imagen))
            print(len(imagen_dos))
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] + imagen_dos[i, j]
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

    def pixel_substraction(self, imagen, imagen_dos=None, valor=0, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        if imagen_dos is None:
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] - valor
                    if limitar:
                        resultado = hca.limitar(resultado)
                    imagen[i, j] = resultado
            imagen_final = imagen
        else:
            imagen = hcv.normalizar_imagen(imagen)
            imagen_dos = hcv.normalizar_imagen(imagen_dos)
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] - imagen_dos[i, j]
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

    def pixel_multiplication(self, imagen, imagen_dos=None, valor=0, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        if imagen_dos is None:
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] * valor
                    if limitar:
                        resultado = hca.limitar(resultado)
                    imagen[i, j] = resultado
            imagen_final = imagen
        else:
            imagen = hcv.normalizar_imagen(imagen)
            imagen_dos = hcv.normalizar_imagen(imagen_dos)
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] * imagen_dos[i, j]
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

    def pixel_division(self, imagen, imagen_dos=None, valor=0, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        if imagen_dos is None:
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] / valor
                    if limitar:
                        resultado = hca.limitar(resultado)
                    imagen[i, j] = resultado
            imagen_final = imagen
        else:
            imagen = hcv.normalizar_imagen(imagen)
            imagen_dos = hcv.normalizar_imagen(imagen_dos)
            for i in range(len(imagen)):
                for j in range(len(imagen[i])):
                    resultado = imagen[i, j] / imagen_dos[i, j]
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

    def blending(self, imagen, imagen_dos, valor=0, limitar=True):
        nombre_imagen = hnm.generar_nombre_imagen()
        imagen_inicial = cp.copy(imagen)
        """
        Inicio del algoritmo
        """
        imagen = hcv.normalizar_imagen(imagen)
        imagen_dos = hcv.normalizar_imagen(imagen_dos)
        for i in range(len(imagen)):
            for j in range(len(imagen[i])):
                resultado = (valor * imagen[i, j]) + ((1 - valor) * imagen_dos[i, j])
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
