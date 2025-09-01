#!/usr/bin/python3

import subprocess
import sys

screen_sess = sys.argv[1]

commands = open("./commands.txt").read().splitlines()
for one_command in commands:
    final_command = one_command.split(":")[1]
    if one_command.startswith("COMMAND:"):
        subprocess.call(["screen", "-S", screen_sess, "-X", "stuff", final_command])
        # last_action = "COMMAND"
    if one_command.startswith("RETURN:"):
        # last_action = "RETURN"
        if final_command == "ASK":
            yes_no = input("Do you want to type the enter key [y/n]?: ")
            if yes_no == "":
                yes_no = "y"
            if yes_no == "y":
                subprocess.call(["screen", "-S", screen_sess, "-X", "stuff", "\015"])
        else:
            subprocess.call(["screen", "-S", screen_sess, "-X", "stuff", "\015"])
