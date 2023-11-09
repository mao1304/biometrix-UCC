from django.urls import path,include
from rest_framework import routers
from curso import views


router_clase = routers.DefaultRouter()
router_clase.register(r'clase', views.claseView, 'clase')

router_aula = routers.DefaultRouter()
router_aula.register(r'aula', views.aulaView, 'aula')

router = routers.DefaultRouter()
router = routers.DefaultRouter()

router.register(r'programa', views.programaView, 'programa')
router.register(r'curso', views.cursoView, 'curso')

urlpatterns = [
    path('clase/',include((router_clase.urls))),
    path('aula/',include(router_aula.urls)),
 
]
