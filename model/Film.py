from .Koneksi import Koneksi
from datetime import datetime

class Film:
  def __init__(self) -> None:
    self.koneksi = Koneksi()

  def getAll(self):
    film = []
    for id in self.koneksi.db:
      doc = self.koneksi.db[id]
      if doc['tipe'] == 'film':
        film.append(doc)

    return film
  
  def getByDate(self):
    film = []
    tanggal_sekarang = datetime.now().strftime("%d-%m-%Y")
    for id in self.koneksi.db:
      doc = self.koneksi.db[id]
      if doc['tipe'] == 'film' and doc['tanggal_mulai'] <= tanggal_sekarang <= doc['tanggal_selesai']:
        film.append(doc)
    
    return film
  
  def getById(self, id):
    film = self.koneksi.db[id]
    return film
  
  def create(self, doc):
    self.koneksi.db.create(doc)
  
  def update(self, doc):
    self.koneksi.db.save(doc)

  def delete(self, doc):
    self.koneksi.db.delete(doc)
  
  def getByTitle(self, title):
    films = self.getAll()
    for film in films:
      if film["judul"] == title:
        return film
    return None