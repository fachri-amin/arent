from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User 
from django.urls import reverse
# Create your models here.

class AkunMitra(models.Model):
    pilihanprovinsi = (
        ('Aceh','Aceh'),
        ('Bali','Bali'),
        ('Banten','Banten'),
        ('Bengkulu','Bengkulu'),
        ('Gorontalo','Gorontalo'),
        ('D.I Yogyakarta','D.I Yogyakarta'),
        ('D.K.I Jakarta','D.K.I Jakarta'),
        ('Jambi','Jambi'),
        ('Jawa Barat','Jawa Barat'),
        ('Jawa Tengah','Jawa Tengah'),
        ('Jawa Timur','Jawa Timur'),
        ('Kalimantan Barat','Kalimantan Barat'),
        ('Kalimantan Selatan','Kalimantan Selatan'),
        ('Kalimantan Tengah','Kalimantan Tengah'),
        ('Kalimantan Timur','Kalimantan Timur'),
        ('Kalimantan Utara','Kalimantan Utara'),
        ('Kep. Bangka Belitung','Kep. Bangka Belitung'),
        ('Kep. Riau','Kep. Riau'),
        ('Lampung','Lampung'),
        ('Maluku','Maluku'),
        ('Maluku Utara','Maluku Utara'),
        ('Nusa Tenggara Barat','Nusa Tenggara Barat'),
        ('Nusa Tenggara Timur','Nusa Tenggara Timur'),
        ('Papua','Papua'),
        ('Papua Barat','Papua Barat'),
        ('Riau','Riau'),
        ('Sulawesi Barat','Sulawesi Barat'),
        ('Sulawesi Selatan','Sulawesi Selatan'),
        ('Sulawesi Tengah','Sulawesi Tengah'),
        ('Sulawesi Tenggara','Sulawesi Tenggara'),
        ('Sulawesi Utara','Sulawesi Utara'),
        ('Sumatera Barat','Sumatera Barat'),
        ('Sumatera Selatan','Sumatera Selatan'),
        ('Sumatera Utara','Sumatera Utara'),
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    provinsi = models.CharField(
        max_length=50,
        choices=pilihanprovinsi,
    )
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='mitra/poto_profil/%Y/%m/%d/')

    def __str__(self):
        return '{}. {}'.format(self.id, self.user.username)

    def get_absolute_url(self):
        
        return reverse('redirectKeHome') #kwargs={'pk': self.pk})

class Iklan(models.Model):
    pilihanJenisKendaraan = (
        ('sepeda_motor', 'Sepeda Motor'),
        ('mobil', 'Mobil')
    )
    mitra = models.ForeignKey(User, on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='mitra/iklan/%Y/%m/%d/')
    judul = models.CharField(max_length=150)
    published = models.DateField(auto_now_add=True)
    jenis_kendaraan = models.CharField(max_length=20, choices=pilihanJenisKendaraan)
    merk = models.CharField(max_length=30)
    tipe_kendaraan = models.CharField(max_length=30)
    harga_sewa = models.CharField(max_length=50)
    deskripsi_lain = models.TextField()
    slug = models.SlugField(blank=True, editable=False)
    golden_iklan = models.BooleanField(default=False)

    def simpanHarga(self, hargaInput):
        listHarga = []
        for i in range(0,len(hargaInput),(1)):
            listHarga.append(hargaInput[i])

        for i in range(len(listHarga),0,-3):
            listHarga.insert(i,'.')
        del listHarga[(len(listHarga)-1)]
        hargaOutput = ''.join(listHarga)
        return hargaOutput

    
    def save(self):
        self.harga_sewa = self.simpanHarga(self.harga_sewa)
        self.slug = slugify((self.mitra.akunmitra.nama, self.judul))
        super().save()

    def get_absolute_url(self):
        
        return reverse('redirectKeHome') #kwargs={'pk': self.pk})
    # def get_absolute_url(self):
    #     return reverse('artikel:artikeldetail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}. {} | {}'.format(self.id, self.mitra.akunmitra.nama, self.judul)

    # class Meta:
    #     ordering = ['-golden_iklan','-id']