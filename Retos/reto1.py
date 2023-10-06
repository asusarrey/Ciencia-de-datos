import urllib.request, json
url="https://gbfs.mex.lyftbikes.com/gbfs/gbfs.json"
with urllib.request.urlopen(url) as url:
    data = json.load(url)
    print(data)
