# trading_info/views.py
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Bot de Trading Automatizado',
        'slogan': 'Objetivo estratégico a corto plazo',
        'description': 'Explora el mundo del trading y aprende con nosotros.',
        'plans': [
            {'name': 'Básico', 'price': '$15/mes', 'features': ['Acceso al bot', '1 par de divisas', 'Soporte básico']},
            {'name': 'Premium', 'price': '$25/mes', 'features': ['Acceso al bot', '3 pares de divisas', 'Soporte prioritario']},
        ],
        'features': ['Precisión >60%', 'Soporte Personalizado', 'Actualizaciones Regulares'],
    }
    return render(request, 'trading_info/home.html', context)

  
def aprender_trading(request):
    return render(request, 'trading_info/aprender.html', {
        'title': 'Aprende Trading',
        'content': 'Aquí encontrarás recursos para aprender trading.'
    })
