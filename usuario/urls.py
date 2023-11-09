from django.urls import path,include
from rest_framework import routers
from usuario.views import SignUpUserAPI, SignUpAdminAPI, UserView,AdminView,SignInAPI, SignOutAPI

router_Prof = routers.DefaultRouter()
router_Prof.register(r'usuarioP', UserView, 'prof')

router_admin = routers.DefaultRouter()
router_admin.register(r'usuarioA', AdminView, 'admin')

urlpatterns = [

    path('signUpAdmin/', SignUpAdminAPI.as_view(), name='signUpAdmin'),
    path('SignUpUser/', SignUpUserAPI.as_view(), name='SignUpUser'),
    path('SignInAPI/', SignInAPI.as_view(), name='SignInAPI'),
     path('logout/', SignOutAPI.as_view(), name='logout'),
    path('ProfList/',include(router_Prof.urls)),
    path('AdminList/',include(router_admin.urls)),
    
]
  