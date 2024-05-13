from flask import Flask, render_template, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

import subprocess

app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "admin": generate_password_hash("P@ssw0rd")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
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
    app.run(host='0.0.0.0', port=80, debug=True)
