# child_mind_internet
Kaggle project where physical activity of children is used to predict problematic internet use.

Notes:
- 39% of the training data is missing sii values.
- 82 data columns on train.csv
- 996 parquet files (files with parquet inside tagged by id of child) in series_train.parquet
- 3960 unique ids in train.csv
- Have not yet opened the parquet files to examine what's in them.

Need to evaluate & cross reference the parquet files against the unique ids to verify which children have parquet data.

Need to determine how we will generate sii for the training data missing sii values. Either that or we cut the missing ids and run training on the set that has sii measurements. We can train models on either approach and see the results.

Need to open up a few parquet files and do a basic lookover to see what we're working with.