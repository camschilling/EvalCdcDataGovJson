from src.evalcdcdatagovjson.clean_data import build_pandas_df
import pandas as pd


def test_build_pandas_df():
    df = build_pandas_df()
    print(df.head())
