# mouse_movement_recorder
Python program that can record mouse clicks and stores them in an SQLite database with the functionality to reproduce the clicks by reading from the database.

## Dependencies 
pynput
regex
webbrowser
sqlite3

## Functionality

This program can be used for UI automation. It is based upon pynput.

### Pros 
1. It is a code independent UI automation approach. It can be used for web as well as stand alone applications. pynput makes use of standard mouse functioinalities, thus making this approach OS independent.
2. Since there is no need of code, non-programmers can also use this to automate their work without the hassle of programming explicitly. All they need to do is record the session once and reuse it again and again.

## Cons
1. No dynamic wait between consecutive clicks that have been recorded as of yet.
2. Keyboard input functionality isn't provided yet.
3. The screen size used for automation has to be equal to the screen size where the script has to be re-run, thus making it a static approach. 

