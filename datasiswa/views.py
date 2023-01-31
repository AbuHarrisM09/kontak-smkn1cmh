from django.shortcuts import render, redirect, get_object_or_404
from .models import Datasiswa
from .forms import DatasiswaForm

# Create your views here.
def list_siswa(request):
    list = Datasiswa.objects.all()
    return render(request, 'siswa/list_siswa.html', {'list': list})

def create_siswa(request):
    if request.method == 'POST':
        form = DatasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/siswa')
    else:
        form = DatasiswaForm()
        return render(request,'siswa/create_siswa.html', {'form': form})

def edit_siswa(request, id):
    siswa = Datasiswa.objects.get(id=id)
    if request.method == 'POST':
        form = DatasiswaForm(request.POST, instance=siswa)
        if form.is_valid():
            form.save()
            return redirect('/siswa')
    else:
        form = DatasiswaForm(instance=siswa)
    return render(request, 'siswa/edit_siswa.html', {'form': form})

def delete_siswa(request, id):
    del_siswa = get_object_or_404(Datasiswa, id=id)
    del_siswa.delete()
    return redirect(request.META.get('HTTP_REFERER', '/siswa'))