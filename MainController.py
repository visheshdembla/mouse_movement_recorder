"""
A program that can be used to perform automation based on mouse clicks

Advantages -
UI independent

Limitations - 
No mechanism to induce wait between steps. 


Future Work -
- Provide Wait Based Automation by recording the time that is required to open up a webpage or a UI
"""

from AutomateRecorder import AutomateRecorder
from AutomateReplayer import AutomateReplayer
import re
import webbrowser
def record_automate():
    name  = raw_input('Enter a name for the automate - ')
    desc = raw_input('Enter a description for the automate - ')
    url = raw_input('Enter the url for the automate - ')
    url_pattern = '^[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU|corp|in|co)$'
    if re.match(url_pattern , url) is not None:
        webbrowser.open(url)
    else:
        print('Invalid URL')
    
    automate_recorder = AutomateRecorder(name,desc,url)

def replay_automate():
    auto_id = int(raw_input('Enter the automation ID-'))
    automate_replayer = AutomateReplayer(auto_id)

if __name__ == '__main__':
    usr_io = 1
    while usr_io != 3:
        usr_io = int(raw_input('Select an operation -\n1: Record an automate \n2: Use automate\n3: Quit\nc'))
        if usr_io == 1:
            record_automate()        
        elif usr_io == 2:
            replay_automate()