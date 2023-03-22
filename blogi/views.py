from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Postaus

# This is the search post view which returns to us-
# what search term user have input, posts that match-
# the given input, the same posts but in lowercase that match-
# the given input, and the total amount of posts that matched
def search_post(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Postaus.objects.filter(otsikko__contains=searched)
        posts_lower = Postaus.objects.filter(otsikko_lower__contains=searched)
        posts_total = (len(posts)+(len(posts_lower)))
        return render(
            request,
            "blogi/search_post.html",
            {'searched': searched, 'posts': posts, 'posts_lower': posts_lower, 'posts_total': posts_total}
        )
    else:
        return render(
            request,
            "blogi/search_post.html",
        )

# All the posts
def postaukset(request):
    postaukset = Postaus.objects.all()
    context = {"postaukset": postaukset}
    return render(
        request,
        "blogi/postauslista.html",
        context,
    )

# Full post
def nayta_postaus(request, id):
    postaus = Postaus.objects.get(id=id)
    context = {"postaus": postaus}
    return render(request, "blogi/postaus.html", context)


# def uusi_postaus(request):
#     if request.method == "GET":
#         # 1. Lomake näytetään ensimmäistä kertaa
#         return render(request, "blogi/uusi_postaus.html")

#     elif request.method == "POST":
#         # 2. Käyttäjä täytti ja lähetti lomakkeen

#         # Luetaan lomakkeen tiedot POST-datasta
#         otsikko = request.POST['otsikko']
#         teksti = request.POST['teksti']

#         # Luodaan uusi Postaus-objekti tietokantaan
#         postaus = Postaus.objects.create(
#             otsikko=otsikko,
#             teksti=teksti,
#         )

#         # Muodostetaan URL-osoite luotuun Postaus-objektiin
#         url = reverse('nayta_postaus', args=(postaus.id,))

#         # Palautetaan uudelleenohjaus uuden Postaus-objektin URL:iin
#         return redirect(url)