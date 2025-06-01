import os
mode = "on"
if mode == "off":
    effect = "Rain".replace(" ", "%20")
    args = ["-silentlaunch-", "color=#000000", "colorMode=Single%20Color"]
    cmd = f"signalrgb://effect/apply/{effect}?{'^&'.join(args)}"
else:
    effect = "Solid Color".replace(" ", "%20")
    args = ["-silentlaunch-"]
    cmd = f"signalrgb://effect/apply/{effect}?{'^&'.join(args)}"
os.system("start " + cmd)