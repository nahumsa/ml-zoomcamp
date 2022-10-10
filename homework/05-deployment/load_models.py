import pickle
from pathlib import Path


def load_pickle(path):
    with open(path, "rb") as input_file:
        loaded_file = pickle.load(input_file)
    return loaded_file


if __name__ == "__main__":
    model_path = Path("model1.bin")
    model = load_pickle(model_path)

    dv_path = Path("dv.bin")
    dv = load_pickle(dv_path)

    client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

    X = dv.transform(client)
    pred = model.predict_proba(X)[:, 1]
    print(pred)
