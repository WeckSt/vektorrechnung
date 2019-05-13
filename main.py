import json
import coordinatecheck


# Loading the coordinates
with open() as f:
    data = json.load(f)

# Input check
coordinatecheck.checkDataLength(data)
coordinatecheck.checkValidInput(data)

# Main program
result = 0.0

for count in range(len(data)):
    result += (data[count]["y"] + data[(count+1) % len(data)]["y"]) * (data[count]["x"] - data[(count+1) % len(data)]["x"])
result /= 2

print result
