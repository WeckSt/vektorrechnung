import sys


def checkDataLength(data):
    if len(data) <= 2:
        print "Not enough data given. At least 3 coordinates are needed".encode("utf-8")
        sys.exit(2)

def checkValidInput(data):
    for coordinate in data:
        if isinstance(coordinate["x"], float) is False or isinstance(coordinate["y"], float) is False:
            print "The used Coordinates are faulty"
            sys.exit(2)
