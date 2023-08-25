import json
import os

SPLIT_RATIO = (9, 1, 0)
DATALIST_FILE = "../../downloads/ds/customdata.json"
DESTINATION_DIR = "../../downloads"

DATALIST_PATH = os.path.join(os.path.dirname(__file__), DATALIST_FILE)
TRAIN_SPLIT_PATH = os.path.join(os.path.dirname(__file__), DESTINATION_DIR, "train_split_custom.json")
VAL_SPLIT_PATH = os.path.join(os.path.dirname(__file__), DESTINATION_DIR, "val_split_custom.json")
TEST_SPLIT_PATH = os.path.join(os.path.dirname(__file__), DESTINATION_DIR, "test_split_custom.json")

with open(DATALIST_PATH, "r") as f:
    datalist = json.load(f)

data_num = len(datalist)

train_split = [data for data in datalist if data.startswith("t")]
val_split = []
test_split = []

left_data = [data for data in datalist if not data.startswith("t")]
left_num = len(left_data)
train_ratio = int(SPLIT_RATIO[0] * (left_num / data_num))
val_ratio = SPLIT_RATIO[1]
test_ratio = SPLIT_RATIO[2]

split_num = train_ratio + val_ratio + test_ratio
for i in range(left_num):
    if i % split_num < train_ratio:
        train_split.append(datalist[i])
    elif i % split_num < train_ratio + val_ratio:
        val_split.append(datalist[i])
    else:
        test_split.append(datalist[i])

with open(TRAIN_SPLIT_PATH, "w") as f:
    json.dump(train_split, f)

with open(VAL_SPLIT_PATH, "w") as f:
    json.dump(val_split, f)

with open(TEST_SPLIT_PATH, "w") as f:
    json.dump(test_split, f)

print("train: " + str(len(train_split)))
print("val: " + str(len(val_split)))
print("test: " + str(len(test_split)))