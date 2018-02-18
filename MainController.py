from AutomateRecorder import AutomateRecorder
from AutomateReplayer import AutomateReplayer
import sys
def record_automate():
    name  = raw_input('Enter a name for the automate - ')
    desc = raw_input('Enter a description for the automate - ')
    url = raw_input('Enter the url for the automate - ')
    automate_recorder = AutomateRecorder(name,desc,url)

def replay_automate():
    auto_id = int(raw_input('Enter the automation ID-'))
    automate_replayer = AutomateReplayer(auto_id)

if __name__ == '__main__':
    usr_io = 1
    while usr_io != 3:
        usr_io = int(raw_input('Select an operation -\n1: Record an automate \n2: Use automate\n3: Quit'))
        if usr_io == 1:
            record_automate()        
        elif usr_io == 2:
            replay_automate()