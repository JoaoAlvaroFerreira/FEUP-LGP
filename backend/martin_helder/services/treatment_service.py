"""
Service layer for treatment related operations
"""

from django.core.paginator import Paginator
from rest_framework.exceptions import ValidationError

from martin_helder.services.physiotherapist_service import PhysiotherapistService
from martin_helder.models import TreatmentCycle
from martin_helder.services.patient_service import PatientService
from martin_helder.models.treatment import Treatment
from martin_helder.models.serializers.treatment import TreatmentSerializer
from martin_helder.models.goniometry import Goniometry
from martin_helder.models.perimetry import Perimetry
from martin_helder.models.muscletest import MuscleTest
from martin_helder.services.perimetry_service import PerimetryService
from martin_helder.services.muscle_test_service import MuscleTestService
from martin_helder.services.goniometry_service import GoniometryService
from martin_helder.services.pagination_service import PaginationService
from martin_helder.models.serializers.treatment import TreatmentListSerializer
from martin_helder.models.serializers.treatment import TreatmentPhysioListSerializer
from martin_helder.views.view_utils import Utils
from martin_helder.services.report_service import ReportService

class TreatmentService:
    """
    Service class for treatment related operations
    """

    @staticmethod
    def treat_patient(treatment_request, id_patient, id_treatment_cycle, id_physio):
        """
        Method to treat a patient, creating a new treatment

        :param treatment_request: Information for the requested new treatment
        :param id_patient: ID of the patient to be treated
        :param id_treatment_cycle: Treatment cycle where the new treatment belongs
        :return: Treatment created
        """

        return_value = {}

        PatientService.is_valid_patient(id_patient)
        PhysiotherapistService.is_physiotherapist_attributed_patient(id_patient, id_physio)
        TreatmentService.is_valid_treatment_cycle(id_treatment_cycle, id_patient)
        TreatmentService.has_treatment_cycle_remaining_sessions(id_treatment_cycle)

        new_treatment = Treatment.objects.create(treatment_cycle_id=id_treatment_cycle,
                                                 start_date=
                                                 treatment_request['start_date'],
                                                 end_date=
                                                 treatment_request[
                                                     'end_date'] if 'end_date' in treatment_request else None,
                                                 summary=
                                                 treatment_request[
                                                     'summary'] if 'summary' in treatment_request else None,
                                                 pain_level=
                                                 treatment_request[
                                                     'pain_level'] if 'pain_level' in treatment_request else None,
                                                 medication=
                                                 treatment_request[
                                                     'medication'] if 'medication' in treatment_request else None,
                                                 treatment=
                                                 treatment_request[
                                                     'treatment'] if 'treatment' in treatment_request else None,
                                                 periodic_evaluation=
                                                 treatment_request[
                                                     'periodic_evaluation'] if 'periodic_evaluation' in
                                                 treatment_request
                                                 else None)

        new_treatment.save()

        return_value['treatment_id'] = new_treatment.id

        if "perimetries" in treatment_request:
            return_value['perimetries_id'] = []
            for perimetry in treatment_request['perimetries']:
                return_value['perimetries_id'].append(PerimetryService.add_perimetry(perimetry, new_treatment.id))

        if "muscle_tests" in treatment_request:
            return_value['muscle_tests_id'] = []
            for muscle_test in treatment_request['muscle_tests']:
                return_value['muscle_tests_id'].append(MuscleTestService.add_muscle_test(muscle_test, new_treatment.id))

        if "goniometries" in treatment_request:
            return_value['treatment_requests_id'] = []
            for goniometry in treatment_request['goniometries']:
                return_value['treatment_requests_id'].append(GoniometryService.add_goniometry(goniometry,
                                                                                              new_treatment.id))

        return return_value

    @staticmethod
    def list_all_treatments(id_patient, id_treatment_cycle, page_num, page_size, path):
        """
          Method to list all treatments on treatment cycle

        :param id_patient: Specified Patient
        :param id_treatment_cycle: Specified treatment cycle
        :param page_num: Specified page number
        :param page_size: Specified number of elements per page
        :param path: Current endpoint url
        :return: list of information of patients on the system
        """

        PatientService.is_valid_patient(id_patient)
        TreatmentService.is_valid_treatment_cycle(id_treatment_cycle, id_patient)

        all_treatments = Treatment.objects.filter(treatment_cycle_id=id_treatment_cycle)
        paginator = Paginator(all_treatments, page_size)

        PaginationService.is_valid_page_number(paginator, int(page_num))
        results = TreatmentListSerializer(paginator.page(page_num), many=True).data

        return PaginationService.get_paginated_results(paginator, page_num, path, results)

    @staticmethod
    def list_all_physio_treatments(physio_id, page_num, page_size, path):
        """
          Method to list all treatments done by a physiotherapist ordered by date in descending order

        :param physio_id: Specified Physiotherapist
        :param page_num: Specified page number
        :param page_size: Specified number of elements per page
        :param path: Current endpoint url
        :return: list of physiotherapist treatments
        """

        all_treatment_cycles = TreatmentCycle.objects.filter(physiotherapist=physio_id)
        all_treatments = Treatment.objects.filter(
            treatment_cycle_id__in=all_treatment_cycles
        ).order_by('end_date').reverse()

        paginator = Paginator(all_treatments, page_size)

        PaginationService.is_valid_page_number(paginator, int(page_num))
        results = TreatmentPhysioListSerializer(paginator.page(page_num), many=True).data

        return PaginationService.get_paginated_results(paginator, page_num, path, results)

    @staticmethod
    def is_valid_treatment_cycle(id_treatment_cycle, id_patient):
        """
        Checks if the specified treatment cycle belongs to the patient

        :param id_treatment_cycle: ID of the treatment cycle
        :param id_patient: Patient where the cycle should belong to
        """

        Utils.validate_uuid(id_treatment_cycle)
        Utils.validate_uuid(id_patient)

        if not TreatmentCycle.objects.filter(id=id_treatment_cycle, patient_id=id_patient).exists():
            raise ValidationError("The treatment cycle is not valid!")

    @staticmethod
    def has_treatment_cycle_remaining_sessions(id_treatment_cycle):
        """
        Checks if the patient hasn't already reached the limit of sessions of the treatment cycle

        :param id_treatment_cycle: ID of the treatment cycle
        """
        try:
            treatment_cycle = TreatmentCycle.objects.get(id=id_treatment_cycle)
        except:
            raise ValidationError("The treatment cycle is not valid!")

        if treatment_cycle.number_of_sessions <= treatment_cycle.completed_sessions:
            raise ValidationError("All sessions of the treatment cycle " + str(treatment_cycle.id) + " were already "
                                                                                                     "performed!")

    @staticmethod
    def is_valid_treatment(treatment_id):
        """
        Checks if the specified treatment exists

        :param treatment_id: if of the treatment
        """

        Utils.validate_uuid(treatment_id)

        if not Treatment.objects.filter(id=treatment_id).exists():
            raise ValidationError("The treatment is not valid!")

    @staticmethod
    def treatment_info(treatment_id):
        """
        Method that acquires information about a specific treatment

        :param treatment_id: id of the treatment
        :return: Serializer of treatment
        """

        TreatmentService.is_valid_treatment(treatment_id)

        try:
            treatment = Treatment.objects.get(id=treatment_id)
        except:
            raise ValidationError("The treatment is not valid!")

        treatment_data = TreatmentSerializer(treatment).data

        return treatment_data

    @staticmethod
    def treatment_report(treatment_id):
        """
        Method that generates PDF report

        :param treatment_id: id of the treatment
        :return: PDF Report of treatment
        """

        TreatmentService.is_valid_treatment(treatment_id)

        try:
            treatment = Treatment.objects.get(id=treatment_id)
            treatment_cycle = treatment.treatment_cycle
            goniometries = Goniometry.objects.filter(treatment_id=treatment_id)
            perimetries = Perimetry.objects.filter(treatment_id=treatment_id)
            muscle_tests = MuscleTest.objects.filter(treatment_id=treatment_id)
        except:
            raise ValidationError("The treatment is not valid!")

        return ReportService.treatment_report(treatment, treatment_cycle, goniometries, perimetries, muscle_tests)
