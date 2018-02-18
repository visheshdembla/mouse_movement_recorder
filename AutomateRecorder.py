from pynput import mouse
from SqlHandler import SqlHandler
from pynput.mouse import Button, Controller

class MouseException(Exception):
    pass

class AutomateRecorder():
    
    def __init__(self,name,desc,url):
        self.db_name = 'intel_auto.sqlite'
        
        with mouse.Listener(on_move = self.on_move, on_click = self.on_click, on_scroll = self.on_scroll) as listener:
            self.start_automation(SqlHandler(self.db_name),name,desc,url)
            listener.join()
    
    def on_move(self,x,y):
        #print("("+str(x)+","+str(y)+")")
        pass

    def on_scroll( self, x , y, dx, dy):
        #print("Scrolled - ("+str(x)+","+str(y)+")")
        pass
    def on_click( self, x , y , button , pressed ):

        # 1 is for left click 2 is for right click
        print("("+str(x)+","+str(y)+")")
        mouse1 = Controller()
        print("("+str(mouse1.position[0])+","+str(mouse1.position[1])+")")
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
            return False
        else:
            return

    

    def start_automation(self,sql_handler,name,desc,url):
        #Start a new automation session
        #Generate automation ID
        #Initialize sequence
        self.auto_id = sql_handler.create_new_automation(name,desc,url)
        self.seq_num = 0
        sql_handler.close()
    
    def end_automation(self,button,sql_handler):
        sql_handler.show_events(self.auto_id)
        sql_handler.close()
        

if __name__ == '__main__':
    name = 'Test'
    desc = 'Test Desc'
    url = 'www.google.com'
    mouse_manager = AutomateRecorder(name,desc,url)
