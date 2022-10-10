import pickle
from pathlib import Path

from flask import Flask, jsonify, request


def load_pickle(path):
    with open(path, "rb") as input_file:
        loaded_file = pickle.load(input_file)
    return loaded_file


model_path = Path("model1.bin")
dv_path = Path("dv.bin")
model = load_pickle(model_path)
dv = load_pickle(dv_path)
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict_length():
    client = request.get_json()
    X = dv.transform([client])
    pred = model.predict_proba(X)[:, 1]
    result = {
        "probability": float(pred),
        "model_version": "1",
        "model_name": "ml-zoomcamp",
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
