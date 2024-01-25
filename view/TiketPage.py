from .FilmPage import FilmPage
from datetime import datetime
from model.Tiket import Tiket

class TiketPage:
  def __init__(self):
    self.film_page = FilmPage()
    self.tiket = Tiket()
    self.semua_kursi = [
      'A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5',
      'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5'
    ]

  def buatTiket(self, index):
    film = self.film_page.daftar_film[index]
    pilih = -1
    print('===== JADWAL FILM =====')
    self.film_page.jadwalFilm(film['_id'])
    print("[0] KELUAR")
    while pilih < 0 or pilih > len(self.film_page.daftar_jadwal):
      print('-----------------------')
      pilih = int(input("PILIH JADWAL FILM: "))
      if pilih < 0 or pilih > len(self.film_page.daftar_jadwal):
        print('OPSI TIDAK DITEMUKAN!')
    
    if pilih != 0:
      jadwal = self.film_page.daftar_jadwal[pilih-1]
      jumlah_tiket = int(input("JUMLAH TIKET: "))
      for i in range(jumlah_tiket):
        print(f"TIKET-{i+1}")
        kursi_terisi = film['jadwal'][jadwal]['kursi']
        kursi_tersedia = sorted(list(set(self.semua_kursi) - set(kursi_terisi)))
        tiket = {
          "tipe": "tiket",
          "tanggal": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
          "judul": film['judul'],
          "jadwal": jadwal,
          "harga": film['harga'],
          "studio": film['jadwal'][jadwal]['studio'],
        }
        for i, kursi in enumerate(kursi_tersedia):
          print(f"[{i+1}] {kursi}")
        print('-----------------------')
        pilih_kursi = int(input("PILIH KURSI: "))
        tiket['kursi'] = kursi_tersedia[pilih_kursi-1]
        self.tiket.create(tiket)
        film['jadwal'][jadwal]['kursi'].append(kursi_tersedia[pilih_kursi-1])
      
      total_bayar = film['harga'] * jumlah_tiket
      print(f"TOTAL BAYAR: {total_bayar}")
      print("TERIMA KASIH ATAS PESANANNYA")
      self.film_page.film.update(film)

