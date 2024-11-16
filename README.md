# child_mind_internet
Kaggle project where physical activity of children is used to predict problematic internet use.

Notes:
- 39% of the training data is missing sii values.
- 82 data columns on train.csv
- 996 parquet files (files with parquet inside tagged by id of child) in series_train.parquet
- 3960 unique ids in train.csv
- Have not yet opened the parquet files to examine what's in them.
- Parquet directory folders for training are massive (more than 6 gb)
- Test data csv isn't actually a test csv, we will have to generate our own test dataframe for predictions from the training set.

Need to evaluate & cross reference the parquet files against the unique ids to verify which children have parquet data.

Need to determine how we will generate sii for the training data missing sii values. Either that or we cut the missing ids and run training on the set that has sii measurements. We can train models on either approach and see the results.

If we "generate" sii datapoints for a part of the training set, we cannot utilize those "generated" datapoints for evaluation in our testing set. Oftentimes, we split the training set to produce testing sets via cross-validation, but this is not performable or feasible for "generated" datapoints. So, if we generate sii values, we separate the datapoints and only use them for training purposes. We can also use this approach to potentially improve our datapoint generation abilities.

Need to open up a few parquet files and do a basic lookover to see what we're working with.

We should keep the parquet files downloaded into a separate directory for access, but we can keep train.csv in the main directory.

Once we begin working with the data, we can utilize separate branches to try different variations & approaches.

Useful discussion links from Kaggle:

https://www.kaggle.com/competitions/child-mind-institute-problematic-internet-use/discussion/546266
