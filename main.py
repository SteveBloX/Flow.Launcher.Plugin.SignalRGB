# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher

class RGB(FlowLauncher):

    def query(self, query):
        if query == "on":
            return [{
                "Title": "Enable RGB",
                "SubTitle": "Press enter to enable RGB lighting",
                "JsonRPCAction": {
                    "method": "enable_rgb",
                    "parameters": []
                },
            }]
        elif query == "off":
            return [{
                "Title": "Disable RGB",
                "SubTitle": "Press enter to disable RGB lighting",
                "JsonRPCAction": {
                    "method": "disable_rgb",
                    "parameters": []
                },
            }]
        return [
            
        ]

    """def context_menu(self, data):
        return [
            {
                "Title": "Hello World Python's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
                }
            }
        ]"""

    def enable_rgb(self):
        effect = "Rain".replace(" ", "%20")
        args = ["-silentlaunch-", "color=#000000", "colorMode=Single%20Color"]
        cmd = f"signalrgb://effect/apply/{effect}?{'^&'.join(args)}"
        os.system("start " + cmd)
    def disable_rgb(self):
            effect = "Solid Color".replace(" ", "%20")
            args = ["-silentlaunch-"]
            cmd = f"signalrgb://effect/apply/{effect}?{'^&'.join(args)}"
            os.system("start " + cmd)

if __name__ == "__main__":
    RGB()
