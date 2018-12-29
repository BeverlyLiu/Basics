import json
from urllib.request import urlopen

with urlopen("https://storage.googleapis.com/encode-experiments/streams/smoothstep/multibitrate/lp/sxsw/bitrate_master.json") as response:
    source = response.read()

print(source)

data = json.loads(source)

print(json.dumps(data, indent=2))

print("\nlen of qualities = ", len(data['qualities']), '\n')