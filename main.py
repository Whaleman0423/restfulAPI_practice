from flask import Flask, request, jsonify
from target_controller import TargetController

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/', methods=["GET"])
def get_all():
    return TargetController.getall_api()

@app.route('/user/<pid>', methods=["GET"])
def get_one(pid):
    return TargetController.get_api(pid)

@app.route('/user/', methods=["POST"])
def post_api():
    new = request.get_json()
    return TargetController.post_api(new)

@app.route('/user/', methods=["PUT"])
def update_api():
    renew = request.get_json()
    return TargetController.update_api(renew)

@app.route('/user/<pid>', methods=["DELETE"])
def delete_api(pid):
    return TargetController.delete_api(pid)

if __name__ == '__main__':
    app.run(debug=True)
