"""martin_helder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path

from martin_helder.views.treatment_view import TreatmentView
from martin_helder.views.treatment_physio_view import TreatmentPhysioView
from martin_helder.views.hello_world  import HelloWorld
from martin_helder.views.patient_view import PatientView
from martin_helder.views.patient_info_view import PatientInfoView
from martin_helder.views.administrator_view import AdministratorView
from martin_helder.views.doctor_view import DoctorView
from martin_helder.views.treatment_info_view import TreatmentInfoView
from martin_helder.views.treatment_report_view import TreatmentReportView
from martin_helder.views.goniometry_info_view import GoniometryInfoView
from martin_helder.views.muscle_test_info_view import MuscleTestInfoView
from martin_helder.views.perimetry_info_view import PerimetryInfoView
from martin_helder.views.body_zone_view import BodyZoneView
from martin_helder.views.associate_physiotherapist_view import AssocPhysioWithPatientView
from martin_helder.views.auth_login_view import AuthLoginView
from martin_helder.views.auth_refresh_view import AuthRefreshView
from martin_helder.views.auth_reset_view import AuthResetView
from martin_helder.views.auth_recover_view import AuthRecoverView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Martin Helder REST API",
      default_version='v0.1',
      description="REST API for managing Martin Helder treatment database",
   ),
   public=False,
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('martin-helder', HelloWorld.as_view()),
    path('treatments', TreatmentPhysioView.as_view()),
    path('patients', PatientView.as_view()),
    path('patients/<str:id_patient>', PatientInfoView.as_view()),
    path('patients/<str:id_patient>/associate-physiotherapist', AssocPhysioWithPatientView.as_view()),
    path('patients/<str:id_patient>/treatment-cycles/<str:id_treatment_cycle>/treatments', TreatmentView.as_view()),
    path('patients/<str:id_patient>/treatment-cycles/<str:id_treatment_cycle>/treatments/<str:id_treatment>', TreatmentInfoView.as_view()),
    path('patients/<str:id_patient>/treatment-cycles/<str:id_treatment_cycle>/treatments/<str:id_treatment>/report', TreatmentReportView.as_view()),
    path('patients/<str:id_patient>/treatment-cycles/<str:id_treatment_cycle>/treatments/<str:id_treatment>/goniometries/<str:id_goniometry>', GoniometryInfoView.as_view()),
    path('patients/<str:id_patient>/treatment-cycles/<str:id_treatment_cycle>/treatments/<str:id_treatment>/muscle-tests/<str:id_muscle_test>', MuscleTestInfoView.as_view()),
    path('patients/<str:id_patient>/treatment-cycles/<str:id_treatment_cycle>/treatments/<str:id_treatment>/perimetries/<str:id_perimetry>', PerimetryInfoView.as_view()),
    path('administrators', AdministratorView.as_view()),
    path('doctors', DoctorView.as_view()),
    path('body-zones', BodyZoneView.as_view()),
    path('auth/login', AuthLoginView.as_view()),
    path('auth/refresh', AuthRefreshView.as_view()),
    path('auth/password/reset', AuthResetView.as_view()),
    path('auth/password/recover', AuthRecoverView.as_view())
]
