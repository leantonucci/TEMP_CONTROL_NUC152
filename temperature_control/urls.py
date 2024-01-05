from django.urls import path
from . import views
#URLConf
urlpatterns = [
    path('',views.Temp_control_screen),
    path('PUCHEROS_PLUS/',views.set_PID_HAT),
    path('FIDEOS/',views.set_PID_STANFORD)
    ]