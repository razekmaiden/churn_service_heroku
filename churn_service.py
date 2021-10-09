import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_model:
    model = pickle.load(f_model)

with open(dv_file, 'rb') as f_dv:
    dv = pickle.load(f_dv)

app = Flask('churn_service')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'churn_probability': float(y_pred),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)