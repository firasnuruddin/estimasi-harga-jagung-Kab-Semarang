from django.http.response import JsonResponse
from django.shortcuts import render
import joblib
import numpy as np


def index(request):
    return render(request, "index.html")


def form_page(request):
    return render(request, "form.html")


def predict(request):
    if request.POST.get('action') == 'POST':
        Luas_Panen = request.POST.get('Luas_Panen')
        Curah_Hujan = request.POST.get('Curah_Hujan')
        Jumlah_Panen = request.POST.get('Jumlah_Panen')
        Produktivitas = request.POST.get('Produktivitas')

        model_learning = joblib.load(
            r'D:\django-jagung-master\jagung\model\estimasijagung.pkl')

        sample_data = [
            Luas_Panen,
            Jumlah_Panen,
            Produktivitas,
            Curah_Hujan
        ]
        manipulate_array = np.array(sample_data).reshape(1, -1)
        result = model_learning.predict(manipulate_array)
        estimation = result[0]

        content = {
            'estimation': estimation,
        }

        return JsonResponse(content, safe=False)
