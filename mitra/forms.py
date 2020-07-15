from django import forms
from django.contrib.auth.models import User
from .models import AkunMitra, Iklan


class AkunMitraForm(forms.ModelForm):
    class Meta:
        model = AkunMitra
        fields = [
            'nama',
            'provinsi',
            'alamat',
            'no_hp',
            'photo',
        ]
        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nama lengkap Anda',
                },
            ),
            'provinsi': forms.Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            'no_hp': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            # 'photo':forms.ImageField(),
            'alamat': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class PilihProvinsiForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ membuat NOT Required field """
        super().__init__(*args, **kwargs)
        self.fields['provinsi'].required = False

    class Meta:
        model = AkunMitra
        fields = [
            'provinsi'
        ]
        widgets = {
            'provinsi': forms.Select(
                attrs={
                    'class': 'cari-provinsi form-control',
                },
            ),
        }


class UserMitra(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email Anda',
                },
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password Anda',
                },
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Username Anda',
                },
            ),
        }


class IklanForm(forms.ModelForm):
    class Meta:
        model = Iklan
        fields = [
            'judul',
            'jenis_kendaraan',
            'merk',
            'tipe_kendaraan',
            'harga_sewa',
            'deskripsi_lain',
            'gambar',
        ]
        widgets = {
            'judul': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Buat judul semenarik mungkin',
                },
            ),
            'harga_sewa': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'jenis_kendaraan': forms.Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            'merk': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            'tipe_kendaraan': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ex:supra, avanza dll',
                },
            ),
            'deskripsi_lain': forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),
            'gambar': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
