import time
from pypresence import Presence

with open("clientid") as clientIdFile:
    lines4542367 = clientIdFile.read()
    clientId = lines4542367.split('\n', 1)[0]
with open("state.txt") as stateFile:
    lines432578 = stateFile.read()
    userState = lines432578.split('\n', 1)[0]
with open("details.txt") as detailsFile:
    lines234578 = detailsFile.read()
    rpDetails = lines234578.split('\n', 1)[0]

rpc = Presence(clientId)
rpc.connect()

print("Connected to Discord!")

startTime = time.time()

while True:
    rpc.update(state=userState,details=rpDetails,large_image="large",start=startTime)
    time.sleep(10)
