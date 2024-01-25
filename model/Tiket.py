from .Koneksi import Koneksi
from datetime import datetime

class Tiket:
  def __init__(self):
    self.koneksi = Koneksi()

  def getByMonth(self):
    tiket = []
    bulan_sekarang = datetime.now().month
    for id in self.koneksi.db:
      doc = self.koneksi.db[id]
      if doc['tipe'] == 'tiket':
        tanggal = datetime.strptime(doc['tanggal'], "%d-%m-%Y %H:%M:%S")
        if tanggal.month == bulan_sekarang:
          tiket.append(doc)

    return tiket

  def create(self, doc):
    self.koneksi.db.create(doc)