
import calendar
from data_analysis import utils as u
import pandas as pd


def trips_month_city(df:pd.DataFrame) -> dict:
    """return a dict with the trips by city and by month"""
    final_info = {
        "All": [0,0,0,0,0,0],
        "Chicago": [0,0,0,0,0,0],
        "New York": [0,0,0,0,0,0],
        "Washington": [0, 0, 0, 0, 0, 0],
    }

    group_by_dict = df.groupby(["city", pd.DatetimeIndex(df["Start Time"]).month])["Trip Duration"].count().to_dict()

    for key in group_by_dict.keys():
        (city, month) = key
        final_info[city][month-1] = group_by_dict[key]
        final_info["All"][month-1] += group_by_dict[key]
    return final_info


def analyze(df: pd.DataFrame) -> dict:
    """Generate a dict with all statistics from a pandas DataFrame."""
    analysis = {
        "number_of_trips": None,
        "avg_travel_time": None,
        "avg_age": None,
        "trips_month_city":  {
            "All": [0, 0, 0, 0, 0, 0],
            "Chicago": [0, 0, 0, 0, 0, 0],
            "New York": [0, 0, 0, 0, 0, 0],
            "Washington": [0, 0, 0, 0, 0, 0],
        },
        "most_common_month": None,
        "most_common_dow": None,
        "most_common_hod": None,
    }
    if not df.empty:
        # number_of_trips
        analysis["number_of_trips"] = f'{(len(df.index)) :,}'

        # number_of_trips
        analysis["avg_age"] = len(df.index)

        # avg_travel_time
        analysis["avg_travel_time"]= u.float_to_str_date(df["Trip Duration"].mean())

        # avg_travel_time
        birth_year_filter = (df["Birth Year"] != 0)
        lst= birth_year_filter.unique()
        if len(lst) == 1 and lst[0] == False: analysis["avg_age"] = "unknown"
        else: analysis["avg_age"] = 2017 - int(df[df["Birth Year"] != 0]["Birth Year"].mean())

        # trips_month_city
        analysis["trips_month_city"] = trips_month_city(df)

        # most_common_month
        analysis["most_common_month"] = calendar.month_name[(pd.DatetimeIndex(df['Start Time']).month).value_counts().idxmax()]

        # most_common_dow
        analysis["most_common_dow"]= calendar.day_name[(pd.DatetimeIndex(df['Start Time']).dayofweek).value_counts().idxmax()]

        # most_common_how
        analysis["most_common_hod"]= int((pd.DatetimeIndex(df['Start Time']).hour).value_counts().idxmax())

    return analysis
