from model.Film import Film
from datetime import datetime

class FilmPage:
  def __init__(self):
    self.film = Film()
    self.daftar_film = self.film.getByDate()

  def listFilm(self, with_price=False):
    for i, film in enumerate(self.daftar_film):
      if with_price:
        print(f"[{i+1}] {film['judul'].upper()}\t| Rp.{film['harga']}")
      else:
        print(f"[{i+1}] {film['judul'].upper()}")
      
  def jadwalFilm(self, id):
    film = self.film.getById(id)
    self.daftar_jadwal = []
    waktu_sekarang = datetime.now().strftime("%H:%M")
    for key, value in film['jadwal'].items():
      if key >= waktu_sekarang:
        self.daftar_jadwal.append(key)
        print(f"[{len(self.daftar_jadwal)}] {key}")

  def kursiStudio(self, id, jadwal):
    film = self.film.getById(id)
    return film['jadwal'][jadwal]
  
  def detailFilm(self, index):
    film = self.daftar_film[index]
    jenis_film = [film['jenis_film']] if isinstance(film['jenis_film'], str) else film['jenis_film']
    produser = [film['produser']] if isinstance(film['produser'], str) else film['produser']
    sutradara = [film['sutradara']] if isinstance(film['sutradara'], str) else film['sutradara']
    produksi = [film['produksi']] if isinstance(film['produksi'], str) else film['produksi']
    casts = [film['casts']] if isinstance(film['casts'], str) else film['casts']

    print('===== DETAIL FILM =====')
    print(f"JUDUL           : {film['judul'].upper()}")
    print(f"JENIS FILM      : {', '.join([jenis.upper() for jenis in jenis_film])}")
    print(f"DURASI | RATING : {film['durasi']} MENIT | {film['rating_usia']}")
    print(f"PRODUSER        : {', '.join([jenis.upper() for jenis in produser])}")
    print(f"SUTRADARA       : {', '.join([jenis.upper() for jenis in sutradara])}")
    print(f"PRODUKSI        : {', '.join([jenis.upper() for jenis in produksi])}")
    print(f"CASTS           : {', '.join([jenis.upper() for jenis in casts])}")
    print(f"SINOPSIS        : {film['sinopsis']}")
    
  def searchFilm(self, title):  
    film = self.film.getByTitle(title) 
    if film: 
      jenis_film = [film['jenis_film']] if isinstance(film['jenis_film'], str) else film['jenis_film']
      produser = [film['produser']] if isinstance(film['produser'], str) else film['produser']
      sutradara = [film['sutradara']] if isinstance(film['sutradara'], str) else film['sutradara']
      produksi = [film['produksi']] if isinstance(film['produksi'], str) else film['produksi']
      casts = [film['casts']] if isinstance(film['casts'], str) else film['casts']
      
      print('===== DETAIL FILM =====')
      print(f"JUDUL           : {film['judul'].upper()}")
      print(f"JENIS FILM      : {', '.join([jenis.upper() for jenis in jenis_film])}")
      print(f"DURASI | RATING : {film['durasi']} MENIT | {film['rating_usia']}")
      print(f"PRODUSER        : {', '.join([jenis.upper() for jenis in produser])}")
      print(f"SUTRADARA       : {', '.join([jenis.upper() for jenis in sutradara])}")
      print(f"PRODUKSI        : {', '.join([jenis.upper() for jenis in produksi])}")
      print(f"CASTS           : {', '.join([jenis.upper() for jenis in casts])}")
      print(f"SINOPSIS        : {film['sinopsis']}")
    
    else:
      print("JUDUL FILM YANG ANDA MASUKKAN TIDAK DITEMUKAN")  