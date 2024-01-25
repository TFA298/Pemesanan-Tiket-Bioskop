from model.Film import Film
from model.Tiket import Tiket
from .FilmPage import FilmPage
from collections import defaultdict

class AdminPage:
  def __init__(self):
    self.film = Film()
    self.tiket = Tiket()
    self.film_page = FilmPage()

  def home(self):
    while True:
      print('========= CINEMA 23 (ADMIN) =========')
      print('[1] LIHAT SEMUA FILM')
      print('[2] LIHAT FILM SEDANG TAYANG')
      print('[3] TAMBAH FILM')
      print('[4] UBAH FILM')
      print('[5] HAPUS FILM')
      print('[6] LAPORAN PENJUALAN TIKET HARIAN')
      print('[0] KELUAR')
      print('-------------------------------------')
      pilih = int(input('PILIH MENU: '))

      if pilih == 1:
        self.semuaFilm()
      elif pilih == 2:
        self.filmSedangTayang()
      elif pilih == 3:
        self.tambahFilm()
      elif pilih == 4:
        self.ubahFilm()
      elif pilih == 5:
        self.hapusFilm()
      elif pilih == 6:
        self.laporanHarian()
      elif pilih == 0:
        break
      else:
        print('MENU TIDAK DITEMUKAN!')

  def semuaFilm(self):
    while True:
      print('===== DAFTAR FILM =====')
      self.film_page.daftar_film = self.film.getAll()
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

  def filmSedangTayang(self):
    while True:
      print('===== DAFTAR FILM SEDANG TAYANG =====')
      self.film_page.daftar_film = self.film.getByDate()
      self.film_page.listFilm()
      print("[0] KELUAR")
      print('-------------------------------------')
      pilih = int(input("LIHAT DETAIL FILM: "))
      if pilih > 0 and pilih <= len(self.film_page.daftar_film):
        self.film_page.detailFilm(pilih-1)
      elif pilih == 0:
        break
      else:
        print('OPSI TIDAK DITEMUKAN!')

  def tambahFilm(self):
    print('===== TAMBAH FILM =====')
    film = {
      "tipe": "film"
    }
    film['judul'] = input("JUDUL FILM: ")
    jenis_film = input("JENIS FILM: ")
    film['jenis_film'] = [jenis.strip() for jenis in jenis_film.split(',')] if ',' in jenis_film else jenis_film.strip()
    film['durasi'] = int(input("DURASI FILM: "))
    film['rating_usia'] = input("RATING USIA FILM: ")
    produser = input("PRODUSER FILM: ")
    film['produser'] = [kata.strip() for kata in produser.split(',')] if ',' in produser else produser.strip()
    sutradara = input("SUTRADARA FILM: ")
    film['sutradara'] = [kata.strip() for kata in sutradara.split(',')] if ',' in sutradara else sutradara.strip()
    penulis = input("PENULIS FILM: ")
    film['penulis'] = [kata.strip() for kata in penulis.split(',')] if ',' in penulis else penulis.strip()
    produksi = input("PRODUKSI FILM: ")
    film['produksi'] = [kata.strip() for kata in produksi.split(',')] if ',' in produksi else produksi.strip()
    casts = input("CASTS FILM: ")
    film['casts'] = [kata.strip() for kata in casts.split(',')] if ',' in casts else casts.strip()
    film['sinopsis'] = input("SINOPSIS FILM: ")
    film['tanggal_mulai'] = input("TANGGAL MULAI FILM: ")
    film['tanggal_selesai'] = input("TANGGAL SELESAI FILM: ")
    film['harga'] = input("HARGA FILM: ")
    jadwal = {}

    while True:
      waktu_dic = {}
      waktu = input("JADWAL FILM: ")
      studio = input("STUDIO FILM: ")
      waktu_dic['studio'] = studio
      waktu_dic['kursi'] = []
      jadwal[waktu] = waktu_dic
      lagi = input("INPUT JADWAL LAGI? [Y/T]: ")
      if lagi != 'Y' and lagi != 'y':
        break
    
    film['jadwal'] = jadwal
    self.film.create(film)
    print("FILM BERHASIL DITAMBAH!")

  def ubahFilm(self):
    while True:
      print('===== UBAH FILM =====')
      self.film_page.daftar_film = self.film.getAll()
      self.film_page.listFilm()
      print("[0] KELUAR")
      print('-----------------------')
      pilih = int(input("PILIH FILM: "))
      if pilih > 0 and pilih <= len(self.film_page.daftar_film):
        self.prosesUbah(pilih-1)
      elif pilih == 0:
        break
      else:
        print('OPSI TIDAK DITEMUKAN!')

  def prosesUbah(self, index):
    print("KOSONGKAN JIKA TIDAK ADA PERUBAHAN")
    film = self.film_page.daftar_film[index]

    judul = input("JUDUL FILM: ")
    film['judul'] = judul if judul else film['judul']

    jenis_film = input("JENIS FILM: ")
    jenis_film_list = [jenis.strip() for jenis in jenis_film.split(',')] if ',' in jenis_film else jenis_film.strip()
    film['jenis_film'] = jenis_film_list if jenis_film else film['jenis_film']

    durasi = int(input("DURASI FILM: "))
    film['durasi'] = durasi if durasi else film['durasi']

    rating_usia = input("RATING USIA FILM: ")
    film['rating_usia'] = rating_usia if rating_usia else film['rating_usia']

    produser = input("PRODUSER FILM: ")
    produser_list = [kata.strip() for kata in produser.split(',')] if ',' in produser else produser.strip()
    film['produser'] = produser_list if produser else film['produser']
    
    sutradara = input("SUTRADARA FILM: ")
    sutradara_list = [kata.strip() for kata in sutradara.split(',')] if ',' in sutradara else sutradara.strip()
    film['sutradara'] = sutradara_list if sutradara else film['sutradara']
    
    penulis = input("PENULIS FILM: ")
    penulis_list = [kata.strip() for kata in penulis.split(',')] if ',' in penulis else penulis.strip()
    film['penulis'] = penulis_list if penulis else film['penulis']
    
    produksi = input("PRODUKSI FILM: ")
    produksi_list = [kata.strip() for kata in produksi.split(',')] if ',' in produksi else produksi.strip()
    film['produksi'] = produksi_list if produksi else film['produksi']
    
    casts = input("CASTS FILM: ")
    casts_list = [kata.strip() for kata in casts.split(',')] if ',' in casts else casts.strip()
    film['casts'] = casts_list if casts else film['casts']
    
    sinopsis = input("SINOPSIS FILM: ")
    film['sinopsis'] = sinopsis if sinopsis else film['sinopsis']
    
    tanggal_mulai = input("TANGGAL MULAI FILM: ")
    film['tanggal_mulai'] = tanggal_mulai if tanggal_mulai else film['tanggal_mulai']
    
    tanggal_selesai = input("TANGGAL SELESAI FILM: ")
    film['tanggal_selesai'] = tanggal_selesai if tanggal_selesai else film['tanggal_selesai']
    
    harga = input("HARGA FILM: ")
    film['harga'] = harga if harga else film['harga']

    jadwal = film['jadwal'] if 'jadwal' in film else {}
    while True:
      waktu_dic = {}
      waktu = input("JADWAL FILM: ")
      studio = input("STUDIO FILM: ")
      waktu_dic['studio'] = studio
      waktu_dic['kursi'] = jadwal['kursi'] if 'kursi' in jadwal else []
      jadwal[waktu] = waktu_dic
      lagi = input("INPUT JADWAL LAGI? [Y/T]: ")
      if lagi != 'Y' and lagi != 'y':
        break
    
    film['jadwal'] = jadwal
    self.film.update(film)
    print("FILM BERHASIL DIUBAH!")

  def hapusFilm(self):
    while True:
      print('===== UBAH FILM =====')
      self.film_page.daftar_film = self.film.getAll()
      self.film_page.listFilm()
      print("[0] KELUAR")
      print('-----------------------')
      pilih = int(input("PILIH FILM: "))
      if pilih > 0 and pilih <= len(self.film_page.daftar_film):
        self.film.delete(self.film_page.daftar_film[pilih-1])
        print("FILM BERHASIL DIHAPUS!")
      elif pilih == 0:
        break
      else:
        print('OPSI TIDAK DITEMUKAN!')
  
  def laporanHarian(self):
    print('===== LAPORAN HARIAN =====')
    tiket = self.tiket.getByMonth()
    data_penjualan = defaultdict(list)
    
    for penjualan in tiket:
      tanggal = penjualan['tanggal'][:10]
      data_penjualan[tanggal].append(penjualan['harga'])

    for tanggal, harga_list in data_penjualan.items():
      jumlah_penjualan = len(harga_list)
      total_harga = sum(harga_list)
      print(f"{tanggal} | jumlah penjualan: {jumlah_penjualan} | total: {total_harga}")