import pandas
import matplotlib.pyplot as plt
import data_generator
import json
import os

print("Starting..")

month = 4
year = 2021

data_folder = os.path.join(os.path.dirname(
    __file__), "data")
data_file_path = os.path.join(
    data_folder, "data_{}{}.json".format(month, year))

print("Data folder: {}".format(data_folder))

if os.path.exists(data_file_path) == False:
    print("File for given date {}/{} does not exist. Attempting to fetch data from the server..".format(month, year))
    data_generator.init()
    data = data_generator.get_global_daily_report(month, year)
    if data[0] == 200:
        print("Got data successfully!")
        with open(data_file_path, "w") as f:
            json.dump(json.loads(data[1])["Document"], f, indent=4)
            print("Data written at: {}".format(data_file_path))
else:
    print("Found a data file for the given date!")

print("Reading data file from: {}".format(data_file_path))
df = pandas.read_json(data_file_path)
# cases_delhi = df[df["province_state"].isin(["Delhi"])]
# cases_delhi.plot(x="last_update", y=[
#     "confirmed", "active", "recovered", "deaths"], kind="bar")

# cond_1 = (df["active"] > 1000000)
# cond_2 = df["province_state"].str.lower().str.strip() != "0"
# active_cases_more_than_10k = df[cond_1 & cond_2].drop_duplicates(
#     ["combined_key", "active"]
# )
# active_cases_more_than_10k.plot(x="combined_key", y="active", kind="bar")

fig, axes = plt.subplots(2, 2)

cases_in_mah = df[(
    df["province_state"].str.lower().str.strip() == "maharashtra".lower())]
cases_in_mah.plot(ax=axes[0, 0], x="last_update", y="active", kind="scatter")

cases_in_eng = df[(
    df["province_state"].str.lower().str.strip() == "England".lower())]
cases_in_eng.plot(ax=axes[1, 0], x="last_update",
                     y="active", kind="scatter")

cases_in_delhi = df[(
    df["province_state"].str.lower().str.strip() == "delhi".lower())]
cases_in_delhi.plot(ax=axes[0, 1], x="last_update", y="active", kind="scatter")

cases_in_ny = df[(
    df["province_state"].str.lower().str.strip() == "New york".lower())]
cases_in_ny.plot(ax=axes[1, 1], x="last_update", y="active", kind="scatter")

plt.show()

# df.to_excel(os.path.join(data_folder, "data_{}{}.xlsx".format(month, year)), engine="xlsxwriter")
# print(df.info())
