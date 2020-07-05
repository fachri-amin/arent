from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .models import AkunMitra, Iklan
from .forms import AkunMitraForm, UserMitra, IklanForm


def loginView(request):

    if request.method == 'POST':
        username_login = request.POST['username']
        password_login = request.POST['password']
        user = authenticate(request, username=username_login,
                            password=password_login)
        if user is not None:
            login(request, user)
            return redirect('redirectKeHome')
        else:
            return redirect('mitra:login')

    return render(request, 'mitra/login.html')


def registerView(request):
    registered = False
    user_mitra = UserMitra(request.POST or None)
    profile_mitra = AkunMitraForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if user_mitra.is_valid() and profile_mitra.is_valid():
            user = user_mitra.save()
            user.set_password(user.password)
            user.save()
            profile = profile_mitra.save(commit=False)
            profile.user = user
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
            profile.save()
            registered = True
            new_user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            login(request, new_user)
            return redirect('redirectKeHome')

    context = {
        'profileMitraForm': profile_mitra,
        'userMitraForm': user_mitra,
        'page_title': 'Registrasi Mitra',
        'registered': registered,
        # 'error1':user_mitra.errors,
        # 'error2':profile_mitra.errors,
    }

    return render(request, 'mitra/registrasi.html', context)


@login_required(login_url='mitra:login')
def logoutView(request):
    if request.method == 'POST':
        if request.POST['logout'] == 'ya':
            logout(request)
            return redirect('redirectKeHome')
        elif request.POST['logout'] == 'tidak':
            return redirect('redirectKeHome')

    context = {
        'page_title': 'Logout Confirmation'
    }

    return render(request, 'mitra/logout.html', context)


class UpdateUser(UpdateView, LoginRequiredMixin):
    # login_url = '/mitra/login/'
    model = AkunMitra
    template_name = 'mitra/updateUser.html'
    form_class = AkunMitraForm
    success_url = reverse_lazy('redirectKeHome')
    context_object_name = 'obj'
    extra_context = {
        'page_title': 'Edit Akun',
    }

    # def get_object(self, *args, **kwargs, queyset=None):
    #     obj =  super().get_object()
    #     if not obj.mitra == self.request.user:
    #         return redirect(obj)
    #     return obj

    # ini untuk ownership object/ jadi cuma yang create object ini yang bisa edit
    def dispatch(self, request, *args, **kwargs):
        obj = super().get_object()
        if not obj.user == self.request.user:
            return redirect(obj)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


@login_required(login_url='mitra:login')
def tambahIklan(request):
    iklan = IklanForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if iklan.is_valid():
            iklan_save = iklan.save(commit=False)
            iklan_save.mitra = request.user
            if 'gambar' in request.FILES:
                iklan_save.gambar = request.FILES['gambar']
            iklan_save.save()
            return redirect('redirectKeHome')
    context = {
        'page_title': 'Tambah Iklan',
        'iklanForm': iklan,
    }
    return render(request, 'mitra/tambahIklan.html', context)


class UpdateIklan(UpdateView, LoginRequiredMixin):
    model = Iklan
    template_name = 'mitra/updateUser.html'
    form_class = IklanForm
    success_url = reverse_lazy('mitra:iklanSaya')
    extra_context = {
        'page_title': 'Edit Iklan',
    }

    # ini untuk ownership object/ jadi cuma yang create object ini yang bisa edit
    def dispatch(self, request, *args, **kwargs):
        obj = super().get_object()
        if not obj.mitra == self.request.user:
            return redirect(obj)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     return context


class ManageIklan(ListView, LoginRequiredMixin):
    login_url = '/mitra/login/'
    template_name = 'mitra/iklanSaya.html'
    model = Iklan
    context_object_name = 'iklan_list'
    ordering_by = ['-id']
    paginate_by = 25

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update({
            'page_title': 'Iklan Saya'
        })
        kwargs = self.kwargs
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        self.queryset = self.model.objects.filter(mitra=self.request.user.id)
        return super().get_queryset()


class DeleteIklan(DeleteView, LoginRequiredMixin):
    model = Iklan
    template_name = 'mitra/iklanDeleteConfirm.html'
    success_url = reverse_lazy('mitra:iklanSaya')

    # ini untuk ownership object/ jadi cuma yang create object ini yang bisa edit
    def dispatch(self, request, *args, **kwargs):
        obj = super().get_object()
        if not obj.mitra == self.request.user:
            return redirect(obj)
        return super().dispatch(request, *args, **kwargs)


class DetailIklan(DetailView):
    template_name = 'mitra/iklanDetail.html'
    model = Iklan

# def cariIklan(request, cari):
#     pencarian = cari.replace('%20',' ')
#     tampil = Iklan.objects.filter(judul__contains=pencarian)
#     context = {
#         'iklan_list':tampil,
#         'page_title':'Home',
#     }

#     return render(request, 'home.html', context)
