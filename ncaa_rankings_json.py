"""
    ESPN NCAA Football API

    Final Variables
    ---------------
    rankings: list of dictionaries
        Current teams in the top 25 rankings.

        Currently only using the College Football Playoff Committee rankings
        but need to pull and store the rest that are given from this API.

    dropped_out: list of dictionaries
        Teams that have dropped out of the top 25 rankings.
"""
import requests, json

url = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/rankings"

response = requests.get(url)
data = json.loads(response.text)

# with open("espn_col_foot.json", "r") as thing:
#     data = json.load(thing)

# ------------- admin data
# TODO: pull and store data from "AP Top 25" and "AFCA Coaches Poll"
ranking_committee = data["availableRankings"][0]["name"]
current_season_year = data["latestSeason"]["year"]
current_season_start = data["latestSeason"]["startDate"]
current_season_end = data["latestSeason"]["endDate"]
current_season_latest_week = data["latestWeek"]["number"]
ranking_headline = data["rankings"][0]["headline"]

print(
    f"{ranking_headline}\n"
    f"Ranking Committee: {ranking_committee}\n"
    f"Year: {current_season_year}\n"
    f"Season Start: {current_season_start}\n"
    f"Season End: {current_season_end}\n"
    f"Current Week: {current_season_latest_week}\n"
)


# ------------- sports data
league = data["leagues"][0]["name"]

# ------------- current rankings
rankings = []
for i in range(len(data["rankings"][0]["ranks"])):
    current_rank = data["rankings"][0]["ranks"][i]["current"]
    previous_rank = data["rankings"][0]["ranks"][i]["previous"]
    trend = data["rankings"][0]["ranks"][i]["trend"]
    location = data["rankings"][0]["ranks"][i]["team"]["location"]
    name = data["rankings"][0]["ranks"][i]["team"]["name"]
    nickname = data["rankings"][0]["ranks"][i]["team"]["nickname"]
    abbreviation = data["rankings"][0]["ranks"][i]["team"]["abbreviation"]
    color = data["rankings"][0]["ranks"][i]["team"]["color"]
    record = data["rankings"][0]["ranks"][i]["recordSummary"]

    team_dict = {
        "current_rank": current_rank,
        "previous_rank": previous_rank,
        "trend": trend,
        "location": location,
        "name": name,
        "nickname": nickname,
        "abbreviation": abbreviation,
        "color": color,
        "record": record,
    }
    rankings.append(team_dict)

for team in rankings:
    print(
        f"{team['current_rank']}. {team['location']} {team['name']} ({team['record']}) Trend:{team['trend']}"
    )

# ------------- teams that dropped out of the rankings
dropped_out = []
for i in range(len(data["rankings"][0]["droppedOut"])):
    previous_rank = data["rankings"][0]["droppedOut"][i]["previous"]
    location = data["rankings"][0]["droppedOut"][i]["team"]["location"]
    name = data["rankings"][0]["droppedOut"][i]["team"]["name"]
    nickname = data["rankings"][0]["droppedOut"][i]["team"]["nickname"]
    abbreviation = data["rankings"][0]["droppedOut"][i]["team"]["abbreviation"]
    color = data["rankings"][0]["droppedOut"][i]["team"]["color"]
    record = data["rankings"][0]["droppedOut"][i]["recordSummary"]

    team_dict = {
        "previous_rank": previous_rank,
        "trend": trend,
        "location": location,
        "name": name,
        "nickname": nickname,
        "abbreviation": abbreviation,
        "color": color,
        "record": record,
    }
    dropped_out.append(team_dict)

print(f"\nDropped Teams")
for team in dropped_out:
    print(
        f"Previous Rank: {team['previous_rank']}. {team['location']} {team['name']} ({team['record']})"
    )
