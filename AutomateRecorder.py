from pynput import mouse
from SqlHandler import SqlHandler
from pynput.mouse import Button, Controller
class AutomateRecorder:
    """
    This class provides functionality to record clicks and stores them in an sqlite db file
    the db can be later used to reproduce the same behavior
    An automate stops recording on press of middle mouse button
    """
    def __init__(self,name,desc,url):
        self.db_name = 'intel_auto.sqlite'
        
        with mouse.Listener( on_click = self.on_click) as listener:
            self.start_automation(SqlHandler(self.db_name),name,desc,url)
            print("Press Middle Mouse Button To Start Recording. Press it again to stop.")
            self.recording = False
            listener.join()
    

    """
    On click the current co-ordinates of the mouse are stored in db
    """
    def on_click( self, x , y , button , pressed ):
        if self.recording == True:
            # 1 is for left click 2 is for right click
            sql_handler = SqlHandler(self.db_name)
            if pressed and button ==  mouse.Button.left:
                self.seq_num += 1 
                sql_handler.store_event(self.auto_id,self.seq_num,1,x,y)

            elif pressed and button == mouse.Button.right:
                self.seq_num += 1 
                sql_handler.store_event(self.auto_id,self.seq_num,2,x,y)

            #END AUTOMATION ON middle mouse button CLICK
            elif pressed and button == mouse.Button.middle:
                self.end_automation(button,SqlHandler(self.db_name))
                self.recording = False
                print('Recording Stopped')
                return False
            else:
                return
        elif pressed and button == mouse.Button.middle and self.recording == False:
            print('Recording Mouse Clicks')
            self.recording = True

    """
    Starts a new automation session and initializes the sequence of events in the automation session
    """

    def start_automation(self,sql_handler,name,desc,url):
        self.auto_id = sql_handler.create_new_automation(name,desc,url)
        self.seq_num = 0
        sql_handler.close()
    

    """
    Termiates the automation and commits all the steps recorded
    """
    def end_automation(self,button,sql_handler):
        sql_handler.show_events(self.auto_id)
        sql_handler.close()