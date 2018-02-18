from pynput.mouse import Button , Controller
from SqlHandler import SqlHandler
from time import sleep
import math
class AutomateReplayer():
    
    
    def __init__(self,auto_id):
        self.db_name = 'intel_auto.sqlite'
        self.sql_handler = SqlHandler(self.db_name)
        self.mouse = Controller()
        self.auto_id = auto_id
        self.events = self.sql_handler.get_events(self.auto_id)
       
        for i in range(len(self.events)):
            event = self.events[i][1]
            x_co = self.events[i][2]
            y_co = self.events[i][3]
            sleep(2)
            self.perform_event(event,x_co,y_co)
        
        
    """ 
    Function to perform the mouse operation stored in the database
    1 : Left Click 
    2 : Right Click
    3 : Enter Data (TO-DO)
    Before performing operation, the mouse position is set to the x,y pos
    X and Y co-ordinates are divided by a factor of 1.25 to avoid the scale down done by pynput
    """ 
    def perform_event(self, event , x_co , y_co):
        
        x_co = int((x_co / 1.25))
        y_co = int((y_co / 1.25))
        print(x_co)
        print(y_co)
        self.mouse.position = (x_co , y_co)
        if event == 1:
            self.mouse_click(Button.left)
        elif event == 2:
            self.mouse_click(Button.right)
        else:
           pass


    def mouse_click(self, button):
        self.mouse.press(button)
        self.mouse.release(button)


if __name__ == '__main__':
    event_replay = AutomateReplayer(10)
        