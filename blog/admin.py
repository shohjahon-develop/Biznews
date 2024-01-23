from django.contrib import admin
from .models import News,Gun,Tank,Dodge,Awm,Train,Products,Bmw,Game,Add,Snew,Contact,Newslet,Comment,Mahsulot,Bot,Lorem

# Register your models here.
admin.site.register(Contact)
admin.site.register(Newslet)
admin.site.register(Comment)
@admin.register(Lorem)
class LoremAdmin(admin.ModelAdmin):
    list_display = ['name','date',"status"]
    list_filter = ['name',"date","status"]
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ['name','date',"status"]
    list_filter = ['name',"date","status"]
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ['name','status','price']
    list_filter = ['status','name','price']
    prepopulated_fields = {"slug":('name',)}

@admin.register(Snew)
class SnewAdmin(admin.ModelAdmin):
    list_display = ['title','status','slug']
    list_filter = ['status','created_time']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name','sana']
    list_filter = ['sana']

@admin.register(Gun)
class GunAdmin(admin.ModelAdmin):
    list_display = ['name','bio']
    list_filter = ['name','bio']


@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    list_display = ['name','bio','sana']
    list_filter = ['name','bio']



@admin.register(Dodge)
class DodgeAdmin(admin.ModelAdmin):
    list_display = ['name','bio']
    list_filter = ['name','bio']



@admin.register(Awm)
class AwmAdmin(admin.ModelAdmin):
    list_display = ['name','bio']
    list_filter = ['name','bio']

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ['name','bio']
    list_filter = ['name','bio']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name','bio']
    list_filter = ['name', 'bio']



@admin.register(Bmw)
class BmwAdmin(admin.ModelAdmin):
    list_display = ['name','bio']
    list_filter = ['name','bio']

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name','bio']
    list_filter = ['bio','name']


@admin.register(Add)
class AddAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']












































