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
import pprint

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
    
    def get_result(self):
        rs = self.fetchall()
        if len(rs) == 1:
            return rs[0][0]
        else:
            return [r[0] for r in rs]

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
            self.execute("""drop table {}""".format(table))
        self.commit()

    # def backup_db(self):
    #     pass

    # def restore_db(self):
    #     pass

    # def dump_db_to_csv(self):
    #     '''serialize all tables to human-readable format'''
    #     pass
    
    def format_table(self, table_name=''):
        '''return the contents of the specified table as a formatted string'''
        self.execute("""select * from {}""".format(table_name))
        return pprint.pformat(self.fetchall())

    def get_tables(self):
        self.execute("""select name from sqlite_master where type = 'table'""")
        return self.get_result()
        
    def check_db(self):
        '''Function to sanity check that tables exist in the database'''
        tables = self.get_tables()
        if tables:
            return True
        else:
            return False

    def add_player(self, fullname, email='', phone=0):
        self.execute("""insert into player (fullname, email, phone) values ('{}', '{}', {})""".format(fullname, email, phone))
        self.commit()

    def get_player_id(self, fullname=None, email=None, phone=None, reddit=None, discord=None):
        if fullname:
            self.execute("""select id from player where fullname == '{}'""".format(fullname))
        elif email:
            self.execute("""select id from player where email == '{}'""".format(email))
        elif phone:
            self.execute("""select id from player where fullname == '{}'""".format(fullname))
        elif reddit:
            self.execute("""select id from player inner join reddit where player.id = reddit.player_id and reddit.account == '{}'""".format(reddit))
        elif discord:
            self.execute("""select id from player inner join discord where player.id = discord.player_id and discord.account == '{}'""".format(discord))
        return self.get_result()

    def associate_social_with_player(self, player_id, account, act_type):
        if act_type == 'reddit':
            self.execute("""insert into reddit (player_id, account) values ('{}', '{}')""".format(player_id, account))
        elif act_type == 'discord':
            self.execute("""insert into discord (player_id, account) values ('{}', '{}')""".format(player_id, account))
        else:
            print('unrecognized account type: {}'.format(act_type))

    def get_social_of_player(self, player_id, act_type):
        if act_type == 'discord':
            self.execute("""select account from discord where player_id == {}""".format(player_id))
        elif act_type == 'reddit':
            self.execute("""select account from reddit where player_id == {}""".format(player_id))
        else:
            print('unrecognized account type: {}'.format(act_type))
        return self.get_result()

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


