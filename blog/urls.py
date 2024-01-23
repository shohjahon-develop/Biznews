from django.urls import path
from .views import (category,
                    contact,
                    mahsulots,
                    single,index,dodgedetailview,gundetailview,awmdetailview,newdetailview,productsdetailview,tankdetailview,botsdetailview,mahsulotsdetailview,loremsdetailview)

urlpatterns = [
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('single/', single, name='single'),
    path('', index, name='index'),
    path('dodge/<int:id>', dodgedetailview, name='dodgeDetail'),
    path('gun/<int:id>', gundetailview, name='gunDetail'),
    path('awm/<int:id>', awmdetailview, name='awmDetail'),
    path('new/<int:id>', newdetailview, name='newDetail'),
    path('products/<int:id>', productsdetailview, name='productsDetail'),
    path('tank/<int:id>', tankdetailview, name='tankDetail'),
    path('<slug:bots>', botsdetailview, name='botsDetail'),
    path("mahsulots/",mahsulots,name='mahsulots'),
    path('mahsulots/<slug:mahsulots>', mahsulotsdetailview, name='mahsulotsDetail'),
    path('lorems/<slug:lorems>', loremsdetailview, name='loremsDetail')
]