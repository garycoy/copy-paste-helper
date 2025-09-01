# copy-paste-helper

```
 awk '1;!(NR%1){print "RETURN:ASK";}' commands.txt > commands2.txt
```

example commands.txt file:

```
COMMAND:pwd
RETURN:ASK
COMMAND:echo 'hello world'
RETURN:ASK
COMMAND:pmon
RETURN:YES

```
