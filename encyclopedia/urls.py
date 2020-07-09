from django.urls import path


from . import views


urlpatterns = [
   
    path("", views.index, name="index"),
    path("wiki/<str:page>", views.entry_page, name="entry_page"),
    path("mysearch", views.mysearch, name="mysearch"),
    path("new", views.new, name="new"),
    path("saveentry",views.saveentry,name="saveentry"),
    path("randompage",views.randompage, name="randompage"),
    path("editpage/<str:title>",views.editpage,name="editpage"),
    path("resave",views.resave,name="resave")

]
