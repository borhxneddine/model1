from f1 import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/endpoint', methods=['GET'])
def api_endpoint():
    if request.method == 'GET':
        return jsonify({'message': 'GET method is called'})

if __name__ == '__main__':
    app.run(debug=True, port=9090)
