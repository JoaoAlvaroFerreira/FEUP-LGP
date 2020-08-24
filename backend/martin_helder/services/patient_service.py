"""
Service layer for patient related operations
"""

from django.core.paginator import Paginator
from rest_framework.exceptions import ValidationError

from martin_helder.models import Patient
from martin_helder.services.person_service import PersonService
from martin_helder.services.pagination_service import PaginationService
from martin_helder.services.query_service import QueryService
from martin_helder.models.serializers.patient import PatientSerializer, PatientListSerializer
from martin_helder.views.view_utils import Utils

class PatientService:
    """
    Service class for patient related operations
    """

    @staticmethod
    def is_valid_patient(id_patient):
        """
        Checks if the specified patient exists

        :param id_patient: ID of patient to be checked
        """

        Utils.validate_uuid(id_patient)

        if not Patient.objects.filter(id=id_patient).exists():
            raise ValidationError("The patient is not valid!")

    @staticmethod
    def add_patient(patient_request):
        '''
        Method to add a new patient

        :param patient_request: Incoming request
        :return: patient and person id from the new patient
        '''
        return_value = {}

        return_value['person_id'] = PersonService.add_person({'street': patient_request['address']['street'],
                                                              'zip_code': patient_request['address']['zip_code'],
                                                              'city': patient_request['address']['city']},
                                                             {'nif': patient_request['nif'],
                                                              'first_name': patient_request['first_name'],
                                                              'last_name': patient_request['last_name'],
                                                              'birth_date': patient_request['birth_date'],
                                                              'telephone_number': patient_request['telephone_number'],
                                                              'email': patient_request['email'],
                                                              'gender': patient_request['gender']}
                                                             )

        new_patient = Patient.objects.create(profession=patient_request['profession'],
                                             diagnostic=patient_request['diagnostic'],
                                             clinical_history=patient_request['clinical_history'],
                                             person_id=return_value['person_id']
                                             )

        new_patient.save()

        return_value['patient_id'] = new_patient.id

        return return_value

    @staticmethod
    def list_patients(page_num, page_size, path, query=""):
        """
        Method to list patients on the system

        :param page_num: Specified page number
        :param page_size: Specified number of elements per page
        :param path: Current endpoint url
        :param query: Search query
        :return: list of information of patients on the system
        """

        patients_list = QueryService.get_query_results(Patient.objects, query, {"person__first_name": 'A',
                                                                                "person__last_name": 'A',
                                                                                "person__telephone_number": 'B',
                                                                                "person__email": 'B',
                                                                                "profession": 'B',
                                                                                "diagnostic": 'C',
                                                                                "clinical_history": 'C',
                                                                                "doctor__name": 'B'})

        paginator = Paginator(patients_list, page_size)

        PaginationService.is_valid_page_number(paginator, int(page_num))
        results = PatientListSerializer(paginator.page(page_num), many=True).data

        return PaginationService.get_paginated_results(paginator, page_num, path, results)


    @staticmethod
    def patient_info(patient_id):
        """
        Method that acquires information about a specific patient

        :param patient_id: id of the patient in question
        :return: Serializer of patient
        """

        PatientService.is_valid_patient(patient_id)

        try:
            patient = Patient.objects.get(id=patient_id)
        except:
            raise ValidationError("The patient is not valid!")

        patient_data = PatientSerializer(patient).data

        return patient_data
