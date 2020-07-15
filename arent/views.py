from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from mitra.models import AkunMitra, Iklan
from mitra.forms import IklanForm, PilihProvinsiForm
from django.db.models import Q


class Home(ListView):
    template_name = 'home.html'
    model = Iklan
    context_object_name = 'iklan_list'
    paginate_by = 25
    #ordering = ['-id']

    def get_queryset(self):
        cari = self.request.GET.get('cari')
        cari_provinsi = self.request.GET.get('provinsi')
        cari_jenis_kendaraan = self.request.GET.get('jenis_kendaraan')
        object_list = self.model.objects.all().order_by(
            '-golden_iklan', '-id')  # ini cara order by nya
        if cari != None:
            object_list = Iklan.objects.filter(Q(judul__icontains=cari) | Q(
                deskripsi_lain__icontains=cari) | Q(merk__icontains=cari) | Q(tipe_kendaraan__icontains=cari))
        elif cari_provinsi != 'default' and cari_provinsi != None:
            object_list = Iklan.objects.filter(
                mitra__akunmitra__provinsi=cari_provinsi)
        elif cari_jenis_kendaraan != None and cari_provinsi == 'default':
            object_list = Iklan.objects.filter(
                jenis_kendaraan=cari_jenis_kendaraan)
        else:
            object_list = self.model.objects.all().order_by('-golden_iklan', '-id')
        #! perbaiki filternya, masih belum seperti yang diharapkan
        #! cari_provinsi bermasalah
        # elif cari != None and cari_provinsi != None and cari_jenis_kendaraan != None:
        #     object_list = Iklan.objects.filter(Q(judul__icontains=cari) | Q(
        #         deskripsi_lain__icontains=cari) | Q(merk__icontains=cari) | Q(tipe_kendaraan__icontains=cari))
        #     object_list = object_list.filter(
        #         mitra__akunmitra__provinsi=cari_provinsi)
        #     object_list = object_list.filter(
        #         jenis_kendaraan=cari_jenis_kendaraan)
        return object_list

    def get_context_data(self, *args, **kwargs):
        provinsi_list = PilihProvinsiForm()
        self.kwargs.update({
            'page_title': 'Home',
            'provinsi_list': provinsi_list,
            'cari': self.request.GET.get('cari'),
            'cari_provinsi': self.request.GET.get('provinsi'),
            'cari_jenis_kendaraan': self.request.GET.get('jenis_kendaraan'),
        })
        kwargs = self.kwargs
        context = super().get_context_data(**kwargs)
        return context

    def get_allow_empty(self):
        return True


def redirectKeHome(request):
    return redirect('home', 1)
