from flask import Flask, render_template, request, send_file
from algorithms.point_operator import PointOperator
from algorithms.aritmethic_operator import AritmethicOperator
from algorithms.logical_operator import LogicalOperator
from algorithms.geometric_operator import GeometricOperator
from algorithms.filter_operator import FilterOperator
from algorithms.morphology_operator import MorphologyOperator
from algorithms.other_operator import OtherOperator
import helpers.image_helper as him

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder="static"
)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/point_operator/thresholding', methods=['POST', 'GET'])
def thresholding():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        tipo = int(request.form.get('tipo'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = PointOperator().thresholding(imagen, float(valor), tipo)
    return render_template('point_operator/thresholding.html', url_imagen=respuesta)

@app.route('/point_operator/contrast_stretching', methods=['POST', 'GET'])
def contrast_stretching():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor_minimo = int(request.form.get('valor_minimo'))
        valor_maximo = int(request.form.get('valor_maximo'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = PointOperator().contrast_stretching(imagen, valor_minimo, valor_maximo)
    return render_template('point_operator/contrast_stretching.html', url_imagen=respuesta)

@app.route('/point_operator/histogram_equalization', methods=['POST', 'GET'])
def histogram_equalization():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = PointOperator().histogram_equalization(imagen)
    return render_template('point_operator/histogram_equalization.html', url_imagen=respuesta)

@app.route('/point_operator/logarithm', methods=['POST', 'GET'])
def logarithm():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = PointOperator().logarithm(imagen)
    return render_template('point_operator/logarithm.html', url_imagen=respuesta)

@app.route('/point_operator/exponential', methods=['POST', 'GET'])
def exponential():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = PointOperator().exponential(imagen)
    return render_template('point_operator/exponential.html', url_imagen=respuesta)

@app.route('/point_operator/raise_to_power', methods=['POST', 'GET'])
def raise_to_power():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        constante = int(request.form.get('constante'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = PointOperator().raise_to_power(imagen, constante)
    return render_template('point_operator/raise_to_power.html', url_imagen=respuesta)

@app.route('/aritmethic_operator/pixel_adition', methods=['POST', 'GET'])
def pixel_adition():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            valor = int(0)
            imagen_dos = None
            imagen = him.obtener_imagen(archivo)
            archivo_dos = request.files.get('imagen_dos')
            if (archivo_dos is None):
                valor = int(request.form.get('valor'))
            else:
                imagen_dos = him.obtener_imagen(archivo_dos)
            respuesta = AritmethicOperator().pixel_adition(imagen, imagen_dos, valor)
    return render_template('aritmethic_operator/pixel_adition.html', url_imagen=respuesta)

@app.route('/aritmethic_operator/pixel_substraction', methods=['POST', 'GET'])
def pixel_substraction():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            valor = int(0)
            imagen_dos = None
            imagen = him.obtener_imagen(archivo)
            archivo_dos = request.files.get('imagen_dos')
            if (archivo_dos is None):
                valor = int(request.form.get('valor'))
            else:
                imagen_dos = him.obtener_imagen(archivo_dos)
            respuesta = AritmethicOperator().pixel_substraction(imagen, imagen_dos, valor)
    return render_template('aritmethic_operator/pixel_substraction.html', url_imagen=respuesta)

@app.route('/aritmethic_operator/pixel_multiplication', methods=['POST', 'GET'])
def pixel_multiplication():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            valor = int(0)
            imagen_dos = None
            imagen = him.obtener_imagen(archivo)
            archivo_dos = request.files.get('imagen_dos')
            if (archivo_dos is None):
                valor = int(request.form.get('valor'))
            else:
                imagen_dos = him.obtener_imagen(archivo_dos)
            respuesta = AritmethicOperator().pixel_multiplication(imagen, imagen_dos, valor)
    return render_template('aritmethic_operator/pixel_multiplication.html', url_imagen=respuesta)

@app.route('/aritmethic_operator/pixel_division', methods=['POST', 'GET'])
def pixel_division():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            valor = int(0)
            imagen_dos = None
            imagen = him.obtener_imagen(archivo)
            archivo_dos = request.files.get('imagen_dos')
            if (archivo_dos is None):
                valor = int(request.form.get('valor'))
            else:
                imagen_dos = him.obtener_imagen(archivo_dos)
            respuesta = AritmethicOperator().pixel_division(imagen, imagen_dos, valor)
    return render_template('aritmethic_operator/pixel_division.html', url_imagen=respuesta)

@app.route('/aritmethic_operator/blending', methods=['POST', 'GET'])
def blending():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        archivo_dos = request.files.get('imagen_dos')
        if archivo is None or archivo_dos is None:
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            imagen_dos = him.obtener_imagen(archivo_dos)
            respuesta = AritmethicOperator().blending(imagen, imagen_dos, valor)
    return render_template('aritmethic_operator/blending.html', url_imagen=respuesta)

@app.route('/logical_operator/invert', methods=['POST', 'GET'])
def invert():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = LogicalOperator().invert(imagen)
    return render_template('logical_operator/invert.html', url_imagen=respuesta)

@app.route('/logical_operator/and', methods=['POST', 'GET'])
def and_():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            valor = int(0)
            imagen_dos = None
            imagen = him.obtener_imagen(archivo)
            archivo_dos = request.files.get('imagen_dos')
            if (archivo_dos is None):
                valor = int(request.form.get('valor'))
            else:
                imagen_dos = him.obtener_imagen(archivo_dos)
            respuesta = LogicalOperator().and_(imagen, imagen_dos, valor)
    return render_template('logical_operator/and.html', url_imagen=respuesta)

@app.route('/logical_operator/or', methods=['POST', 'GET'])
def or_():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            valor = int(0)
            imagen_dos = None
            imagen = him.obtener_imagen(archivo)
            archivo_dos = request.files.get('imagen_dos')
            if (archivo_dos is None):
                valor = int(request.form.get('valor'))
            else:
                imagen_dos = him.obtener_imagen(archivo_dos)
            respuesta = LogicalOperator().or_(imagen, imagen_dos, valor)
    return render_template('logical_operator/or.html', url_imagen=respuesta)

@app.route('/geometric_operator/translate', methods=['POST', 'GET'])
def translate():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor_x = int(request.form.get('valor_x'))
        valor_y = int(request.form.get('valor_y'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = GeometricOperator().translate(imagen, valor_x, valor_y)
    return render_template('geometric_operator/translate.html', url_imagen=respuesta)

@app.route('/geometric_operator/scale', methods=['POST', 'GET'])
def scale():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = GeometricOperator().scale(imagen, valor)
    return render_template('geometric_operator/scale.html', url_imagen=respuesta)

@app.route('/geometric_operator/rotate', methods=['POST', 'GET'])
def rotate():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        grados = int(request.form.get('grados'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = GeometricOperator().rotate(imagen, grados)
    return render_template('geometric_operator/rotate.html', url_imagen=respuesta)

@app.route('/geometric_operator/shear', methods=['POST', 'GET'])
def shear():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = float(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = GeometricOperator().shear(imagen, valor)
    return render_template('geometric_operator/shear.html', url_imagen=respuesta)

@app.route('/geometric_operator/twirl', methods=['POST', 'GET'])
def twirl():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = GeometricOperator().twirl(imagen, valor)
    return render_template('geometric_operator/twirl.html', url_imagen=respuesta)

@app.route('/filter_operator/mean', methods=['POST', 'GET'])
def mean():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = FilterOperator().mean(imagen, valor)
    return render_template('filter_operator/mean.html', url_imagen=respuesta)

@app.route('/filter_operator/median', methods=['POST', 'GET'])
def median():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = FilterOperator().median(imagen, valor)
    return render_template('filter_operator/median.html', url_imagen=respuesta)

@app.route('/filter_operator/gaussian', methods=['POST', 'GET'])
def gaussian():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = FilterOperator().gaussian(imagen, valor)
    return render_template('filter_operator/gaussian.html', url_imagen=respuesta)

@app.route('/filter_operator/conservative', methods=['POST', 'GET'])
def conservative():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        tamanio = int(request.form.get('tamanio'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = FilterOperator().conservative(imagen, valor, tamanio)
    return render_template('filter_operator/conservative.html', url_imagen=respuesta)

@app.route('/morphology_operator/erotion', methods=['POST', 'GET'])
def erotion():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = MorphologyOperator().erotion(imagen, valor)
    return render_template('morphology_operator/erotion.html', url_imagen=respuesta)

@app.route('/morphology_operator/dilation', methods=['POST', 'GET'])
def dilation():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = MorphologyOperator().dilation(imagen, valor)
    return render_template('morphology_operator/dilation.html', url_imagen=respuesta)

@app.route('/morphology_operator/opening', methods=['POST', 'GET'])
def opening():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = MorphologyOperator().opening(imagen, valor)
    return render_template('morphology_operator/opening.html', url_imagen=respuesta)

@app.route('/morphology_operator/closing', methods=['POST', 'GET'])
def closing():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        valor = int(request.form.get('valor'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = MorphologyOperator().closing(imagen, valor)
    return render_template('morphology_operator/closing.html', url_imagen=respuesta)

@app.route('/other_operator/hog', methods=['POST', 'GET'])
def hog():
    if request.method == 'GET':
        respuesta = None
    if request.method == 'POST':
        orientacion = int(request.form.get('orientacion'))
        archivo = request.files.get('imagen')
        if (archivo is None):
            respuesta = None
        else:
            imagen = him.obtener_imagen(archivo)
            respuesta = OtherOperator().hog(imagen, orientacion)
    return render_template('other_operator/hog.html', url_imagen=respuesta)

if __name__ == "__main__":
    app.run()
