from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from django.urls import reverse
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.decorators import login_required

from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer,AdminSerializer
from .models import NewUser
from .forms import AdminUserForm, NewUserForm, LoginUserForm



from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
#retorna todos los registros de usuarios como json  

class ReadOnlyUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
    
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return NewUser.objects.filter(admin_check=False)  
    permission_classes = [ReadOnlyUserPermission]

class AdminView(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    def get_queryset(self):
        return NewUser.objects.filter(admin_check=True)  
    permission_classes = [ReadOnlyUserPermission]

@method_decorator(csrf_exempt, name='dispatch')
class SignUpAdminAPI(APIView):
    def post(self, request, format=None):
        print("Entrando a la vista SignUpAdminAPI")
        form = AdminUserForm(request.data)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                admin_check = form.cleaned_data.get('admin_check', False)

                user = NewUser.objects.create_user(
                    username=username,
                    password=password,
                    admin_check=admin_check,
                )

                authenticated_user = authenticate(request, username=username, password=password)
                login(request, authenticated_user)

                response = Response({'message': 'Registro exitoso'}, status=status.HTTP_201_CREATED)
                response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000"
                return response
            except IntegrityError as e:
                print(f"Error de integridad: {e}")
                return Response({'error': 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Formulario no válido")
            print("Datos del formulario:", request.data)
            return Response({'error': 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(csrf_exempt, name='dispatch')
class SignUpUserAPI(APIView):
    def post(self, request, format=None):
        print("Entrando a la vista SignUpUserAPI")
        if request.user.admin_check == False:
            return Response({'error': 'Acceso no autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
        form = NewUserForm(request.data)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                huella = form.cleaned_data['huella']
                admin_check = form.cleaned_data.get('admin_check', False)

                user = NewUser.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    huella=huella,
                    admin_check=admin_check,
                )

                user.save()

                response = Response({'message': 'Registro exitoso'}, status=status.HTTP_201_CREATED)
                response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000"
                return response
            except IntegrityError as e:
                print(f"Error de integridad: {e}")
                return Response({'error': 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("Formulario no válido")
            print("Datos del formulario:", request.data)
            return Response({'error': 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
        
@login_required  
def home_view(request):
    return render(request, 'home.html')

   
@method_decorator(csrf_exempt, name='dispatch')
class SignInAPI(APIView):
    def post(self, request, format=None):
        print("Entrando a la vista SignInAPI")
        form = LoginUserForm(request.data)
        
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                if request.session.get('login_attempts', 0) >= 5:
                    raise SuspiciousOperation("Número máximo de intentos de inicio de sesión alcanzado.")

                user = authenticate(request, username=username, password=password)

                if user is None:
                    raise SuspiciousOperation("Usuario o contraseña incorrectos.")

                request.session['login_attempts'] = 0
                login(request, user)

                return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)

            except SuspiciousOperation as e:
                request.session['login_attempts'] = request.session.get('login_attempts', 0) + 1
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
    
@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class SignOutAPI(APIView):
    def post(self, request, format=None):
        request.session.flush()
        logout(request)
        return Response({'message': 'Cierre de sesión exitoso'}, status=status.HTTP_200_OK)