import pandas as pd


def get_line_average(dataframe, field):
    return dataframe.loc[field].mean(axis=0)
