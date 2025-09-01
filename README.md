# copy-paste-helper

## Purpose/Overview:

cp_helper.py is designed for Linux.

cp_helper.py requires python3.

cp_helper.py or "copy paste helper" is a small utility that is designed to take a series of commands from a 'command file' and send the commands, one at a time, to a GNU screen session.  This is essentially running the commands in a session on the target linux host. The commands are sent one-at-a-time, and the user is prompted whether or not to send/hit return/enter after each command.

cp_helper.py relies on a valid installation of [GNU screen](https://www.gnu.org/software/screen/). It relies on the user having some knowledge of screen (starting new sessions, attaching, detaching, etc.)

## Installation


### cp_helper.py
On your target linux host, navigate to a desired landing location. E.g 'cd /home/someuser'.

Once in the desired landing location, run:

```
wget https://raw.githubusercontent.com/garycoy/copy-paste-helper/refs/heads/main/cp_helper.py
```

Alternatively, go to the URL: https://github.com/garycoy/copy-paste-helper and open the cp_helper.py file in your browser. Copy/paste the contents into cp_helper.py on your linux host.

Once cp_helper.py is on your linux host in the desired location, perform:

```
chmod 755 ./cp_helper.py
```
Make the .py file executable.

### rc
'rc' is sort for 'run command'. The 'rc' script leverages cp_helper.py to 'inject' or run a single command-line command in your screen session.

Perform the following to install:

Ensure you are in the same location as where you downloaded/stored cp_helper.py.

```
wget https://raw.githubusercontent.com/garycoy/copy-paste-helper/refs/heads/main/rc
chmod 755 rc
```
'rc' is a bash/shell script that calls cp_helper.py.

## Configuration

cp_helper.py (and rc) relies on a 'commands.txt' file. This file is just a text file with the commands you wish to run - in a particular format.

### commands.txt

commands.txt needs to be in a particular format for cp_helper.py to run correctly/successfully. commands.txt should be in the same location/directory as cp_helper.py.

The format is below:

```
COMMAND:<your command here>
RETURN:ASK
COMMAND:<another command here>
RETURN:ASK
COMMAND:<this command will run automatically - no enter>
RETURN:YES
```
Explanation:

The commands.txt should be comprised of "COMMAND:" lines and "RETURN:" lines.

Each command you wish to run should be prefaced with the text "COMMAND:".
Each command should be followed by a "RETURN:" line. This "RETURN:" line should be either:

RETURN:ASK
or
RETURN:YES

RETURN:ASK => ask the user if return/enter should be sent to GNU screen.

RETURN:YES => automatically hit the return/enter key after injecting the command

Example commands.txt:

```
COMMAND:pwd
RETURN:ASK
COMMAND:uname -a
RETURN:ASK
COMMAND:ls -ltr
RETURN:YES
```
The above example will inject 'pwd' onto the GNU screen command line, then prompt the user to hit return. It will inject 'uname -a' and prompt user for return/enter. Then it will inject 'ls -ltr' and automatically hit return/enter.

## Usage

Navigate to the directory where cp_helper.py resides. Build your commands.txt file (see section above).

### Build commands.txt
Some handy 'helpers' for quickly building your commands.txt are below. Start off with just a text file of the commands you wish to run.

Now, vi the file, and replace the beginning of each line with "COMMAND:":

```
# in vi:
:1,$s,^,COMMAND:,g
```
Save the file.

Perform the following awk command to add "RETURN:ASK" after each command line. Ask will be the 'default'. Any time you want to automatically hit return, replace ASK with YES in your commands.txt file.
```
awk '1;!(NR%1){print "RETURN:ASK";}' commands.txt > commands2.txt
mv commands2.txt commands.txt
```
### Executing cp_helper.py

cp_helper.py relies on GNU screen. Before running cp_helper.py, you will need a running screen session that cp_helper.py will utilize.

First attach to or open your GNU screen session. Open another terminal session (does not have to be a screen session) and perform the steps in this section. You want to have a 'split' screen where you can view both the GNU screen session and your newly opened session. Ensure you can see both terminal windows. You will be able to see the commands being 'injected' into the screen session when you run cp_helper.py.

Either launch a new screen session or retrieve the session number/id of the screen you wish to use:

```
screen -ls

There is a screen on:
        79999.pts-0.myhost   (Detached)
1 Socket in /var/run/screen/S-myuser.```
```

Obtain the id (in the example above 79999). You will use the id with cp_helper.py to send the commands to the correct screen/terminal session.

To run your commands file, perform the following (from the location where cp_helper.py resides):

```
./cp_helper.py <screen id>
```

Example:
```
./cp_helper.py 79999 <==== the id from 'screen ls' you wish to run against
```

**Note**: your commands.txt file must be in the same location as cp_helper.py.

You will see your commands 'appear' in the screen session. You will be prompted to hit 'enter' according to the content of your 'commands.txt' file. Hit enter as requested. Next command will be injected - rinse and repeat.

### Testing/troubleshooting

It is a good idea to use the 'crawl/walk/run' approach here. Do not start off running impactful, potentially dangerous commands in your 'commands.txt' file. Start off by 'crawling' and testing this with simple, innocuous commands that don't really do anything (eg. pwd, ls, echo, etc.).

Once you are comfortable with the execution/behavior of cp_helper.py - you can begin to introduce more impactful commands and workflows.
