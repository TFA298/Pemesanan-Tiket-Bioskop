from .FilmPage import FilmPage
from .TiketPage import TiketPage
from .AdminPage import AdminPage

class HomePage:
  def __init__(self):
    self.film_page = FilmPage()
    self.tiket_page = TiketPage()
    self.admin_page = AdminPage()

  def view(self):
    while True:
      print('===== CINEMA 23 =====')
      print('[1] LIHAT DAFTAR FILM')
      print('[2] CARI FILM')
      print('[3] PESAN TIKET')
      print('[0] KELUAR')
      print('---------------------')
      pilih = int(input('PILIH MENU: '))

      if pilih == 1:
        self.daftarFilm()
      elif pilih == 2:
        self.cariFilm()
      elif pilih == 3:
        self.pesanTiket()  
      elif pilih == 9:
        self.admin_page.home()
      elif pilih == 0:
        break
      else:
        print('MENU TIDAK DITEMUKAN!')

  def daftarFilm(self):
    while True:
      print('===== DAFTAR FILM =====')
      self.film_page.listFilm()
      print("[0] KELUAR")
      print('-----------------------')
      pilih = int(input("LIHAT DETAIL FILM: "))
      if pilih > 0 and pilih <= len(self.film_page.daftar_film):
        self.film_page.detailFilm(pilih-1)
      elif pilih == 0:
        break
      else:
        print('OPSI TIDAK DITEMUKAN!')
  
  def pesanTiket(self):
    while True:
      print('===== PESAN TIKET =====')
      self.film_page.listFilm(with_price=True)
      print("[0] KELUAR")
      print('-----------------------')
      pilih = int(input("PILIH FILM: "))
      if pilih > 0 and pilih <= len(self.film_page.daftar_film):
        self.tiket_page.buatTiket(pilih-1)
      elif pilih == 0:
        break
      else:
        print('OPSI TIDAK DITEMUKAN!')

  def cariFilm(self):
    print("===== CARI FILM =====")
    title = input("MASUKKAN JUDUL FILM :")
    self.film_page.searchFilm(title)