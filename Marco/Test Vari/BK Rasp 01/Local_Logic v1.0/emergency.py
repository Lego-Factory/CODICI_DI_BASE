import buildhat

def kill():
    for char in ["A", "B", "C", "D"]:
        try:
            buildhat.Motor(char).stop()
        except buildhat.exc.DeviceInvalid:
            continue