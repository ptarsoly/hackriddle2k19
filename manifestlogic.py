import json
import os
import sys

manifest = []

def allocate_seat(passenger, seats, groups):
    for s in seats:
        if passenger["class"] == "first" and s["id"] in groups["groupfirst"]:
            if passenger["seat"] == s["type"] and s["status"] == "free" :
                s["status"] = passenger["id"]
                print ("first")
                seat = {"passenger": passenger["id"], "number": s["id"]}
                manifest.append(seat)
                return
        if passenger["priority"] == "yes" and s["id"] in groups["group0"]:
            if passenger["seat"] == s["type"] and s["status"] == "free":
                s["status"] = passenger["id"]
                print ("priority")
                seat = {"passenger": passenger["id"], "number": s["id"]}
                manifest.append(seat)
                return

        if passenger["priority"] == "no" and s["id"] not in groups["groupfirst"] and s["id"] not in groups["group0"] and passenger["class"] == "economy":
            if passenger["bags"] == "1" and s["id"] in groups["bagged"]:
                if passenger["seat"] == s["type"] and s["status"] == "free":
                    s["status"] = passenger["id"]
                    print ("bagged")
                    seat = {"passenger": passenger["id"], "number": s["id"]}
                    manifest.append(seat)
                    return
            else:
                if passenger["seat"] == s["type"] and s["status"] == "free":
                    s["status"] = passenger["id"]
                    print ("unbagged")
                    seat = {"passenger": passenger["id"], "number": s["id"]}
                    manifest.append(seat)
                    return
        
    


passengerfile = sys.argv[1]
seatfile =  sys.argv[2]
groupfile = sys.argv[3]

with open(passengerfile) as f:
    passengers = json.load(f)

with open(groupfile) as f:
    groups = json.load(f)


with open(seatfile) as f:
    seats = json.load(f)

for p in passengers:
    print (p["priority"])
    allocate_seat(p, seats, groups)

##print (seats)

manifest_json = json.dumps(manifest)

print (manifest_json)

with open("manifest.json","w") as f:
  f.write(manifest_json)






