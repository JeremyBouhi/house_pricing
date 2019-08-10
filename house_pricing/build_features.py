# Imports
import logging
import pandas as pd
#from model.config import OUTPUT_FEATURES, OUTPUT_PREPARE
import os
OUTPUT_SPLIT = os.path.join("outputs", "split_data.pkl")
OUTPUT_FEATURES = os.path.join("outputs", "split_featured.pkl")


def build_features(data_df: pd.DataFrame) -> pd.DataFrame:
    return data_df.copy()  # Nothing yet


if __name__ == "__main__":
    input_dict = pd.read_pickle(OUTPUT_SPLIT)  # Pulling data

    output_dict = input_dict    # Keep the same for simplicity but you should copy it
    for df_name in ["X_train", "X_test"]:
        split_data = input_dict[df_name]
        split_data_featured = build_features(split_data)
        output_dict[df_name] = split_data_featured

    pd.to_pickle(output_dict, OUTPUT_FEATURES)

    logging.info("The dataset has been featured and stored at %s", OUTPUT_FEATURES)
