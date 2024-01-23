from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404
from .models import News,Gun,Tank,Dodge,Awm,Train,Products,Bmw,Add,Game,Bot,Mahsulot,Lorem
from .forms import ContactForms,NewsletForms,CommentForms


def category(request):
    ned = NewsletForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse("<h2>So'rovingiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/> ")
    games = Game.objects.all()
    lorems = Lorem.objects.all()
    context = {
        "games": games,
        "ned":ned,
        "lorems":lorems
    }
    return render(request,"category.html",context=context)

def contact(request):
    ned = NewsletForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse("<h2>So'rovingiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/> ")

    form = ContactForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>So'rovingiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/> ")
    context = {
        "form": form,
        "ned":ned
    }
    return render(request,"contact.html",context=context)


def single(request):
    come = CommentForms(request.POST or None)
    if request.method == "POST" and come.is_valid():
        come.save()
        return HttpResponse("<h2>So'rovingiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/> ")

    ned = NewsletForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse("<h2>So'rovingiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/> ")
    products = Products.objects.all()
    bmws = Bmw.objects.all()
    adds = Add.objects.all()
    context = {
        "products": products,
        "bmws":bmws,
        "adds":adds,
        "ned": ned,
        "come":come
    }
    return render(request,"single.html",context=context)

def index(request):
    ned = NewsletForms(request.POST or None)
    if request.method == "POST" and ned.is_valid():
        ned.save()
        return HttpResponse("<h2>So'rovingiz muvofiqiyatli amalga oshirildi raxmat !!! <h2/> ")
    new = News.objects.all()
    gun = Gun.objects.all()
    tank = Tank.objects.all()
    dodge = Dodge.objects.all()
    awm = Awm.objects.all()
    train = Train.objects.all()
    bots = Bot.objects.all()
    context = {
        "new":new,
        "gun":gun,
        "dodge":dodge,
        "tank":tank,
        "awm":awm,
        "train":train,
        "ned": ned,
        "bots":bots
    }
    return render(request,"index.html",context=context)


def dodgedetailview(request,id):
    try:
        dodge=Dodge.objects.get(id=id)
        context = {
            "dodge":dodge
        }
    except dodge.DoesNotExist:
        raise Http404("No dodge found")
    return render(request,"dodge_detail.html",context=context)


def gundetailview(request,id):
    try:
        gun=Gun.objects.get(id=id)
        context = {
            "gun":gun
        }
    except gun.DoesNotExist:
        raise Http404("No gun found")
    return render(request,"gun_detail.html",context=context)

def awmdetailview(request,id):
    try:
        awm=Awm.objects.get(id=id)
        context = {
            "awm":awm
        }
    except awm.DoesNotExist:
        raise Http404("No awm found")
    return render(request,"awm_detail.html",context=context)

def newdetailview(request,id):
    try:
        new=News.objects.get(id=id)
        context = {
            "new":new
        }
    except new.DoesNotExist:
        raise Http404("No new found")
    return render(request,"new_detail.html",context=context)

def productsdetailview(request,id):
    try:
        products=Products.objects.get(id=id)
        context = {
            "products":products
        }
    except products.DoesNotExist:
        raise Http404("No products found")
    return render(request,"products_detail.html",context=context)



def tankdetailview(request,id):
    try:
        tank=Tank.objects.get(id=id)
        context = {
            "tank":tank
        }
    except tank.DoesNotExist:
        raise Http404("No tank found")
    return render(request,"tank_detail.html",context=context)


def botsdetailview(request,bots):
    bots = get_object_or_404(Bot, slug=bots)
    context = {
        "bots": bots
    }
    return render(request,"bots_detail.html",context=context)



def mahsulots(request):
    mahsulots=Mahsulot.objects.all()
    context = {
        "mahsulots":mahsulots
    }
    return render(request,"mahsulots.html",context=context)


def mahsulotsdetailview(request,mahsulots):
    mahsulots = get_object_or_404(Mahsulot, slug=mahsulots)
    context = {
        "mahsulots":mahsulots
    }
    return render(request,"mahsulots_detail.html",context=context)


def loremsdetailview(request,lorems):
    lorems = get_object_or_404(Lorem, slug=lorems)
    context = {
        "lorems":lorems
    }
    return render(request,"lorems_detail.html",context=context)





































