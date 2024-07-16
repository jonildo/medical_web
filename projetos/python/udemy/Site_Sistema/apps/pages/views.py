from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    
    messages.debug(request, 'Esta é uma mensagem de sucesso!')
    messages.info(request, 'Esta é uma mensagem de sucesso!')
    messages.success(request, 'Esta é uma mensagem de sucesso!')
    messages.error(request, 'Esta é uma mensagem de sucesso!')
    messages.warning(request, 'Esta é uma mensagem de sucesso!')
    
    context = {
        'messagem': messages.success(request, 'Esta é uma mensagem de sucesso!')
    }
    return render(request, 'index.html')
