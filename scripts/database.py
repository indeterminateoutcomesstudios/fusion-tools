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

# https://stackoverflow.com/questions/3296040/why-arent-my-sqlite3-foreign-keys-working

import sqlite3
from datetime import datetime, date, time
import pprint
import logging
db_log = logging.getLogger(__name__)

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
        self.connection = sqlite3.connect(name, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
        self.cursor = self.connection.cursor()
        
    def execute(self, command='', values=()):
        self.cursor.execute(command, values)

    def executescript(self, script=''):
        if script:
            self.cursor.executescript(script)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def get_1_col_result(self):
        rs = self.fetchall()
        if len(rs) == 0:
            return []
        elif len(rs) == 1:
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
            self.execute("drop table {}".format(table))
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
        self.execute("select * from {}".format(table_name))
        return pprint.pformat(self.fetchall())

    def get_tables(self):
        self.execute("select name from sqlite_master where type = ?", ('table',))
        return [t[0] for t in self.fetchall()]
        
    def check_db(self):
        '''Function to sanity check that tables exist in the database'''
        tables = self.get_tables()
        if tables:
            return True
        else:
            return False

    def add_player(self, fullname, email='', phone=0):
        self.execute("insert into player (fullname, email, phone) values (?, ?, ?)", (fullname, email, phone))
        self.commit()

    def get_player_id(self, fullname=None, email=None, phone=None, reddit=None, discord=None):
        if fullname:
            self.execute("select id from player where fullname == ?", (fullname,))
        elif email:
            self.execute("select id from player where email == ?", (email,))
        elif phone:
            self.execute("select id from player where fullname == ?", (fullname,))
        elif reddit:
            self.execute("select id from player inner join reddit where player.id = reddit.player_id and reddit.account == ?", (reddit,))
        elif discord:
            self.execute("select id from player inner join discord where player.id = discord.player_id and discord.account == ?", (discord,))
        return self.get_1_col_result()

    def associate_social_with_player(self, player_id, account, act_type):
        if act_type == 'reddit':
            self.execute("insert into reddit (player_id, account) values (?, ?)", (player_id, account))
        elif act_type == 'discord':
            self.execute("insert into discord (player_id, account) values (?, ?)", (player_id, account))
        else:
            db_log.warning('\nunrecognized account type: {}'.format(act_type))

    def get_social_of_player(self, player_id, act_type):
        if act_type == 'discord':
            self.execute("select account from discord where player_id == {}".format(player_id))
        elif act_type == 'reddit':
            self.execute("select account from reddit where player_id == {}".format(player_id))
        else:
            db_log.warning('\nunrecognized account type: {}'.format(act_type))
        return self.get_1_col_result()

    def add_game(self, date=None, time=None, location='', vtt=False, status=Request):
        dt = datetime.combine(date, time)
        self.execute("insert into game (status, datetime, location, vtt) values (?, ?, ?, ?)", (status, dt, location, vtt))
        self.commit()

    def get_game_id(self, date=None, vtt=None):
        if date and vtt:
            self.execute("select id from game where datetime like '%{}%' and vtt = ?".format(date), (vtt,))
        elif date:
            self.execute("select id from game where datetime like '%{}%'".format(date))
        # elif vtt: # doesn't seem useful
        #     self.execute("select id from game where vtt = ?", (vtt,))
        return self.get_1_col_result()

    def get_all_games(self):
        self.execute("select * from game")
        return self.fetchall()

    def update_game(self, game_id, date=None, time=None, location=None, vtt=None, status=None):
        if date or time:
            if date and time:
                dt = datetime.combine(date, time)
            else:
                self.execute("select datetime from game where id = ?", (game_id,))
                old_dt = self.fetchall()[0][0]
                old_date = old_dt.date()
                old_time = old_dt.time()
                if date:
                    dt = datetime.combine(date, old_time)
                else:
                    dt = datetime.combine(old_date, time)
            self.execute("update game set (datetime) = (?) where id = ?", (dt, game_id))
        if location:
            self.execute("update game set (location) = (?) where id = ?", (location, game_id))
        if vtt != None:
            self.execute("update game set (vtt) = (?) where id = ?", (vtt, game_id))
        if status:
            self.execute("update game set (status) = (?) where id = ?", (status, game_id))
        self.commit()

    def add_dm_to_game(self, player_id, game_id):
        self.execute("insert into game_dms (game_id, dm_id) values (?, ?)", (game_id, player_id))
        self.commit()

    def add_character_to_game(self, character_id, game_id):
        self.execute("insert into game_pcs (game_id, character_id) values (?, ?)", (game_id, character_id))
        self.commit()

    def get_attendees(self, game_id):
        dm_ids = self.get_dms(game_id)
        if not isinstance(dm_ids, list):
            dm_ids = [dm_ids]
        player_ids = self.get_players_of_game(game_id)
        if not isinstance(player_ids, list):
            player_ids = [player_ids]
        return [dm_ids, player_ids]

    def get_dms(self, game_id):
        self.execute("select id from player inner join game_dms where player.id = game_dms.dm_id and game_dms.game_id == ?", (game_id,))
        return self.get_1_col_result()

    def get_players_of_game(self, game_id):
        self.execute("select player_id from character inner join game_pcs where character.id = game_pcs.character_id and game_pcs.game_id == ?", (game_id,))
        return self.get_1_col_result()

    def add_character_to_player(self, player_id, name):
        self.execute("insert into character (player_id, name) values (?, ?)", (player_id, name))
        self.commit()

    def get_character_id(self, player_id, name):
        self.execute("select id from character where player_id = ? and name = ?", (player_id, name))
        return self.get_1_col_result()

    def get_characters(self, player_id):
        self.execute("select id, name from character where player_id == ?", (player_id,))
        pcs = self.fetchall()
        return pcs

    def award_tokens(self, num_tokens=1, tkn_type='player'):
        if tkn_type == 'player':
            pass
        elif tkn_type == 'author':
            pass
        else:
            db_log.warning('\nunrecognized token type: {}'.formt(tkn_type))

    def transfer_tokens(self, giv_id, rec_id, num_tokens):
        if giv_id == rec_id:
            return

    def add_wealth(self, character_id, gold=0.0, game_id=None):
        self.execute("insert into wealth (character_id, game_id, gold_value) values (?, ?, ?)", (character_id, game_id, gold))
        self.commit()

    def get_character_wealth(self, character_id):
        self.execute("select * from wealth where character_id == ?", (character_id,))
        txs = self.fetchall()
        total = 0.0
        for tx in sorted(txs, key=lambda x: x[1]): #sorting by game number...perhaps by date would be better
            total += tx[2]
        return total

    def add_experience(self, character_id, exp=0, game_id=None):
        self.execute("insert into experience (character_id, game_id, amount) values (?, ?, ?)", (character_id, game_id, exp))
        self.commit()

    def get_character_experience(self, character_id):
        self.execute("select * from experience where character_id == ?", (character_id,))
        txs = self.fetchall()
        total = 0
        for tx in sorted(txs, key=lambda x: x[1]): #sorting by game number...perhaps by date would be better
            total += tx[2]
        return total

    def add_inventory(self, character_id, name='', game_id=None):
        self.execute("insert into inventory (character_id, game_id, name) values (?, ?, ?)", (character_id, game_id, name))
        self.commit()


