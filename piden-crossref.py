import os

directory = os.getcwd()

test_dir = directory + "\series_test.parquet"
train_dir = directory + "\series_train.parquet"

trf_args = list(os.walk(train_dir))

for z in trf_args: #every z is a tuple
    for r in z:
        print(r)