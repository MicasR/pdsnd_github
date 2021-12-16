from data_analysis import utils as u
import pandas as pd


def retrieve_data_from_csv(path: str, city: str) -> pd.DataFrame:
    """Get csv data and return a panda dataframe with origen column."""
    data = pd.read_csv(path)
    data["city"] = city

    if city == "Washington":
        data["Gender"] = pd.Series()
        data["Birth Year"] = pd.Series()
    return data


CHICAGO = retrieve_data_from_csv("./raw_data/chicago.csv", "Chicago")
NEW_YORK = retrieve_data_from_csv("./raw_data/new_york_city.csv", "New York")
WASHINGTON = retrieve_data_from_csv("./raw_data/washington.csv", "Washington")


def casefold_str_items(listing: list) -> list:
    """
    Receive a list and return a list with all string items casefolded

    # Examples:
    ``casefold_str_items(['cHicago','WASHINGTON']) # ->['chicago','washington']``
    ``casefold_str_items(['ChicaGO','1', 2, True]) # ->['chicago','1', 2, True]``
    """
    return [item.casefold() if type(item) == str else item for item in listing]


def get_raw_by_city(cities: list[str]) -> pd.DataFrame:
    """
    Receive a list of strings that represent cities and return a panda DataFrame with the data.

    # Keyword arguments:\n
    cities:list[str]\n
    * The available cities are `"Chicago"`, `"New York"` and `"Washington"`.\n
    * Accept any string capitalization of this cities.\n
    * Return all city data if ["*"] is received.

    # Exceptions:\n
    Ignore if an unavailable city string is provided.\n

    # Examples:
    ``get_raw_by_city(["New York"]) #-> New York data``\n
    ``get_raw_by_city(["New York", "243"]) #-> New York data``\n
    ``get_raw_by_city(["cHicAgo", "waSHINGton"]) #-> Chicago and Washington data``\n
    ``get_raw_by_city(["*"]) #-> all data``\n
    ``get_raw_by_city(["NYC"]) #-> no data``\n
    ``get_raw_by_city([]) #-> no data``\n
    """

    frames = []

    cities_lower_case = casefold_str_items(cities)

    if "chicago" in cities_lower_case or "*" in cities_lower_case:
        frames.append(CHICAGO)
    if "new york" in cities_lower_case or "*" in cities_lower_case:
        frames.append(NEW_YORK)
    if "washington" in cities_lower_case or "*" in cities_lower_case:
        frames.append(WASHINGTON)

    if frames:
        return pd.concat(frames, ignore_index=True)
    else:
        return pd.DataFrame()


def get_clean_by_city(cities: list[str]) -> pd.DataFrame:
    """
    Receive a list of strings that represent cities and return a panda DataFrame with the data.\n
    Its like the get_raw_by_city but with cleaning methods applied

    # Keyword arguments:\n
    cities:list[str]\n
    * The available cities are `"Chicago"`, `"New York"` and `"Washington"`.\n
    * Accept any string capitalization of this cities.\n
    * Return all city data if ["*"] is received.

    # Exceptions:\n
    Ignore if an unavailable city string is provided.\n

    # Examples:
    ``get_clean_by_city(["New York"]) #-> New York data``\n
    ``get_clean_by_city(["New York", "243"]) #-> New York data``\n
    ``get_clean_by_city(["cHicAgo", "waSHINGton"]) #-> Chicago and Washington data``\n
    ``get_clean_by_city(["*"]) #-> all data``\n
    ``get_clean_by_city(["NYC"]) #-> no data``\n
    ``get_clean_by_city([]) #-> no data``\n
    """
    df = get_raw_by_city(cities)
    if pd.DataFrame().equals(df):
        return df
    else:
        df["User Type"].fillna("unknown", inplace=True)
        df["Gender"].fillna("unknown", inplace=True)
        df["Birth Year"].fillna(0.0, inplace=True)
        return df


def filter_data(filters: dict) -> pd.DataFrame:
    """Receive filters as a dict and return a pandas Dataframe."""
    # city
    df = get_clean_by_city(filters["cities"])
    if df.empty: return df

    #User Type & Gender
    filter_series = (
        (df["User Type"].isin(filters["user_types"])) &
        (df["Gender"].isin(filters["genders"]))
    )

    #Start Time
    if u.str_is_date(filters["date"]["from"]):
        filter_series = filter_series & (
            pd.to_datetime(df["Start Time"], format='%Y-%m-%d') >= filters["date"]["from"]
        )

    #End Time
    if u.str_is_date(filters["date"]["thru"]):
        filter_series = filter_series & (
            pd.to_datetime(df["End Time"], format='%Y-%m-%d') < filters["date"]["thru"]
        )

    #duration min
    if u.is_positive_float(filters["duration"]["min"]):
        filter_series = filter_series & (
            df["Trip Duration"] >= float(filters["duration"]["min"])
        )

    #duration max
    if u.is_positive_float(filters["duration"]["max"]):
        filter_series = filter_series & (
            df["Trip Duration"] < float(filters["duration"]["max"])
        )


    #known age
    if not filters["age"]["known"]["include"]:
        filter_series = filter_series & (
            df["Birth Year"] == 0
        )

    #known age min
    if u.is_positive_float(filters["age"]["known"]["min"]) and filters["age"]["known"]["include"]:
        filter_series = filter_series & (
            (df["Birth Year"] <= 2017-float(filters["age"]["known"]["min"]))
        )

    #known age max
    if u.is_positive_float(filters["age"]["known"]["max"]) and filters["age"]["known"]["include"]:
        filter_series = filter_series & (
            (df["Birth Year"] > 2017-float(filters["age"]["known"]["max"])) |
            (df["Birth Year"] == 0)
        )

    #unknown age
    if not filters["age"]["unknown"]["include"]:
        filter_series = filter_series & (
            df["Birth Year"] != 0
        )

    return df[filter_series]
