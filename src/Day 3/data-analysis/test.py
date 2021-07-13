import pandas
import os

sample_data = [
    {
        "header1": 1,
        "header2": 2,
        "header3": 2
    },
    {
        "header1": 1,
        "header2": 2,
        "header3": 2
    },
    {
        "header1": 1,
        "header2": 2,
        "header3": 2
    },
    {
        "header1": 1,
        "header2": 2,
        "header3": 2
    }
]

data_df = pandas.DataFrame(data=sample_data)
data_df.to_excel("data1.xlsx", engine="xlsxwriter")
