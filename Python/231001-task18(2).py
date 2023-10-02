
#Extract the domain name from a URL
# https://www.codewars.com/kata/514a024011ea4fb54200004b

# ------------------ Slava -----------------------
def domain_name(url):
    start = max(url.find('www.') + 4, url.find('://') + 3) if url.find('www.') != -1 or url.find('://') != -1 else 0
    end = url.find('.', start)
    return url[start:end]