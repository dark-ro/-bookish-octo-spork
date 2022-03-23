from django.shortcuts import render
from store.forms import ClientForm
from store.models import client

# Create your views here.
def index(request):
    message = "  "
    message2 = " "
    if request.method =='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            commentaire = form.cleaned_data['commentaire']
            utilisateur = client.objects.filter(email=email, commentaire=commentaire)
            if not utilisateur.exists():
                utilisateur = client.objects.create(email=email, commentaire=commentaire)
                message = "Bienvenue cher nouveau client "
                message2= "et merci pour Votre confiance"
    else:
        form = ClientForm()
    context = {
        'message2': message2,
        'message': message,
        'form' : form
    }        
    return render(request, 'store/index.html', context)