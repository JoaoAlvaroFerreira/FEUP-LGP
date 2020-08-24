"""
Serializer layer for patient related operations
"""

import uuid
from django.db import models
from rest_framework import serializers

from martin_helder.models.treatmentcycle import TreatmentCycle
from martin_helder.models.treatment import Treatment
from martin_helder.models.patient import Patient
from martin_helder.models.doctor import DoctorSerializer
from martin_helder.models.person import PersonSerializer
from martin_helder.models.state import StateSerializer


class PatientSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model
    """
    person = PersonSerializer()
    doctor = DoctorSerializer()
    state = StateSerializer()

    class Meta:
        model = Patient
        fields = '__all__'

class PatientListSerializer(serializers.ModelSerializer):
    """
    Class that serializes the model in a list
    """

    name = serializers.SerializerMethodField(source='person')
    person = PersonSerializer()
    doctor = serializers.StringRelatedField(source="doctor.name")
    state = serializers.StringRelatedField(source="state.name")
    last_treatmentment_cycle = serializers.SerializerMethodField()
    number_completed_sessions = serializers.SerializerMethodField()

    @staticmethod
    def get_name(obj):
        """
        Assembles the full name from the first and last

        :param obj: Current related object (Person)
        :return: Full name
        """

        return '{} {}'.format(obj.person.first_name, obj.person.last_name)

    @staticmethod
    def get_last_treatmentment_cycle(obj):
        patient_id = obj.id

        treatments = Treatment.objects.filter(treatment_cycle__patient=patient_id).order_by('-start_date')

        if len(treatments) > 0:
            return treatments[0].treatment_cycle.id
        else:
            return 'No treatment cycles'

    @staticmethod
    def get_number_completed_sessions(obj):
        '''
        Gets the number of sessions and completed sessions
        :param obj: Current related object (Person)
        :return: Tuple with number of sessions and completed sessions
        '''
        patient_id = obj.id

        treatments = Treatment.objects.filter(treatment_cycle__patient=patient_id).order_by('-start_date')

        if len(treatments) > 0:
            treatment_cycle = TreatmentCycle.objects.get(id=treatments[0].treatment_cycle.id)

            number_of_sessions = treatment_cycle.number_of_sessions
            completed_sessions = treatment_cycle.completed_sessions

            return (number_of_sessions, completed_sessions)
        else:
            return (0,0)

    class Meta:
        model = Patient
        exclude = ('profession',)
