from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='lista_alunos', permanent=False), name='home'),
    path('admin/', admin.site.urls),

    path('alunos/', include('alunos.urls')),
    path('disciplinas/', include('disciplinas.urls')),
    path('notas/', include('notas.urls')),
]
