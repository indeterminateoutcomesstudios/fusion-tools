import unittest
from datetime import datetime, date, time
from database import *

class BackendTest(unittest.TestCase): 
  
  def setUp(self):
    self.db = Backend('test.db')
    self.db.destroy_db()
    self.db.initialize_db()
    
  def tearDown(self):
    self.db.destroy_db()
    self.db.close()
    
  def test_formattable(self):
    o = self.db.format_table('game_status')
    self.assertListEqual(eval(o), [('R',1),('N',2),('F',3),('A',4),('S',5),('C',6),('D',7)])
    
  def test_checkdb(self):
    self.assertTrue(self.db.check_db())
    self.db.destroy_db()
    self.assertFalse(self.db.check_db())

  def test_player(self):
    # TODO: enforce uniqueness?
    self.db.add_player('John Doe','johndoe@example.com',5555555555)
    self.db.execute('select * from player where id == 1')
    f = self.db.fetchone()
    self.assertEqual(f, (1, 'John Doe', 'johndoe@example.com', 5555555555))
    pid = self.db.get_player_id(fullname='John Doe')
    self.assertEqual(pid, 1)
    pid = self.db.get_player_id(email='johndoe@example.com')
    self.assertEqual(pid, 1)
    pid = self.db.get_player_id(phone=6666666666)
    self.assertNotEqual(pid, 1)

    pid = self.db.get_player_id(fullname='John Doe')
    self.db.associate_social_with_player(pid, 'jdoe', 'reddit')
    reddit = self.db.get_social_of_player(pid, 'reddit')
    discord = self.db.get_social_of_player(pid, 'discord')
    self.assertEqual(reddit, 'jdoe')
    self.assertNotEqual(discord, 'jdoe')
    self.db.associate_social_with_player(pid, 'gijoe', 'discord')
    discord = self.db.get_social_of_player(pid, 'discord')
    self.assertEqual(discord, 'gijoe')
    self.db.associate_social_with_player(pid, 'frank', 'facebook')
    facebook = self.db.get_social_of_player(pid, 'facebook')
    self.assertEqual(facebook, [])

    new_pid = self.db.get_player_id(discord='gijoe')
    self.assertEqual(new_pid, pid)
    new_pid = self.db.get_player_id(reddit='jdoe')
    self.assertEqual(new_pid, pid)

  def test_game(self):
    # TODO: multiple games on the same day?
    d = date(2018,6,25)
    t = time(20,30,0)
    location = "1845 35th Ave, Hillsboro, OR 97116"
    vtt = False
    status = Request
    self.db.add_game(d, t, location, vtt, status)
    # self.db.add_game(d, t, location, vtt, status)
    games = self.db.get_all_games()
    self.assertEqual(games[0], (1, Request, datetime(2018, 6, 25, 20, 30), '1845 35th Ave, Hillsboro, OR 97116', 0))
    # self.assertEqual(games[1], (2, 'R', '2018-06-25 20:30:00', '1845 35th Ave, Hillsboro, OR 97116', 0))
    gid = self.db.get_game_id(d)
    self.assertEqual(gid, 1)

    self.db.update_game(gid, location='Underdark')
    self.db.update_game(gid, vtt=True)
    self.db.update_game(gid, status=Denied)
    self.db.update_game(gid, date=date(2018,6,26))
    self.db.update_game(gid, time=time(20,0,0))
    games = self.db.get_all_games()
    self.assertEqual(games[0], (1, Denied, datetime(2018, 6, 26, 20), 'Underdark', 1))
    self.db.update_game(gid, date=date(2018,7,7), time=time(22, 34, 0), location='Earth', vtt=False, status=Accepted)
    games = self.db.get_all_games()
    self.assertEqual(games[0], (1, Accepted, datetime(2018, 7, 7, 22, 34), 'Earth', 0))

    # dm connection
    self.db.add_player('Evil DM','edm@example.com',6666666666)
    self.db.add_player('Player A','pa@example.com',1111111111)
    self.db.add_player('Player B','pb@example.com',2222222222)
    self.db.add_player('Player C','pc@example.com',3333333333)
    pid = self.db.get_player_id(fullname='Evil DM')
    self.db.add_dm_to_game(pid, gid)

    # pc connection    
    pid = self.db.get_player_id(fullname='Player A')
    self.db.add_character_to_player(pid, 'Francis')
    cid = self.db.get_character_id(pid, 'Francis')
    self.db.add_character_to_game(cid, gid)

    pid = self.db.get_player_id(fullname='Player B')
    self.db.add_character_to_player(pid, 'Franklin')
    cid = self.db.get_character_id(pid, 'Franklin')
    self.db.add_character_to_game(cid, gid)

    pid = self.db.get_player_id(fullname='Player C')
    self.db.add_character_to_player(pid, 'Ferdinand')
    cid = self.db.get_character_id(pid, 'Ferdinand')
    self.db.add_character_to_game(cid, gid)

    # player + dm list from pcs
    attendees = self.db.get_attendees(gid)
    self.assertListEqual(attendees, [[1],[2,3,4]])

    self.db.add_game(d, t, location, True, status)
    gid = self.db.get_game_id(date=d, vtt=True)
    pid = self.db.get_player_id(fullname='Evil DM')
    self.db.add_dm_to_game(pid, gid)
    pid = self.db.get_player_id(fullname='Player A')
    cid = self.db.get_character_id(pid, 'Francis')
    self.db.add_character_to_game(cid, gid)
    attendees = self.db.get_attendees(gid)
    self.assertListEqual(attendees, [[1],[2]])

    # post connection
    # write-up connections
    # map connections
    # game status

  def test_character(self):
    self.db.add_player('Player A','pa@example.com',1111111111)
    pid = self.db.get_player_id(fullname='Player A')
    self.assertEqual(pid, 1)
    self.db.add_character_to_player(pid, 'Francis')
    pcs = self.db.get_characters(player_id=pid)
    self.assertEqual(pcs, [(1,'Francis')])
    # experience
    self.db.add_experience(pcs[0][0], exp=4000, game_id=1)
    self.db.add_experience(pcs[0][0], exp=4000, game_id=2)
    self.db.add_experience(pcs[0][0], exp=4000, game_id=3)
    exp = self.db.get_character_experience(pcs[0][0])
    self.assertEqual(exp, 12000)
    # wealth
    # TODO: online transaction date for when talking with merchant
    self.db.add_wealth(pcs[0][0], gold=100.25, game_id=1)
    self.db.add_wealth(pcs[0][0], gold=1000.25, game_id=1)
    self.db.add_wealth(pcs[0][0], gold=-200.0, game_id=2)
    cash = self.db.get_character_wealth(pcs[0][0])
    self.assertEqual(cash, 900.5)
    # inventory

if __name__ == '__main__': # pragma: no cover
  unittest.main()