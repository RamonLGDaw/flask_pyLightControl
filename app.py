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
