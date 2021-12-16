from data_analysis import utils as u


def format_filters(filters: dict) -> dict:
    """Receive filters and prepare for usage on dataframe."""
    formated_dict = {
        "cities": [], #list
        "user_types": [], #list
        "genders": [], # list
        "date": {
            "from": None, #str "yyyy-mm-dd"
            "thru": None, #str "yyyy-mm-dd"
        },
        "duration": {
            "min": None, #float
            "max": None  #float
        },
        "age": {
            "known": {
                "include": True, #bool
                "min": None, #float
                "max": None, #float
            },
            "unknown": {
                "include": True, #bool
            }
        }
    }

    # append cities
    if filters.get("city-chicago") == "on": formated_dict["cities"].append("chicago")
    if filters.get("city-new-york") == "on": formated_dict["cities"].append("new york")
    if filters.get("city-washington") == "on": formated_dict["cities"].append("washington")

    # append user types
    if filters.get("user-type-unknown") == "on": formated_dict["user_types"].append("unknown")
    if filters.get("user-type-customer") == "on": formated_dict["user_types"].append("Customer")
    if filters.get("user-type-dependent") == "on": formated_dict["user_types"].append("Dependent")
    if filters.get("user-type-subscriber") == "on": formated_dict["user_types"].append("Subscriber")

    # append genders
    if filters.get("gender-male") == "on": formated_dict["genders"].append("Male")
    if filters.get("gender-female") == "on": formated_dict["genders"].append("Female")
    if filters.get("gender-unknown") == "on": formated_dict["genders"].append("unknown")

    # set dates
    if u.str_is_date(filters.get("date-from")): formated_dict["date"]["from"] = filters.get("date-from")
    if u.str_is_date(filters.get("date-thru")): formated_dict["date"]["thru"] = filters.get("date-thru")

    # set duration
    if u.is_positive_float(filters.get("min-duration")): formated_dict["duration"]["min"] = float(filters.get("min-duration"))
    if u.is_positive_float(filters.get("max-duration")): formated_dict["duration"]["max"] = float(filters.get("max-duration"))

    #Set age includes
    if filters.get("include-known-age") == None: formated_dict["age"]["known"]["include"] = False
    if filters.get("include-unknown-age") == None: formated_dict["age"]["unknown"]["include"] = False

    # set age min max
    if u.is_positive_float(filters.get("min-age")): formated_dict["age"]["known"]["min"] = float(filters.get("min-age"))
    if u.is_positive_float(filters.get("max-age")): formated_dict["age"]["known"]["max"] = float(filters.get("max-age"))

    return formated_dict

