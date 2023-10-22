# Who's Online?
# https://www.codewars.com/kata/5b6375f707a2664ada00002a

# ------------------------ Olesia ------------------------
def who_is_online(friends):
    result = {}
    online , offline, away = [], [], []

    for a in friends:
        if a["status"] == "online" and a["last_activity"] <= 10:
            online.append(a["username"])
        if a["status"] == "offline":
            offline.append(a["username"])
        if a["last_activity"] > 10 and a["status"] == "online":
            away.append(a["username"])

    if len(online) >= 1:
        result["online"] = online
    if len(offline) >= 1:
        result["offline"] = offline
    if len(away) >= 1:
        result["away"] = away
    return result

# ------------------------ Mariia ------------------------
def who_is_online(friends):
    names_dict = {
        "online": [],
        "offline": [],
        "away": []
    }
    for x in friends:
        if x["status"] == 'online' and x["last_activity"] <= 10:
            names_dict["online"].append(x["username"])
        elif x["status"] == 'online' and x["last_activity"] > 10:
            names_dict["away"].append(x["username"])
        else:
            names_dict["offline"].append(x["username"])
            
    if names_dict["online"] == []:
        names_dict.pop("online")
    if names_dict["offline"] == []:
        names_dict.pop("offline")
    if names_dict["away"] == []:
        names_dict.pop("away")
            
    return names_dict