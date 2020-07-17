from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from mitra.models import AkunMitra, Iklan
from mitra.forms import IklanForm, PilihProvinsiForm
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict


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
        # if cari != None:
        #     object_list = Iklan.objects.filter(Q(judul__icontains=cari) | Q(
        #         deskripsi_lain__icontains=cari) | Q(merk__icontains=cari) | Q(tipe_kendaraan__icontains=cari))
        # elif cari_provinsi != 'default' and cari_provinsi != None and cari_jenis_kendaraan == None:
        #     object_list = Iklan.objects.filter(
        #         mitra__akunmitra__provinsi=cari_provinsi)
        # elif cari_jenis_kendaraan != None and cari_provinsi == 'default':
        #     object_list = Iklan.objects.filter(
        #         jenis_kendaraan=cari_jenis_kendaraan)
        # elif cari_provinsi != 'default' and cari_provinsi != None and cari_jenis_kendaraan != None:
        #     object_list = Iklan.objects.filter(
        #         mitra__akunmitra__provinsi=cari_provinsi, jenis_kendaraan=cari_jenis_kendaraan)

        return object_list

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        if request.is_ajax():
            cari = request.GET.get('cari')
            cari_provinsi = request.GET.get('cari_provinsi')
            cari_jenis_kendaraan = request.GET.get('cari_jenis_kendaraan')

            data = {
                'cari': cari,
                'provinsi': cari_provinsi,
                'jenis_kendaraan': cari_jenis_kendaraan
            }

            json_data = serializers.serialize('python', self.object_list)
            return JsonResponse(json_data, safe=False, status=200)
        context = self.get_context_data()
        return self.render_to_response(context)

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
