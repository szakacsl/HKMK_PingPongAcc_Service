import sys
import json

# create json file from processing images
# do some magic here
gsus = {
    "param1": 3,
    "param2": ["a", "b", "c"]
}

print(json.dumps(gsus))

