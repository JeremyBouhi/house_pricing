import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
import logging
import os
OUTPUT_FEATURES = os.path.join("outputs", "split_featured.pkl")
OUTPUT_TRAIN = os.path.join("outputs", "model.pkl")
OUTPUT_EVALUATE = os.path.join("outputs", "metrics.txt")


def evaluate(model, X, y) -> pd.DataFrame:
    """Evaluate the model on the test set and return some metrics"""
    y_pred = model.predict(X)
    metrics = sqrt(mean_squared_error(y, y_pred))
    return metrics


if __name__ == "__main__":
    # Pulling the model
    model = pd.read_pickle(OUTPUT_TRAIN)
    # Pulling the data
    splits = pd.read_pickle(OUTPUT_FEATURES)
    X, y = splits["X_test"], splits["y_test"]

    # Evaluate
    metrics = evaluate(model, X, y)
    # Storing the metrics for DVC
    with open(OUTPUT_EVALUATE, "w") as f:
        f.write("%f" % (metrics))

    logging.info("RMSE : %d and stored at %s", metrics, OUTPUT_EVALUATE)

