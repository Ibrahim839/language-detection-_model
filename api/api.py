from flask import Flask ,jsonify ,request
from model.model import model


api = Flask(__name__)

@api.route('/', methods=['GET'])


def index():
    return jsonify({
        'status':'healthy',
        'version':model.__version__
    })
@api.route('/predict',methods=['POST'])
def predict():
    d = request.get_json()
    s = d['text']
    result = model.predict(d['text'])
    return {
        'result':result
    }

if __name__=='__main__':
    
    api.run(
        host= '127.0.0.1',
        port= 5000,
        debug= True
    )
