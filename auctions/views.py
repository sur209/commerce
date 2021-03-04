from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from .models import User, Bid, Comment, AuctionList, Watchlist
from django import forms

class NewAuctionForm(forms.Form):
    auctionName = forms.CharField(label = "Nueva subasta")
    auctionDescription = forms.CharField(label = "Descripción")
    initialBid = forms.IntegerField()
    auctionImg = forms.ImageField(required=False)
    category = forms.CharField(label="Categoria")




def index(request):
    # If user isn't authenticated will be redirected to login page.
    #if not request.user.is_authenticated:
    #    return HttpResponseRedirect(reverse("login"))

    x = AuctionList.objects.all()
    print(x)

    return render(request, "auctions/index.html", {
        "auctions": x
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "POST":
        form = NewAuctionForm(request.POST)
        print(form.errors)
        if form.is_valid():
            auctionName = form.cleaned_data["auctionName"]
            auctionDescription = form.cleaned_data["auctionDescription"]
            auctionImg = form.cleaned_data["auctionImg"]
            initialBid = form.cleaned_data["initialBid"]
            category = form.cleaned_data["category"]
            eq = AuctionList(auction=auctionName, description=auctionDescription, img=auctionImg, oferta=initialBid, categoria=category)
            eq.save()

            return HttpResponseRedirect(reverse("index"))

        else:
            return HttpResponseNotFound("Sory")




    else:
        form = NewAuctionForm()
        return render(request, "auctions/create.html", {
            "form": form
            })

def listingpage(request, listing):
    if request.method == "POST":
        print(lulukas)
        return HttpResponseNotFound("Watcheandola")

    else:
        publicacion = AuctionList.objects.get(auction__iexact=str(listing))
        seguimiento = Watchlist.objects.filter(user=request.user, auctionid=publicacion.id)
        print(f"Este es el seguimiento: {(seguimiento)}")
        return render(request, "auctions/listingpage.html", {
         "item":publicacion, "seguimiento":bool(seguimiento) })

@login_required
def watchlist(request, item_id):
    identifier = item_id
    x = AuctionList.objects.get(id=identifier)
    seguimiento = Watchlist.objects.filter(user=request.user, auctionid=item_id)

    if seguimiento:
        seguimiento.delete()
        return render(request, "auctions/listingpage.html", {
            "item":x, "seguimiento":bool(seguimiento)
            })

    else:
        print(f"This is identifier: {identifier}")
        t = Watchlist(user=request.user, auctionid=identifier)
        t.save()
        seguimiento = Watchlist.objects.filter(user=request.user, auctionid=item_id)
        return render(request, "auctions/listingpage.html", {
            "item":x, "seguimiento":bool(seguimiento)
            })