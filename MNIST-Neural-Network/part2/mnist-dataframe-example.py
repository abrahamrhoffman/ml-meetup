#!/usr/bin/python
import pandas as pd
TEST = pd.read_csv('./mnist/test.csv', header=None)
TEST.shape
TEST.head()
TEST.columns.values
TEST.iloc[0:1]
TEST.iloc[0:1].values
type(TEST.head().iloc[0:1].values)
