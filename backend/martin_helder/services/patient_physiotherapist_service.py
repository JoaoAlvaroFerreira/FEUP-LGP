"""
Service layer for patientphysiotherapist related operations
"""

from martin_helder.models.patientphysiotherapist import PatientPhysiotherapist
from martin_helder.services.patient_service import PatientService
from martin_helder.services.physiotherapist_service import PhysiotherapistService


class PatientPhysioService:
    """
    Service class for patientphysiotherapist related operations
    """

    @staticmethod
    def check_if_patient_has_physio(patient_id):
        """
        Method that checks if patient has a physio or not
        :param patient_id: The id of the given patient
        :return: boolean value containing the answer
        """
        if PatientPhysiotherapist.objects.filter(patient=patient_id).exists():
            return True
        return False

    @staticmethod
    def assoc_physio_with_patient(request, patient_id):
        """
        Method that associates a physio with a patient

        :param request: request of association
        :param patient_id: id of the patient
        :return: id of patient, physio and of association
        """

        physiotherapist_id = request['physiotherapist_id']

        return_value = {'patient_id': patient_id, 'physiotherapist_id': physiotherapist_id}

        PatientService.is_valid_patient(patient_id)
        PhysiotherapistService.is_valid_physiotherapist(physiotherapist_id)

        if not PatientPhysioService.check_if_patient_has_physio(patient_id):
            new_patient_physio = PatientPhysiotherapist.objects.create(patient_id=patient_id,
                                                                       physiotherapist_id=physiotherapist_id)
        else:
            new_patient_physio = PatientPhysiotherapist.objects.get(patient=patient_id)
            new_patient_physio.physiotherapist_id = physiotherapist_id

        new_patient_physio.save()

        return_value['id'] = new_patient_physio.id

        return return_value
