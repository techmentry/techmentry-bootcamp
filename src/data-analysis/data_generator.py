import requests
from requests.compat import urljoin
import json
import os
import datetime

# https://www.covid19api.dev/#intro

# creating a static dictionary for all the month in the 3 letter format. as this is the only
# sure way of getting it correct without having to do a lot of date parsing.
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

# create a global variable for the bearer token.
# what is a bearer token? in simple words, it is a token we get when we authenticate with the server. when we send it to the server with the
bearer_token = ""
api_def = None


def read_api_def():
    # we store this API definition in a file just so that whenever there is a change to the API we don't have to touch the code. We can just
    # change the API endpoint, and the code should work the same way.
    global api_def
    # read this API definition from the file in the config folder, and then store it for later use.
    api_def_file_path = os.path.join(
        os.path.dirname(__file__), "config", "api-def.json")
    with open(api_def_file_path, "r") as f:
        api_def = json.load(f)


def generate_token(force=False):
    # The covid 19 tracking API we want to use requires us to authenticate with some form of username and password. To this request,
    # the API returns a bearer token, which in simpler terms is a way for it to know who is making a request and if that person can
    # use that endpoint. It also helps keep a track of the number of requests a user has made and also manage telemetry.
    global bearer_token

    # the token that the server sends us has a lifetime of ~55 hours. Hence, we don't need to regenerate it. We can just store the token
    # and load it the next time we bring up our script. However, it is to be noted that once 55 hours are up, we need to regenerate the token.
    # you can write some code trivially by storing the date and time the token was generated on in the json file itself, and then using it with the code below
    # to check if the token present is valid or not. If it is not, then you can refresh it. See a simple example below
    token_file_path = os.path.join(
        os.path.dirname(__file__), "config", "token.json")
    # check if we have a valid token already in the file
    if force == False and os.path.exists(token_file_path):
        with open(token_file_path) as token_file:
            # is the time difference between now and the date time the token was fetched > 50 hours? if no, then continue using this token
            token_details = json.load(token_file)
            token_load_dt_tm = datetime.datetime.strptime(
                token_details["timestamp"], "%m/%d/%Y, %H:%M:%S")

            if (datetime.datetime.now() - token_load_dt_tm).seconds < (50 * 3600):
                return

    # okay we either need to fetch a token from scratch or need a new one since the old one expired
    auth_params = {
        "username": api_def["username"],
        "password": api_def["password"]
    }

    auth_response = requests.post(
        url=urljoin(api_def["root_url"], api_def["api_defs"]["gen_token"]), data=auth_params)
    # please take a look at REST response codes - https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    if auth_response.status_code == 200:
        bearer_token = json.loads(
            auth_response.content.decode("utf-8"))["Document"]
        auth_token = {
            "token": bearer_token,
            "timestamp": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        }
        with open(token_file_path, "w") as f:
            json.dump(auth_token, f, indent=4)
    else:
        print("A problem occurred. Code: {}, Message: {}".format(
            auth_response.status_code, auth_response.content.decode("utf-8")))
        raise Exception("Problem with auth")


def get_global_daily_report(month: int, year: int):
    # get today's date information
    today = datetime.datetime.today()

    # check if the month is valid
    if month not in months.keys():
        raise Exception(
            "Invalid month range! please choose a month range between 1-12")

    # check if the date range supplied actually makes sense. Covid data is tabulated from Jan 2020 till today.
    if year < 2020 or year > today.year or (year == today.year and month > today.month):
        raise Exception(
            "Invalid date range! No valid data prior to Jan 2020 or in the future. Please choose a month and year between and including, Jan 2020 and current month and year")
    
    # connect to the server to get the data. we also need to 
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
