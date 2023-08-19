from flask import Flask, request, jsonify #importing the libraries 
import random 


app = Flask(__name__)






def generate_random_vector(dim): #where is this function create the radom vectors of 500
    return [random.random() for _ in range(dim)]

@app.route('/random_vector', methods=['POST']) #handling the route calls 
def get_random_vector(): 
    try:
        data = request.get_json()
        preqin_test = data['preqin_test']
        vector = generate_random_vector(500)
        return jsonify(vector)
    except Exception as e:
        return jsonify({'error': str(e)}), 400








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)












