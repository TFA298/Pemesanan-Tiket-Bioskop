import couchdb
from env import DATABASE, URL
from seeder import seeder

class Koneksi:
  def __init__(self):
    self.server = couchdb.Server(URL)

    if DATABASE in self.server:
      self.db = self.server[DATABASE]
    else:
      self.db = self.server.create(DATABASE)
      for seed in seeder['docs']:
        self.db.create(seed)
