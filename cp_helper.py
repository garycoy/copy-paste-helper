#!/usr/bin/python3

# Reference: https://github.com/garycoy/copy-paste-helper/tree/main

# DO NOT CALL THIS DIRECTLY. It's meant to be called from
# cph or rc.

import sys
import os
import time

screen_sess = sys.argv[1]

command_file = sys.argv[2]

commands = open(f'./{command_file}').read().splitlines()
for one_command in commands:
    if one_command.startswith("COMMAND:"):
        final_command = one_command.replace("COMMAND:","")
        final_command = "$'" + final_command + "'"
        os.system("screen -S " + screen_sess + " -X stuff " + final_command)
        # last_action = "COMMAND"
    if one_command.startswith("RETURN:"):
        return_command = one_command.replace("RETURN:","")
        if return_command == "ASK":
            yes_no = input("Do you want to type the enter key [y/n]?: ")
            if yes_no == "":
                yes_no = "y"
            if yes_no == "y":
                os.system("screen -S " + screen_sess + " -X stuff \015" )
                with open("./cp_helper.log","a") as logfile:
                  logfile.write(time.strftime("%Y-%m-%d %H:%M:%S") + " => Executed: " + final_command + "\n")
        else:
            os.system("screen -S " + screen_sess + " -X stuff \015" )
            with open("./cp_helper.log","a") as logfile:
               logfile.write(time.strftime("%Y-%m-%d %H:%M:%S") + " => Executed: " + final_command + "\n")
