import sqlite3

class SqlHandler():
    
    def __init__(self , sql_file):
        self.conn = sqlite3.connect(sql_file)
        self.table_name = 'autom_data_table'
        self.cur = self.conn.cursor()

        #Check if table doesn't exist and create one
        self.cur.execute("SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = '"+self.table_name+"'")
        row_count = self.cur.fetchall()
        if row_count[0][0] == 0 :
            self.create_tables()
    
    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_tables(self):
        self.create_autom_table()
        self.create_event_table()

    def create_autom_table(self):
        tn = self.table_name
        pid = 'id'
        name='name'
        desc='desc'
        url='url'
        self.cur.execute("CREATE TABLE {tn} ( {id} INTEGER PRIMARY KEY AUTOINCREMENT, {name} CHAR(50) NOT NULL , {desc} TEXT NOT NULL , {url} TEXT NOT NULL )".format(tn=tn,id=pid,name=name,desc=desc,url=url))
        self.conn.commit()

    def create_event_table(self):
        tn = 'event_data_table'
        pid = 'id'
        seq_num = 'seq_id'
        auto_id = 'auto_id'
        event_id = 'event_id'
        x_co = 'x_co'
        y_co = 'y_co'
        string_data = 'data'
        self.cur.execute("CREATE TABLE {tn} ( {id} INTEGER PRIMARY KEY AUTOINCREMENT,{auto_id} INTEGER NOT NULL , {sq} INTEGER NOT NULL ,  {eve} INTEGER NOT NULL , {x} INTEGER NOT NULL , {y} INTEGER NOT NULL , {data} CHAR(100) NOT NULL DEFAULT '') ".format(tn=tn,sq=seq_num,eve=event_id,x=x_co,y=y_co,data=string_data,auto_id=auto_id,id=pid))
        self.conn.commit()

    def create_new_automation(self,name_val,desc_val,url_val):
        name = 'name'
        desc = 'desc'
        url = 'url'
        self.cur.execute("INSERT INTO {tn} ({name} , {desc} , {url}) values('{name_val}','{desc_val}','{url_val}')".format(tn=self.table_name,name=name,desc=desc,url=url,name_val=name_val,desc_val=desc_val,url_val=url_val))
        self.conn.commit()
        self.cur.execute("SELECT * FROM {tn}".format(tn=self.table_name))
        rows = self.cur.fetchall()
        return rows[len(rows)-1][0]



    def store_event(self , auto_id_val , seq_num_val, eve_id_val , x_val , y_val , data_val=None):
        tn='event_data_table'
        seq_num = 'seq_id'
        auto_id = 'auto_id'
        event_id = 'event_id'
        x_co = 'x_co'
        y_co = 'y_co'
        string_data = 'data'
        
        if data_val is not None:
            insert_query = "INSERT INTO {tn} ({auto},{sq},{eve},{x},{y},{data}) values({auto_val},{sq_val},{eve_val},{x_val},{y_val},'{data_val}')".format(tn=tn,eve=event_id,x=x_co,y=y_co,eve_val=eve_id_val,x_val=x_val,y_val=y_val,auto=auto_id,sq=seq_num,auto_val = auto_id_val,sq_val=seq_num_val,data=string_data,data_val=data_val)
        else:
            insert_query = "INSERT INTO {tn} ({auto},{sq},{eve},{x},{y}) values({auto_val},{sq_val},{eve_val},{x_val},{y_val})".format(tn=tn,eve=event_id,x=x_co,y=y_co,eve_val=eve_id_val,x_val=x_val,y_val=y_val,auto=auto_id,sq=seq_num,auto_val = auto_id_val,sq_val=seq_num_val)
        
        self.cur.execute(insert_query)
        self.conn.commit()

    def get_events(self,auto_id_val):
        auto_id = 'auto_id'
        out = []
        self.cur.execute("SELECT * FROM 'event_data_table' WHERE {auto} ='{auto_id_val} '".format(auto=auto_id,auto_id_val=auto_id_val))
        data  = self.cur.fetchall()
        #print("Automation Num - {auto}".format(auto=data[0][1]))
        for i in range(len(data)):
            #print("\nSeq Num:{seq}\nEvent:{event}\n(x,y):({x},{y})\n".format(seq=data[i][2],event=data[i][3],x=data[i][4],y=data[i][5]))
            out.append(data[i][2:])
        return out

    def show_events(self, auto_id_val):
        auto_id = 'auto_id'
        
        self.cur.execute("SELECT * FROM 'event_data_table' WHERE {auto} ='{auto_id_val} '".format(auto=auto_id,auto_id_val=auto_id_val))
        data  = self.cur.fetchall()
        print("Automation Num - {auto}".format(auto=data[0][1]))
        for i in range(len(data)):
            print("\nSeq Num:{seq}\nEvent:{event}\n(x,y):({x},{y})\n".format(seq=data[i][2],event=data[i][3],x=data[i][4],y=data[i][5]))
            
        



""" Main"""
if __name__=='__main__':
    sql = SqlHandler('sample2.sqlite')
    print(sql.create_new_automation("hello,auto","new auto","www.google.com"))
