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