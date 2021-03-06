"""
CATATAN
=======
empty value pada model ini
 > Char = empty string
 > Boolean = false
 > Integer = None (Null)

semua IntergerField di sini memiliki sifat Null = True

JANGAN LUPA MENGGANTI BOOLEAN MENJADI BERTIPE NULLBOOLEANFIELD
"""

from __future__ import unicode_literals
from django.db import models
from core.models import *

class ABaseLine(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
    interviewer_id = models.CharField(max_length=25, blank=True)
    data_entry_id = models.CharField(max_length=25, blank=True)
    data_checked_id = models.CharField(max_length=25, blank=True, null=True)
    date_admission = models.CharField(max_length=15, blank=True)
    date_interviewed = models.CharField(max_length=15, blank=True)
    date_data_entered = models.CharField(max_length=15, blank=True)
    date_data_checked = models.CharField(max_length=15, blank=True)
    is_save_all = models.NullBooleanField(default=False, blank=True)
    def __str__(self):
        return "[participant_id : " + unicode(self.participant.participant_id)+ ", participant_name : "+unicode(self.participant.name )+ ", interviewer_id : "+unicode(self.interviewer_id )+ ", data_entry_id : "+unicode(self.data_entry_id )+ ", is_save_all : "+unicode(self.is_save_all )+ ", date_data_checked : "+ unicode(self.date_data_checked )+"]"

class A1MotherDemographic(models.Model):
    a_form = models.ForeignKey(ABaseLine, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=25, blank=True)
    updated_by = models.CharField(max_length=25, blank=True)
    created_time = models.CharField(max_length=28, blank=True)
    updated_time = models.CharField(max_length=28, blank=True)
    participant_id = models.CharField(max_length=10, blank=True)
    a1m_name = models.CharField(max_length=25, blank=True)
    a1m_pob = models.CharField(max_length=25, blank=True)
    a1m_dob = models.CharField(max_length=15, blank=True)
    a1m_residence_street = models.CharField(max_length=25, blank=True)
    a1m_residence_rt = models.CharField(max_length=3, blank=True)
    a1m_residence_rw = models.CharField(max_length=3, blank=True)
    a1m_residence_district = models.CharField(max_length=25, blank=True)
    a1m_residence_city = models.CharField(max_length=25, blank=True)
    a1m_residence_zipcode = models.CharField(max_length=10, blank=True)
    a1m_moving_date = models.CharField(max_length=15, blank=True)
    a1m_residing_duration = models.CharField(max_length=15, blank=True)
    RESIDENTIAL_STATUS_LIST = (
                        ('', ''),
                        ('1', 'Personal property'),
                        ('2', 'Rent'),
                        ('3', 'Family house'),  
        )
    a1m_residential_status = models.CharField(choices=RESIDENTIAL_STATUS_LIST, max_length=1, default="", blank=True)
    ###
    a1m_previous_residence_1st_start_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_1st_end_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_1st_district = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_1st_city = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_1st_zipcode = models.CharField(max_length=10, blank=True)
    ###
    a1m_previous_residence_2nd_start_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_2nd_end_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_2nd_district = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_2nd_city = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_2nd_zipcode = models.CharField(max_length=10, blank=True)
    ##
    a1m_previous_residence_3rd_start_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_3rd_end_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_3rd_district = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_3rd_city = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_3rd_zipcode = models.CharField(max_length=10, blank=True)
    ##
    a1m_previous_residence_4th_start_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_4th_end_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_4th_district = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_4th_city = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_4th_zipcode = models.CharField(max_length=10, blank=True)
    ##
    a1m_previous_residence_5th_start_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_5th_end_year = models.CharField(max_length=15, blank=True)
    a1m_previous_residence_5th_district = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_5th_city = models.CharField(max_length=25, blank=True)
    a1m_previous_residence_5th_zipcode = models.CharField(max_length=10, blank=True)
    ##
    a1m_home_phone_number = models.CharField(max_length=25, blank=True)
    a1m_mobile_phone_number = models.CharField(max_length=25, blank=True)
    a1m_email = models.EmailField(blank=True)
    EDUCATION_LEVEL_LIST = (
                        ('', ''),
                        ('1', 'Illiterate'),
                        ('2', 'Elementary'),
                        ('3', 'High School'),
                        ('4', 'Undergraduate'),
                        ('5', 'Postgraduate'),  
        )
    a1m_education_level = models.CharField(choices=EDUCATION_LEVEL_LIST, max_length=1, default="", blank=True)
    a1m_family_income = models.CharField(max_length=15, blank=True)
    MARITAL_STATUS_LIST = (
                        ('', ''),
                        ('1', 'Married'),
                        ('2', 'Divorced/Unmaried'), 
        )
    a1m_marital_status = models.CharField(choices=MARITAL_STATUS_LIST,max_length=1, default="", blank=True)
    ##
    a1m_relative_name = models.CharField(max_length=25, blank=True)
    a1m_relative_street = models.CharField(max_length=25, blank=True)
    a1m_relative_rt = models.CharField(max_length=3, blank=True)
    a1m_relative_rw = models.CharField(max_length=3, blank=True)
    a1m_relative_district = models.CharField(max_length=25, blank=True)
    a1m_relative_city = models.CharField(max_length=25, blank=True)
    a1m_relative_zipcode = models.CharField(max_length=10, blank=True)
    a1m_relative_home_phone_number = models.CharField(max_length=25, blank=True)
    a1m_relative_mobile_phone_number = models.CharField(max_length=25, blank=True)
    a1m_notes = models.TextField(blank=True)
    def __str__(self):
        return "[participant_id : " + unicode(self.participant_id)+"]"

class A2MotherEmployment(models.Model):
    a_form = models.ForeignKey(ABaseLine, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=25, blank=True)
    updated_by = models.CharField(max_length=25, blank=True)
    created_time = models.CharField(max_length=28, blank=True)
    updated_time = models.CharField(max_length=28, blank=True)
    participant_id = models.CharField(max_length=10, blank=True)
    EMPLOYMENT_STATUS_LIST = (
                        ('', ''),
                        ('1', 'Employed'),
                        ('2', 'Self-employed'),
                        ('0', 'Unemployed'),    
        )
    a2m_working_status = models.CharField(choices=EMPLOYMENT_STATUS_LIST, max_length=1, default="", blank=True)
    a2m_working_type = models.CharField(max_length=25, blank=True)
    a2m_working_pregnancy = models.NullBooleanField(default=False, blank=True)
    a2m_maternal_leave = models.NullBooleanField(default=False, blank=True)
    a2m_maternal_leave_duration = models.IntegerField(null=True, blank=True)
    a2m_work_street = models.CharField(max_length=25, blank=True)
    a2m_work_rt = models.CharField(max_length=3, blank=True)
    a2m_work_rw = models.CharField(max_length=3, blank=True)
    a2m_work_district = models.CharField(max_length=25, blank=True)
    a2m_work_city = models.CharField(max_length=25, blank=True)
    a2m_work_zipcode = models.CharField(max_length=10, blank=True)
    a2m_work_phone_number = models.CharField(max_length=25, blank=True)
    a2m_travel_by_car = models.NullBooleanField(default=False, blank=True)
    a2m_travel_by_motorcycle = models.NullBooleanField(default=False, blank=True)
    a2m_travel_by_cycling = models.NullBooleanField(default=False, blank=True)
    a2m_travel_by_walking = models.NullBooleanField(default=False, blank=True)
    a2m_travel_by_public_transport = models.NullBooleanField(default=False, blank=True)
    a2m_public_transport_type = models.CharField(max_length=25, blank=True)
    a2m_work_time_travel = models.IntegerField(null=True, blank=True)
    a2m_is_exposed_to_pollution = models.NullBooleanField(default=False, blank=True)
    a2m_working_hours = models.IntegerField(null=True, blank=True)
    WORKING_AREA_LIST = (
                        ('', ''),
                        ('1', 'Indoor'),
                        ('2', 'Outdoor'),   
        )
    a2m_working_area = models.CharField(choices=WORKING_AREA_LIST, max_length=1, default="", blank=True)
    a2m_notes = models.TextField(blank=True)
    def __str__(self):
        return "[participant_id : " + unicode(self.participant_id)+"]"


## A3 sampao A5 belum diperbaiki nama fieldnya ##
class A3Obstetric(models.Model):
    a_form = models.ForeignKey(ABaseLine, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=25, blank=True)
    updated_by = models.CharField(max_length=25, blank=True)
    created_time = models.CharField(max_length=28, blank=True)
    updated_time = models.CharField(max_length=28, blank=True)
    participant_id = models.CharField(max_length=10, blank=True)
    a3m_pre_pregnancy_weight = models.CharField(max_length=25, blank=True)
    a3m_pre_pregnancy_height = models.CharField(max_length=25, blank=True)
    a3m_first_day_last_menstruation = models.CharField(max_length=15, blank=True)
    a3m_estimated_due_date = models.CharField(max_length=15, blank=True)
    a3m_gravida = models.CharField(max_length=25, blank=True)
    a3m_parity = models.CharField(max_length=25, blank=True)
    a3m_abortus = models.CharField(max_length=25, blank=True)
    a3m_previous_premature = models.NullBooleanField(blank=True)
    a3m_previous_miscarriage = models.NullBooleanField(blank=True)
    a3m_previous_complication = models.NullBooleanField(blank=True)
    a3m_hypertension_complication = models.NullBooleanField(blank=True)
    a3m_diabetes_complication = models.NullBooleanField(blank=True)
    a3m_preeclampsia_complication = models.NullBooleanField(blank=True)
    a3m_eclampsia_complication = models.NullBooleanField(blank=True)
    a3m_infection_complication = models.NullBooleanField(blank=True)
    a3m_other_complication = models.NullBooleanField(blank=True)
    a3m_other_complication_name = models.CharField(max_length=25, blank=True)
    a3m_medical_history = models.NullBooleanField(blank=True)
    a3m_asthma_history = models.NullBooleanField(blank=True)
    a3m_tubercolosis_history = models.NullBooleanField(blank=True)
    a3m_cronic_cough_history = models.NullBooleanField(blank=True)
    a3m_hypertension_history = models.NullBooleanField(blank=True)
    a3m_heart_disease_history = models.NullBooleanField(blank=True)
    a3m_heart_disease_coronary = models.NullBooleanField(blank=True)
    a3m_heart_disease_valve = models.NullBooleanField(blank=True)
    a3m_heart_disease_rhythm = models.NullBooleanField(blank=True)
    a3m_heart_disease_muscle = models.NullBooleanField(blank=True)
    a3m_diabetes_history = models.NullBooleanField(blank=True)
    a3m_is_use_insulin = models.NullBooleanField(blank=True)
    a3m_stroke_history = models.NullBooleanField(blank=True)
    a3m_allergy_history = models.NullBooleanField(blank=True)
    a3m_allergy_detail = models.CharField(max_length=25, blank=True)
    a3m_other_history = models.NullBooleanField(blank=True)
    a3m_other_detail = models.CharField(max_length=25, blank=True)
    a3m_family_disease = models.NullBooleanField(blank=True)
    a3m_asthma_mother = models.NullBooleanField(blank=True)
    a3m_asthma_father = models.NullBooleanField(blank=True)
    a3m_asthma_sibling = models.NullBooleanField(blank=True)
    a3m_hypertension_mother = models.NullBooleanField(blank=True)
    a3m_hypertension_father = models.NullBooleanField(blank=True)
    a3m_hypertension_sibling = models.NullBooleanField(blank=True)
    a3m_heart_disease_mother = models.NullBooleanField(blank=True)
    a3m_heart_disease_father = models.NullBooleanField(blank=True)
    a3m_heart_disease_sibling = models.NullBooleanField(blank=True)
    a3m_diabetes_mother = models.NullBooleanField(blank=True)
    a3m_diabetes_father = models.NullBooleanField(blank=True)
    a3m_diabetes_sibling = models.NullBooleanField(blank=True)
    a3m_stroke_mother = models.NullBooleanField(blank=True)
    a3m_stroke_father = models.NullBooleanField(blank=True)
    a3m_stroke_sibling = models.NullBooleanField(blank=True)
    a3m_other_disease = models.NullBooleanField(blank=True)
    a3m_other_disease_name = models.CharField(max_length=25, blank=True)
    a3m_other_mother = models.NullBooleanField(blank=True)
    a3m_other_father = models.NullBooleanField(blank=True)
    a3m_other_sibling = models.NullBooleanField(blank=True)
    a3m_notes = models.TextField(blank=True)
    def __str__(self):
        return "[participant_id : " + unicode(self.participant_id)+"]"

class A4Father(models.Model):
    a_form = models.ForeignKey(ABaseLine, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=25, blank=True)
    updated_by = models.CharField(max_length=25, blank=True)
    created_time = models.CharField(max_length=28, blank=True)
    updated_time = models.CharField(max_length=28, blank=True)
    participant_id = models.CharField(max_length=10, blank=True)
    
    a4f_name = models.CharField(max_length=25, blank=True)
    a4f_pob = models.CharField(max_length=25, blank=True)
    a4f_dob = models.CharField(max_length=15, blank=True)
    a4f_residence_street = models.CharField(max_length=25, blank=True)
    a4f_residence_rt = models.CharField(max_length=3, blank=True)
    a4f_residence_rw = models.CharField(max_length=3, blank=True)
    a4f_residence_district = models.CharField(max_length=25, blank=True)
    a4f_residence_city = models.CharField(max_length=25, blank=True)
    a4f_residence_zipcode = models.CharField(max_length=10, blank=True)
    a4f_home_phone_number = models.CharField(max_length=25, blank=True)
    a4f_mobile_phone_number = models.CharField(max_length=25, blank=True)
    a4f_email = models.EmailField(blank=True)
    EDUCATION_LEVEL_LIST = (
                        ('', ''),
                        ('1', 'Illiterate'),
                        ('2', 'Elementary'),
                        ('3', 'High School'),
                        ('4', 'Undergraduate'),
                        ('5', 'Postgraduate'),  
        )
    a4f_education_level = models.CharField(choices=EDUCATION_LEVEL_LIST, max_length=1, default="", blank=True)
    a4f_weight = models.CharField(max_length=25, blank=True)
    a4f_height = models.CharField(max_length=25, blank=True)
    
    EMPLOYMENT_STATUS_LIST = (
                        ('', ''),
                        ('1', 'Employed'),
                        ('2', 'Self-employed'),
                        ('0', 'Unemployed'),
                         
        )
    a4f_employment_status = models.CharField(choices=EMPLOYMENT_STATUS_LIST, max_length=1, default="", blank=True)
    a4f_type_of_job = models.CharField(max_length=25, blank=True)
    a4f_work_street = models.CharField(max_length=25, blank=True)
    a4f_work_rt = models.CharField(max_length=3, blank=True)
    a4f_work_rw = models.CharField(max_length=3, blank=True)
    a4f_work_district = models.CharField(max_length=25, blank=True)
    a4f_work_city = models.CharField(max_length=25, blank=True)
    a4f_work_zipcode = models.CharField(max_length=10, blank=True)
    a4f_work_phone_number = models.CharField(max_length=25, blank=True)
    
    a4f_medical_history = models.NullBooleanField(blank=True)
    a4f_asthma_history = models.NullBooleanField(blank=True)
    a4f_tubercolosis_history = models.NullBooleanField(blank=True)
    a4f_cronic_cough_history = models.NullBooleanField(blank=True)
    a4f_hypertension_history = models.NullBooleanField(blank=True)
    a4f_heart_disease_history = models.NullBooleanField(blank=True)
    a4f_heart_disease_coronary = models.NullBooleanField(blank=True)
    a4f_heart_disease_valve = models.NullBooleanField(blank=True)
    a4f_heart_disease_rhythm = models.NullBooleanField(blank=True)
    a4f_heart_disease_muscle = models.NullBooleanField(blank=True)
    a4f_diabetes_history = models.NullBooleanField(blank=True)
    a4f_is_use_insulin = models.NullBooleanField(blank=True)
    a4f_stroke_history = models.NullBooleanField(blank=True)
    a4f_allergy_history = models.NullBooleanField(blank=True)
    a4f_allergy_detail = models.CharField(max_length=25, blank=True)
    a4f_other_history = models.NullBooleanField(blank=True)
    a4f_other_detail = models.CharField(max_length=25, blank=True)
    
    a4f_family_disease = models.NullBooleanField(blank=True)
    a4f_asthma_mother = models.NullBooleanField(blank=True)
    a4f_asthma_father = models.NullBooleanField(blank=True)
    a4f_asthma_sibling = models.NullBooleanField(blank=True)
    a4f_hypertension_mother = models.NullBooleanField(blank=True)
    a4f_hypertension_father = models.NullBooleanField(blank=True)
    a4f_hypertension_sibling = models.NullBooleanField(blank=True)
    a4f_heart_disease_mother = models.NullBooleanField(blank=True)
    a4f_heart_disease_father = models.NullBooleanField(blank=True)
    a4f_heart_disease_sibling = models.NullBooleanField(blank=True)
    a4f_diabetes_mother = models.NullBooleanField(blank=True)
    a4f_diabetes_father = models.NullBooleanField(blank=True)
    a4f_diabetes_sibling = models.NullBooleanField(blank=True)
    a4f_stroke_mother = models.NullBooleanField(blank=True)
    a4f_stroke_father = models.NullBooleanField(blank=True)
    a4f_stroke_sibling = models.NullBooleanField(blank=True)
    a4f_other_disease = models.NullBooleanField(blank=True)
    a4f_other_disease_name = models.CharField(max_length=25, blank=True)
    a4f_other_mother = models.NullBooleanField(blank=True)
    a4f_other_father = models.NullBooleanField(blank=True)
    a4f_other_sibling = models.NullBooleanField(blank=True)
    
    a4m_notes = models.TextField(blank=True)
    def __str__(self):
        return "[participant_id : " + unicode(self.participant_id)+"]"


class A5PrePregnancySmoking(models.Model):
    a_form = models.ForeignKey(ABaseLine, on_delete=models.PROTECT)
    created_by = models.CharField(max_length=25, blank=True)
    updated_by = models.CharField(max_length=25, blank=True)
    created_time = models.CharField(max_length=28, blank=True)
    updated_time = models.CharField(max_length=28, blank=True)
    participant_id = models.CharField(max_length=10, blank=True)
    SMOKING_STATUS_LIST = (
                    ('', ''),   
                    ('1', 'Smoker'),
                    ('2', 'Ex-smoker'),
                    ('0', 'Never smoke'),
        )
    a5m_mother_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, default="", null=True, blank=True)
    a5m_mother_quit_duration = models.IntegerField(null=True, blank=True)
    a5m_mother_start_smoke_age = models.IntegerField(null=True, blank=True)
    a5m_mother_cigarretes_per_day = models.IntegerField(null=True, blank=True)
    a5m_mother_smoke_pipes = models.NullBooleanField(blank=True)
    a5m_other_member_smoke = models.NullBooleanField(blank=True)
    a5m_other_member_smoke_number = models.IntegerField(null=True, blank=True)
    a5m_total_cigarretes_per_day = models.IntegerField(null=True, blank=True)
    a5m_smoke_in_front_of = models.NullBooleanField(blank=True)
    ##
    a5f_father_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, default="", null=True, blank=True)
    a5f_father_quit_duration = models.IntegerField(null=True, blank=True)
    a5f_father_start_smoke_age = models.IntegerField(null=True, blank=True)
    a5f_father_cigarretes_per_day = models.IntegerField(null=True, blank=True)
    a5f_father_smoke_pipes = models.NullBooleanField(blank=True)
    SMOKING_FREQUENCY_LIST = (
                        ('', ''),
                        ('1','Daily'),
                        ('2','Weekly'),
                        ('3', 'Monthly'),
                        ('0','Never'),
        )
    a5f_father_smoke_frequency = models.CharField(choices=SMOKING_FREQUENCY_LIST, max_length=1, default="", null=True, blank=True)
    a5f_smoke_in_front_of_mother = models.NullBooleanField(blank=True)
    ###
    a5c_colleagues_smoking_status = models.NullBooleanField(blank=True)
    a5c_colleagues_smoke = models.IntegerField(null=True, blank=True)
    a5c_duration_with_smokers_per_day = models.IntegerField(null=True, blank=True)
    a5c_month_duration_with_smokers = models.IntegerField(null=True, blank=True)
    a5m_notes = models.TextField(blank=True)
    def __str__(self):
        return "[participant_id : " + unicode(self.participant_id)+"]"