"""
Service layer for physiotherapist related operations
"""

from rest_framework.exceptions import ValidationError
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

from martin_helder.models.physiotherapist import Physiotherapist, PhysiotherapistSerializer
from martin_helder.models.patientphysiotherapist import PatientPhysiotherapist
from martin_helder.services.query_service import QueryService
from martin_helder.services.pagination_service import PaginationService
from martin_helder.models.serializers.patient import PatientListSerializer
from martin_helder.models.patient import Patient
from martin_helder.views.view_utils import Utils

class PhysiotherapistService:
    """
   Service class for physiotherapist related operations
   """

    @staticmethod
    def is_valid_physiotherapist(id_physiotherapist):
        """
        Checks if the specified physiotherapist exists

        :param id_physiotherapist: ID of physiotherapist to be checked
        """

        Utils.validate_uuid(id_physiotherapist)

        if not Physiotherapist.objects.filter(id=id_physiotherapist).exists():
            raise ValidationError("The physiotherapist is not valid!")

    @staticmethod
    def is_physiotherapist_attributed_patient(id_patient, id_physio):
        """
        Checks if the logged in physiotherapist is attributed to a specified patient

        :param id_patient: ID of the patient to be checked
        """

        if not PatientPhysiotherapist.objects.filter(patient=id_patient,
                                                     physiotherapist=id_physio).exists():
            raise ValidationError("The logged physiotherapist can't treat this patient!")

    @staticmethod
    def list_physios_patients(physio_id, page_num, page_size, path, query=""):
        """
        Method to list patients of a physiotherapist

        :param page_num: Specified page number
        :param page_size: Specified number of elements per page
        :param path: Current endpoint url
        :param query: Search query
        :return: listof patients of a specific physiotherapist
        """

        list_patients = Patient.objects.filter(
            patientphysiotherapist__physiotherapist=physio_id
        ).order_by('person__first_name')

        patient_list = QueryService.get_query_results(list_patients,
                                                      query,
                                                      {"person__first_name": 'A',
                                                       "person__last_name": 'A',
                                                       "person__telephone_number": 'B',
                                                       "person__email": 'B',
                                                       "profession": 'B',
                                                       "diagnostic": 'C',
                                                       "clinical_history": 'C',
                                                       "doctor__name": 'B'})

        paginator = Paginator(patient_list, page_size)

        PaginationService.is_valid_page_number(paginator, int(page_num))
        results = PatientListSerializer(paginator.page(page_num), many=True).data

        return PaginationService.get_paginated_results(paginator, page_num, path, results)

    @staticmethod
    def get_physiotherapist(id_physiotherapist):
        """
        Returns the physiotherapist with a given id

        :param id_physiotherapist: ID of physiotherapist
        :return: Physiotherapist found or none
        """

        Utils.validate_uuid(id_physiotherapist)

        try:
            physiotherapist = Physiotherapist.objects.get(id=id_physiotherapist)
            return PhysiotherapistSerializer(physiotherapist).data
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_physiotherapist_by_credential(credential_id):
        """
        Returns the physiotherapist with a given credential id

        :param credential_id: ID of credential
        :return: Physiotherapist found or none
        """

        try:
            physiotherapist = Physiotherapist.objects.get(credential_id=credential_id)
            return PhysiotherapistSerializer(physiotherapist).data
        except ObjectDoesNotExist:
            return None
