import unittest
from credentials import read_credentials

class CredentialsTest(unittest.TestCase): 
  def test_read(self):
    c = read_credentials('test')
    self.assertEqual(c['test']['client_id'], 'deadbeef')
    self.assertEqual(c['test']['client_secret'], 'blah blah whoanelly-77777777.123123Az')

if __name__ == '__main__': # pragma: no cover
  unittest.main()