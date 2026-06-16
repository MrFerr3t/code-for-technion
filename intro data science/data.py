import pandas as pd
from datetime import datetime


def load_data(path):
    data = pd.read_csv(path)
    return data


def season_name(season):
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
    time_list = datetime.strptime(time, "%d/%m/%y %H:%M")
    return time_list.hour, time_list.day, time_list.month, time_list.year

def weekend_holiday(holiday, weekend):
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
    df["season_name"] = df["season"].apply(season_name)
    df[["Hour"], ["Day"], ["Month"], ["Year"]] = df["timestamp"].apply(get_timestamp).tolist()
    df["is_weekend_holiday"] = df[["is_holiday"],["is_weekend"]].apply(weekend_holiday)
    df["t_diff"] = df[["t1"],["t2"]].apply(diff = lambda t1, t2: abs(t1 - t2))



def data_analysis(df):
    print("describe output:")
    print(df.describe().to_string())
    print()
    print("corr output:")
    corr = df.corr(numeric_only = True)
    print(corr.to_string())
    print()
    corr_dict = {}
    for i in range(len(corr.columns)):
        for j in range(i+1, corr.columns):
            corr_x = corr.columns[i]
            corr_y = corr.columns[j]
            corr_dict[(corr_x,corr_y)] = corr.iloc[i, j]
    
    top_5_corr = dict(sorted(corr_dict.keys()), key = lambda item: abs(item[1])[-1:-5])
    
    print("Highest correlated are:\n")
    for i, (pair, value) in enumerate(top_5_corr.items()):
        print(f"{i + 1}, {pair} with {value:.6f}\n")
    
    bottom_5_corr = dict(sorted(corr_dict.keys()), key = lambda item: abs(item[1])[:5])
    
    print("Lowest correlated are:\n")
    for i, (pair, value) in enumerate(bottom_5_corr.items()):
        print(f"{i + 1}, {pair} with {value:.6f}\n")
    season_t_diff = df.groupby("season_name")["t_diff"].mean(numeric_only = True)
    all_mean = df["t_diff"].mean(numeric_only = True)

    fall_mean = season_t_diff["fall"]
    winter_mean = season_t_diff["winter"]
    spring_mean = season_t_diff["spring"]
    summer_mean = season_t_diff["summer"]

    print(f"fall average t diff is {fall_mean:.2f}")
    print(f"spring average t diff is {spring_mean:.2f}")
    print(f"summer average t diff is {summer_mean:.2f}")
    print(f"winter average t diff is {winter_mean:.2f}")
    print(f"All average t diff is {all_mean:.2f}")