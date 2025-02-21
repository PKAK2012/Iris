# -*- coding: utf-8 -*-
"""Iris.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wqTHqd4Q2dKJDp6DO5i6YqstOdQwiVW4
"""

import pandas as pd
from google.colab import files
files.upload()

df = pd.read_csv("/content/Iris_Data.csv")

df.head()

df.info()

df["species"].unique()

from sklearn.preprocessing import OrdinalEncoder

O=OrdinalEncoder()

df["species"]=O.fit_transform(df[["species"]])

df["species"].unique()

df.info()

df

df.corr()