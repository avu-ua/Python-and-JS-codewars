
#Extract the domain name from a URL
# https://www.codewars.com/kata/514a024011ea4fb54200004b

# ------------------ Slava -----------------------
def domain_name(url):
    start = max(url.find('www.') + 4, url.find('://') + 3) if url.find('www.') != -1 or url.find('://') != -1 else 0
    end = url.find('.', start)
    return url[start:end]

# ------------------------ Mariia ------------------------
import re
def domain_name(url):
    if re.findall("www", url):
        return re.findall(r"www.\w*", url)[0][4::]
    if re.findall(r"\/\/", url):
        return re.findall(r"[\/][\w,-]*\.", url)[0][1:-1]
    return re.findall(r"\w*\.", url)[0][:-1]

# ------------------------ Olesia ------------------------
def domain_name(url):
    if "http://" in url:
        url = url.replace("http://", "")
    elif "https://" in url:
        url = url.replace("https://", "")
    elif "http://www." in url:
        url = url.replace("http://www.", "")
    if "www." in url:
        url = url.replace("www.", "")
    end_index = url.find(".")
    result = url[:end_index]
    return result