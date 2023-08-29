import json
import os

# SPLIT_RATIO = (9, 1, 0)
DATALIST_FILE = "../../downloads/ds/customdata.json"
DESTINATION_DIR = "../../downloads"

DATALIST_PATH = os.path.join(os.path.dirname(__file__), DATALIST_FILE)
TRAIN_SPLIT_PATH = os.path.join(os.path.dirname(__file__), DESTINATION_DIR, "train_split_custom.json")
VAL_SPLIT_PATH = os.path.join(os.path.dirname(__file__), DESTINATION_DIR, "val_split_custom.json")
TEST_SPLIT_PATH = os.path.join(os.path.dirname(__file__), DESTINATION_DIR, "test_split_custom.json")

with open(DATALIST_PATH, "r") as f:
    datalist = json.load(f)

data_num = len(datalist)

print("total: " + str(data_num))

train_split = []
val_split = []
test_split = []

for data in datalist:
    if data.startswith("t"):
        train_split.append(data)
    elif data.startswith("m"):
        val_split.append(data)
    else:
        test_split.append(data)

with open(TRAIN_SPLIT_PATH, "w") as f:
    json.dump(train_split, f)

with open(VAL_SPLIT_PATH, "w") as f:
    json.dump(val_split, f)

with open(TEST_SPLIT_PATH, "w") as f:
    json.dump(test_split, f)

print("train: " + str(len(train_split)))
print("val: " + str(len(val_split)))
print("test: " + str(len(test_split)))