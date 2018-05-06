#player/game tracking database, needs to handle many data
#players, pcs, discord & reddit accounts
#tracking posts to players
#tracking players to games
#tracking games to posts
#tracking tokens (awarded, player)
#tracking player map
#wealth/inventory tracking
#experience tracking

import sqlite3

class Backend():
    '''Represents the database which contains game history and player status'''
    def __init__(self, name='game.db'):
        '''Create connection to sqlite database file on disk and initialize cursor to perform actions'''
        self.connection = sqlite3.connect(name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        
    def execute(self, command=''):
        ''''''
        self.cursor.execute(command)
    
    def fetchone(self):
        ''''''
        return self.cursor.fetchone()

    def fetchall(self):
        ''''''
        return self.cursor.fetchall()
    
    def commit(self):
        ''''''
        self.connection.commit()
    
    def close(self):
        ''''''
        self.connection.close()
        
    def initialize_db(self):
        ''''''
        # self.execute('''create table inventory (barcode integer, bgg_id integer)''')
        # self.execute('''create table history (barcode integer, wwid integer, time_out datetime, time_in datetime, auto_in integer)''')
        self.commit()
    
    def destroy_db(self):
        '''Drop the tables for inventory and history to effectively clear/reset database'''
        # try:
        #     self.execute('''drop table inventory''')
        # except sqlite3.OperationalError:
        #     pass
        # try:
        #     self.execute('''drop table history''')
        # except sqlite3.OperationalError:
        #     pass
        self.commit()
            
    def dump_to_csv(self, table_name='history'):
        '''Write the contents of the specified table to a csv file'''
        pass
    
    def format_table(self, table_name='history'):
        '''return the contents of the specified table as a formatted string'''
        self.execute('''select * from {}'''.format(table_name))
        return pp.pformat(self.fetchall())
        
    def reset_table(self):
        '''Reset/clear the contents of the specified table'''
        pass
        
    def get_history(self):
        ''''''
        return self.format_table('history')
    
    def get_inventory(self):
        ''''''
        return self.format_table('inventory')
        
    def check_db(self):
        '''Function to sanity check that tables exist in the database'''
        self.execute("""select name from sqlite_master where type = 'table'""")
        tables = self.fetchall()
        if tables:
            return True
        else:
            return False
