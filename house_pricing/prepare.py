# Imports
import pandas as pd
import logging
# from .config import OUTPUT_PREPARE
import os

OUTPUT_PREPARE = os.path.join("outputs", "prepared_data.pkl")
INPUT_PREPARE = os.path.join("data", "train.csv")


def prepare(data_df: pd.DataFrame) -> pd.DataFrame:
    # Removing features with lots of null values
    data_df = data_df.filter(
        ["OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF", "1stFlrSF", "SalePrice"])
    data_df = pd.get_dummies(data_df)
    return data_df


if __name__ == "__main__":
    input_df = pd.read_csv(INPUT_PREPARE)  # Pulling data
    output_df = prepare(input_df)
    output_df.to_pickle(OUTPUT_PREPARE)

    logging.info("A dataset of %d columns with %d has been prepared and stored at %s.", output_df.shape[1],
                 output_df.shape[0], OUTPUT_PREPARE)
