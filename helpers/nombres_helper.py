import datetime

CARPETA = "static/images/"
EXTENSION = ".jpg"

def main():
    pass

def generar_nombre_imagen():
    fecha_hora = datetime.datetime.now()
    anio = str(fecha_hora.year)
    mes = str(fecha_hora.month)
    dia = str(fecha_hora.day)
    hora = str(fecha_hora.hour)
    minuto = str(fecha_hora.minute)
    segundo = str(fecha_hora.second)
    return anio + mes + dia + hora + minuto + segundo

def ontener_nombre_archivo(nombre_imagen, carpeta=False):
    if carpeta:
        return CARPETA + nombre_imagen + EXTENSION
    else:
        return nombre_imagen + EXTENSION

if __name__ == '__main__':
    main()