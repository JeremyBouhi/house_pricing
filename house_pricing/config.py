import os

OUTPUT_FOLDER = "/outputs"
OUTPUT_PREPARE = os.path.join(OUTPUT_FOLDER, "/prepared_data.p")
OUTPUT_SPLIT = os.path.join(OUTPUT_FOLDER, "/split_data.p")
OUTPUT_FEATURES = os.path.join(OUTPUT_FOLDER, "/split_featured.p")
OUTPUT_TRAIN = os.path.join(OUTPUT_FOLDER, "/model.p")
OUTPUT_EVALUATE = os.path.join(OUTPUT_FOLDER, "/metrics.csv")
