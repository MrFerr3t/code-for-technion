import pandas as pd
from datetime import datetime


def load_data(path):
    """get path of data in files and return the stored data"""
    data = pd.read_csv(path)
    return data


def season_name(season):
    """get number and return the corresponding name of the season"""
    if (season == 0):
        return "spring"
    elif (season == 1):
        return "summer"
    elif (season == 2):
        return "fall"
    elif (season == 3):
        return "winter"
    else:
        return -1


def get_timestamp(time):
    """get string that has the time and break it up to the correct format"""
    time_list = datetime.strptime(time, "%d/%m/%Y %H:%M")
    return time_list.hour, time_list.day, time_list.month, time_list.year

def weekend_holiday(holiday, weekend):
    """get the holiday and weekend values and return the correct number according to the chart"""
    if weekend == 0 and holiday == 0:
        return 1
    elif weekend == 1 and holiday == 0:
        return 2
    elif weekend == 0 and holiday == 1:
        return 3
    elif weekend == 1 and holiday == 1:
        return 4
    else:
        return -1

def add_new_columns(df):
    """get dataframe and add the requested columns"""
    df["season_name"] = df["season"].apply(season_name)
    df[["Hour", "Day", "Month", "Year"]] = df["timestamp"].apply(lambda x: pd.Series(get_timestamp(x)))
    df["is_weekend_holiday"] = df.apply(lambda row: weekend_holiday(row["is_holiday"], row["is_weekend"]), axis=1)
    df["t_diff"] = df["t2"] - df["t1"]

    return df



def data_analysis(df):
    """get the dataframe and annalize the data according to the homework requirements"""
    print("describe output:")
    print(df.describe().to_string())
    print()

    print("corr output:")
    corr = df.corr(numeric_only=True)
    print(corr.to_string())
    print()

    corr_dict = {}
    for i in range(len(corr.columns)):
        for j in range(i + 1, len(corr.columns)):
            corr_dict[(corr.columns[i],corr.columns[j])] = corr.iloc[i, j]

    sorted_corr = sorted(corr_dict.items(), key=lambda item: abs(item[1]), reverse=True)

    top_5_corr = sorted_corr[:5]

    print("Highest correlated are:\n")
    for i, (pair, value) in enumerate(top_5_corr):
        print(f"{i + 1}. ('{pair[0]}', '{pair[1]}') with {abs(value):.6f}")

    bottom_5_corr = sorted_corr[-5:][::-1]

    print("Lowest correlated are:\n")
    for i, (pair, value) in enumerate(bottom_5_corr):
        print(f"{i + 1}. ('{pair[0]}', '{pair[1]}') with {abs(value):.6f}")
    season_t_diff = df.groupby("season_name")["t_diff"].mean(numeric_only = True)
    all_mean = df["t_diff"].mean(numeric_only = True)

    fall_mean = season_t_diff["fall"]
    winter_mean = season_t_diff["winter"]
    spring_mean = season_t_diff["spring"]
    summer_mean = season_t_diff["summer"]

    print(f"fall average t_diff is {fall_mean:.2f}")
    print(f"spring average t_diff is {spring_mean:.2f}")
    print(f"summer average t_diff is {summer_mean:.2f}")
    print(f"winter average t_diff is {winter_mean:.2f}")
    print(f"All average t_diff is {all_mean:.2f}")