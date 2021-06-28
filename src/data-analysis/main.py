import pandas
import matplotlib.pyplot as plt
import data_generator
import json
import os

# this file uses the data generator module that we wrote
# print some information
print("Starting..")

# some month and year variable to help us get some data
month = 1
year = 2021

# generate some data folder paths
data_folder = os.path.join(os.path.dirname(
    __file__), "data")
# setup some data file paths string
data_file_path = os.path.join(
    data_folder, "data_{}{}.json".format(month, year))

# print this information out.
print("Data folder: {}".format(data_folder))

# check if we already have data for a given year and month. if it is not, then fetch some data, and write that to a file.
if os.path.exists(data_file_path) == False:
    print("File for given date {}/{} does not exist. Attempting to fetch data from the server..".format(month, year))
    # use our data generator module
    data_generator.init()
    data = data_generator.get_global_daily_report(month, year)
    # if the data is correctly fetched, write it to a file. else raise an error
    if data[0] == 200:
        print("Got data successfully!")
        with open(data_file_path, "w") as f:
            json.dump(json.loads(data[1])["Document"], f, indent=4)
            print("Data written at: {}".format(data_file_path))
    else:
        raise RuntimeError(
            "Some problem with getting data: Code {}, Message: {}".format(data[0], data[1]))
else:
    print("Found a data file for the given date!")


def example_1_write_to_excel(data_df):
    # If you wish to write this data to a excel row-col format, uncomment this line.
    data_df.to_excel(os.path.join(data_folder, "data_{}{}.xlsx".format(
        month, year)), engine="xlsxwriter")


def example_2_filter_by_province(data_df):
    # Example 2: filter the data set and get information for Delhi and then plot a bar graph for confirmed, active, recovered cases and the death numbers
    ################################################################
    cases_delhi = data_df[data_df["province_state"].isin(["Delhi"])]
    cases_delhi.plot(x="last_update", y=[
        "confirmed", "active", "recovered", "deaths"], kind="bar")
    plt.show()
    ################################################################


def example_3_filter_by_active_cases(data_df):
    # Example 3: filter the data set and get information for provinces where there are more than a million active cases
    ################################################################
    cond_1 = (data_df["active"] > 1000000)
    cond_2 = data_df["province_state"].str.lower().str.strip() != "0"
    active_cases_more_than_1m = data_df[cond_1 & cond_2].drop_duplicates(
        ["combined_key", "active"]
    )
    active_cases_more_than_1m.plot(x="combined_key", y="active", kind="bar")
    plt.show()
    ################################################################


def example_4_subplot_4_cities_subplot(data_df):
    # Example 4: filter the data set and plot 4 graphs in one figure,
    ################################################################
    fig, axes = plt.subplots(2, 2)
    cases_in_mah = data_df[(
        data_df["province_state"].str.lower().str.strip() == "maharashtra".lower())]
    cases_in_mah.plot(ax=axes[0, 0], x="last_update",
                      y="active", kind="scatter")

    cases_in_eng = data_df[(
        data_df["province_state"].str.lower().str.strip() == "England".lower())]
    cases_in_eng.plot(ax=axes[1, 0], x="last_update",
                      y="active", kind="scatter")

    cases_in_delhi = data_df[(
        data_df["province_state"].str.lower().str.strip() == "delhi".lower())]
    cases_in_delhi.plot(ax=axes[0, 1], x="last_update",
                        y="active", kind="scatter")

    cases_in_ny = data_df[(
        data_df["province_state"].str.lower().str.strip() == "New york".lower())]
    cases_in_ny.plot(ax=axes[1, 1], x="last_update",
                     y="active", kind="scatter")
    plt.show()
    ################################################################


# load the json data using pandas and operate on it as a dataframe.
print("Reading data file from: {}".format(data_file_path))
df = pandas.read_json(data_file_path)

# example 1: write to excel sheet
# if you want to avoid writing to an excel sheet, please comment the line below
example_1_write_to_excel(df)

# please comment example 3 and 4 below and then run this.
# example_2_filter_by_province(df)

# please comment example 2 and 4, and then run the code below
# example_3_filter_by_active_cases(df)

# please comment example 2, 3 and then run code below
# example_4_subplot_4_cities_subplot(df)
# print(df.info())
