"""
Serializer layer for treatment related operations
"""

from rest_framework import serializers

from martin_helder.models.treatmentcycle import TreatmentCycle
from martin_helder.models.treatment import Treatment
from martin_helder.models.person import Person
from martin_helder.models.patient import Patient
from martin_helder.models.perimetry import Perimetry
from martin_helder.models.goniometry import Goniometry
from martin_helder.models.muscletest import MuscleTest

from martin_helder.models.serializers.perimetry import PerimetrySerializer
from martin_helder.models.serializers.goniometry import GoniometrySerializer
from martin_helder.models.serializers.muscletest import MuscleTestSerializer

class TreatmentSerializer(serializers.ModelSerializer):
    """
    Class the serializes the model
    """

    class Meta:
        model = Treatment
        fields = '__all__'

class TreatmentListSerializer(serializers.ModelSerializer):
    """
    Class the serializes the model in a list
    """

    class Meta:
        model = Treatment
        exclude = ('pain_level', 'medication', 'treatment', 'periodic_evaluation', 'treatment_cycle')


class TreatmentPhysioListSerializer(serializers.ModelSerializer):
    """
    Class the serializes the model in a list
    """

    patient_name = serializers.SerializerMethodField()
    perimetries = serializers.SerializerMethodField()
    goniometries = serializers.SerializerMethodField()
    muscle_tests = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    @staticmethod
    def get_patient_name(obj):
        """
        Gets patient name

        :param obj: Current related object (Treatment)
        :return: Name
        """

        treatment_cycle = TreatmentCycle.objects.get(id=obj.treatment_cycle.id)
        patient = Patient.objects.get(id=treatment_cycle.patient.id)
        person = Person.objects.get(id=patient.person.id)

        return person.first_name + ' ' + person.last_name

    @staticmethod
    def get_perimetries(obj):
        """
        Gets perimetries of a treatment

        :param obj: Current related object (Treatment)
        :return: List of perimetries
        """

        return [PerimetrySerializer(perimetry).data
                    for perimetry in Perimetry.objects.filter(treatment=obj.id)]

    @staticmethod
    def get_goniometries(obj):
        """
        Gets goniometries of a treatment

        :param obj: Current related object (Treatment)
        :return: List of goniometries
        """

        return [GoniometrySerializer(goniometry).data
                    for goniometry in Goniometry.objects.filter(treatment=obj.id)]

    @staticmethod
    def get_muscle_tests(obj):
        """
        Gets muscle_tests of a treatment

        :param obj: Current related object (Treatment)
        :return: List of muscle_tests
        """

        return [MuscleTestSerializer(muscle_test).data
                    for muscle_test in MuscleTest.objects.filter(treatment=obj.id)]

    @staticmethod
    def get_url(obj):
        """
        Gets url of a treatments report

        :param obj: Current related object (Treatment)
        :return: Url string
        """

        treatment_cycle = TreatmentCycle.objects.get(id=obj.treatment_cycle.id)
        patient_id = treatment_cycle.patient.id
        treatment_cycle_id = obj.treatment_cycle.id
        treatment_id = obj.id
        ret = ''
        ret += 'patients/'
        ret += str(patient_id)
        ret += '/treatment-cycles/'
        ret += str(treatment_cycle_id)
        ret += '/treatments/'
        ret += str(treatment_id)
        ret += '/report/'

        return ret

    class Meta:
        model = Treatment
        fields = '__all__'
