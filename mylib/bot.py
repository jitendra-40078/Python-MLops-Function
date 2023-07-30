import wikipedia

def scrape(name, length = 1):
    result = wikipedia.summary("Microsoft", sentences = length)
    return result