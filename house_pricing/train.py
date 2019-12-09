# Imports
import logging

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
import pandas as pd
#from model.config import OUTPUT_TRAIN, OUTPUT_SPLIT
import os
OUTPUT_FEATURES = os.path.join("outputs", "split_featured.pkl")
OUTPUT_TRAIN = os.path.join("outputs", "model.pkl")


def train(X, y):
    model = xgb.XGBRegressor()
    model.fit(X, y)
    return model


if __name__ == "__main__":
    input_dict = pd.read_pickle(OUTPUT_FEATURES)

    X, y = input_dict["X_train"], input_dict["y_train"]
    model = train(X, y)

    pd.to_pickle(model, OUTPUT_TRAIN)

    logging.info("A model has been trained with %s features named :\n\t%s.", len(X.columns), ", ".join(X.columns))
