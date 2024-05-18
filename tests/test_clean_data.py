from src.evalcdcdatagovjson.clean_data import build_pandas_df
import pandas as pd


def test_build_pandas_df():
    df = build_pandas_df()
    assert isinstance(df, pd.DataFrame)
    for c in [
        'id',
        'url',
        'theme',
        'publisher_type',
        'publisher_name',
        'access_level',
        'type',
        'distribution_options',
        'record_index',
    ]:
        assert c in list(df.columns)

    print(df)
