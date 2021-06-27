import requests
from requests.compat import urljoin
import json
import os
import datetime

# https://www.covid19api.dev/#intro

months = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec"
}

bearer_token = ""
api_def = None


def read_api_def():
    global api_def
    api_def_file_path = os.path.join(
        os.path.dirname(__file__), "config", "api-def.json")
    with open(api_def_file_path, "r") as f:
        api_def = json.load(f)


def generate_token(force=False):
    global bearer_token
    token_file_path = os.path.join(
        os.path.dirname(__file__), "config", "token.json")
    if force == False and os.path.exists(token_file_path):
        with open(token_file_path) as token_file:
            bearer_token = json.load(token_file)["token"]
            return

    auth_params = {
        "username": api_def["username"],
        "password": api_def["password"]
    }

    auth_response = requests.post(
        url=urljoin(api_def["root_url"], api_def["api_defs"]["gen_token"]), data=auth_params)

    if auth_response.status_code == 200:
        bearer_token = json.loads(
            auth_response.content.decode("utf-8"))["Document"]
        auth_token = {
            "token": bearer_token
        }
        with open(token_file_path, "w") as f:
            json.dump(auth_token, f, indent=4)
    else:
        print("A problem occurred. Code: {}, Message: {}".format(
            auth_response.status_code, auth_response.content.decode("utf-8")))
        raise Exception("Problem with auth")


def get_global_daily_report(month: int, year: int):
    today = datetime.datetime.today()
    if today.year != 2020:
        if today.year == 2021:
            if today.month > 6:
                raise Exception(
                    "Invalid date range! please enter the year as either 2020 (month range 1-12) or 2021 (month range 1-current month)")

    api_req_param = api_def["api_defs"]["global_daily_reports"].format(
        mon=str(months[month]), yyyy=year)
    auth_token = {
        "Authorization": "Bearer {0}".format(bearer_token)
    }
    stats_response = requests.get(
        url=urljoin(api_def["root_url"], api_req_param), headers=auth_token)

    return (
        stats_response.status_code,
        stats_response.content.decode("utf-8")
    )


def init():
    read_api_def()
    generate_token()


def main(mon=0, year=0):
    init()
    mon = datetime.datetime.today().month if mon == 0 else mon
    year = datetime.datetime.today().year if year == 0 else year
    response = get_global_daily_report(mon, year)
    if response[0] == 200:
        with open(os.path.join(os.path.dirname(__file__), "data", "data_{}{}.json".format(mon, year)), "w") as f:
            json.dump(json.loads(response[1]), f, indent=4)


if __name__ == "__main__":
    main()
