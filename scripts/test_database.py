import unittest
from database import Backend

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
    pass

  def test_character(self):
    pass

if __name__ == '__main__': # pragma: no cover
  unittest.main()