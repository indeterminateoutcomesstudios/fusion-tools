#player/game tracking database, needs to handle many data
#players to discord & reddit accounts
#players to PCs
#tracking reddit posts to reddit accounts (and subsequently players + PCs)
#tracking players to games (thru PCs)
#tracking games to posts
#tracking tokens (awarded, player) to players and PCs
#tracking player map to posts and player contributors
#wealth/inventory tracking to PCs
#experience tracking to PCs

import sqlite3

Request = 'R'
Need_Players = 'N'
Party_Full = 'F'
Accepted = 'A'
Successful = 'S'
Cancelled = 'C'
Denied = 'D'

class Backend():
    '''Represents the database which contains game history and player status'''
    def __init__(self, name='game.db'):
        '''Create connection to sqlite database file on disk and initialize cursor to perform actions'''
        self.connection = sqlite3.connect(name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        
    def execute(self, command=''):
        self.cursor.execute(command)

    def executescript(self, script=''):
        if script:
            self.cursor.executescript(script)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def commit(self):
        self.connection.commit()
    
    def close(self):
        self.connection.close()
        
    def initialize_db(self, schema='schema.sqlite'):
        '''Read and create tables from sqlite schema definition'''
        with open(schema, 'rt') as sf:
            schema = sf.read()
        self.executescript(schema)
        self.commit()
    
    def destroy_db(self):
        '''Drop tables to effectively clear/reset database'''
        for table in self.get_tables():
            self.execute('''drop table {}'''.format(table))
        self.commit()

    def backup_db(self):
        pass

    def restore_db(self):
        pass

    def dump_db_to_csv(self):
        '''serialize all tables to human-readable format'''
        pass
    
    def format_table(self, table_name=''):
        '''return the contents of the specified table as a formatted string'''
        self.execute('''select * from {}'''.format(table_name))
        return pp.pformat(self.fetchall())
        
    def reset_table(self):
        '''Reset/clear the contents of the specified table'''
        pass

    def get_tables(self):
        self.execute("""select name from sqlite_master where type = 'table'""")
        ts = self.fetchall()
        return [t[0] for t in ts]
        
    def check_db(self):
        '''Function to sanity check that tables exist in the database'''
        tables = self.get_tables()
        if tables:
            return True
        else:
            return False

    def add_player(self, fullname, email='', phone=None):
        pass

    def associate_social_with_player(self, player_id, account, act_type):
        if act_type == 'reddit':
            pass
        elif act_type == 'discord':
            pass
        else:
            print('unrecognized account type: {}'.format(act_type))

    def add_game(self, status=Request):
        pass

    def update_game_status(self, game_id, status):
        pass

    def add_character_to_player(self, player_id, name):
        pass

    def award_tokens(self, num_tokens=1, tkn_type='player'):
        if tkn_type == 'player':
            pass
        elif tkn_type == 'author':
            pass
        else:
            print('unrecognized token type: {}'.formt(tkn_type))

    def transfer_tokens(self, giv_id, rec_id, num_tokens):
        if giv_id == rec_id:
            return

    def add_wealth(self, character_id, gold=0.0, date=None):
        pass

    def add_experience(self, character_id, exp=0, date=None):
        pass

    def add_inventory(self, character_id, name='', date=None):
        pass


