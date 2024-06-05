from django.shortcuts import render, redirect
from .forms import ClientInfoForm

from django.shortcuts import render, redirect
from .forms import ClientInfoForm

# def submit_client_info(request):
#     if request.method == 'POST':
#         form = ClientInfoForm(request.POST)
#         if form.is_valid():
#             # Récupérer les coordonnées géographiques à partir du formulaire
#             latitude = form.cleaned_data['latitude']
#             longitude = form.cleaned_data['longitude']
#             print('latitude', latitude)
#             print('longitude', longitude)
#             # Enregistrer les données dans la base de données
#             client_info = form.save(commit=False)
#             client_info.latitude = latitude
#             client_info.longitude = longitude
#             client_info.save()
#             return redirect('success')
#     else:
#         form = ClientInfoForm()
#     return render(request, 'pages\submit_client_digit.html', {'form': form})


def success(request):
    return render(request, 'pages\success.html')


def submit_client_info(request):
    if request.method == 'POST':
        form = ClientInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ClientInfoForm()
    return render(request, 'pages\submit_client_info.html', {'form': form})

