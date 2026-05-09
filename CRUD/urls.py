from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('alunos/', include('alunos.urls')),
    path('disciplinas/', include('disciplinas.urls')),
    path('notas/', include('notas.urls')),
]