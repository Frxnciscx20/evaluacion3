from django.urls import path 
from .views import index, feriados, formContacto, formReg, fotos, productos, qsomos 

urlpatterns=[ 
    path ('', index, name="index"),
    path ('feriados/', feriados, name="feriados"),
    path ('formContacto/', formContacto, name="formContacto"),
    path ('formReg/', formReg, name="formReg"),
    path ('fotos/', fotos, name="fotos"),
    path ('productos/', productos, name="productos"),
    path ('qsomos/', qsomos, name="qsomos"),

]