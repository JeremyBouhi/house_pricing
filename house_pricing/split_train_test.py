# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
import logging
#from model.config import OUTPUT_SPLIT, OUTPUT_FEATURES
import os
OUTPUT_PREPARE = os.path.join("outputs", "prepared_data.pkl")
OUTPUT_SPLIT = os.path.join("outputs", "split_data.pkl")


def split_dataset(data_df: pd.DataFrame) -> dict:
    """Just split the dataset with a dict"""

    # Splits the dataset
    print(data_df.shape)
    X, y = data_df.drop("SalePrice", axis=1), data_df["SalePrice"]
    splits = train_test_split(X, y, test_size=0.3)

    # Transform to dict
    labels = ["X_train", "X_test", "y_train", "y_test"]
    splits_dict = dict(zip(labels, splits))

    return splits_dict


if __name__ == "__main__":
    input_df = pd.read_pickle(OUTPUT_PREPARE)  # Pulling data
    output_dict = split_dataset(input_df)

    pd.to_pickle(output_dict, OUTPUT_SPLIT)

    logging.info("The dataset has been split and stored at %s.", OUTPUT_SPLIT)
