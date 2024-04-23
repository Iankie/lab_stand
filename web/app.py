from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form['command']
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return jsonify({'result': result.decode('utf-8')})
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
