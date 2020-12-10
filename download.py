import requests

sheet_id = 1nshYGWLb-YrsiQIjRWJpoa6qAOi2Qra4xZ2ri1t3Osg
url_pattern = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid="

files = {
    "0": "scores.csv",
    "1000391055": "games.csv",
    "500264802": "rounds.csv",
    "429667429": "continent.csv"
}

for index, name in files.items():
    with open(f"data/{name}", "w") as f:
        response = requests.get(f"{url_pattern}{index}")
        f.write(str(response.content, "utf-8"))