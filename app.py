from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variable global para el estado del LED
led_status = "OFF"

@app.route('/')
def home():
    return render_template('index.html', led_status=led_status)

@app.route('/programado')
def programado():
    return render_template('programado.html')

@app.route('/toggle_led', methods=['POST'])
def toggle_led():
    global led_status
    led_status = "ON" if led_status == "OFF" else "OFF"
    return jsonify(status=led_status)

@app.route('/get_status', methods=['GET'])
def get_status():
    global led_status
    return led_status

if __name__=='__main__':
    app.run(debug=True)




# from flask import Flask, render_template, request, redirect, url_for, jsonify
# from datetime import datetime
# import threading
# import time as time_lib

# app = Flask(__name__)

# # Variables para el estado del LED y la programación
# led_status = "OFF"
# programmed_start_time = None
# programmed_end_time = None

# def check_led_schedule():
#     global led_status
#     while True:
#         # Si hay un horario programado, comprobar si debe encenderse el LED
#         if programmed_start_time and programmed_end_time:
#             current_time = datetime.now().time()
#             if programmed_start_time <= current_time <= programmed_end_time:
#                 if led_status == "OFF":
#                     led_status = "ON"
#                     print("LED ENCENDIDO (programado)")
#             else:
#                 if led_status == "ON":
#                     led_status = "OFF"
#                     print("LED APAGADO (fuera del horario programado)")
#         time_lib.sleep(60)  # Verificar cada minuto

# @app.route('/')
# def home():
#     return render_template('index.html', led_status=led_status)

# @app.route('/programado', methods=['GET'])
# def programado():
#     # Pasamos las horas programadas a la plantilla
#     return render_template('programado.html', 
#                            start_time=programmed_start_time,
#                            end_time=programmed_end_time)

# @app.route('/set_program', methods=['POST'])
# def set_program():
#     global programmed_start_time, programmed_end_time

#     start_time = request.form['start_time']
#     end_time = request.form['end_time']

#     # Convertir las horas a objetos `time` para comparación
#     programmed_start_time = datetime.strptime(start_time, "%H:%M").time()
#     programmed_end_time = datetime.strptime(end_time, "%H:%M").time()

#     # Redirigir a la página de programación con las horas seleccionadas
#     return redirect(url_for('programado'))

# @app.route('/cancel_program', methods=['POST'])
# def cancel_program():
#     global programmed_start_time, programmed_end_time

#     # Restablecer las horas programadas a None
#     programmed_start_time = None
#     programmed_end_time = None

#     # Redirigir a la página de programación con las horas eliminadas
#     return redirect(url_for('programado'))

# @app.route('/get_status', methods=['GET'])
# def get_status():
#     return jsonify(status=led_status)

# if __name__ == '__main__':
#     # Iniciar el hilo que verifica la programación
#     thread = threading.Thread(target=check_led_schedule)
#     thread.daemon = True  # El hilo se cierra cuando la aplicación Flask termina
#     thread.start()

#     app.run(debug=True, host='0.0.0.0', port=5000)
