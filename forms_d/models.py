"""
CATATAN
=======
empty value pada model ini
 > Char = empty string
 > Boolean = None
 > Integer = None (Null)

semua IntergerField di sini memiliki sifat Null = True
"""

from __future__ import unicode_literals
from django.db import models
from core.models import *

###### First Visit ######

class DInfant(models.Model):
	participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
	date_admission = models.CharField(max_length=15, blank=True)
	child_id = models.CharField(max_length=12, blank=True)
	child_name = models.CharField(max_length=25, blank=True)
	interviewer_id = models.CharField(max_length=25, blank=True)
	date_interviewed = models.CharField(max_length=15, blank=True)
	data_entry_id = models.CharField(max_length=25, blank=True)
	date_data_entered = models.CharField(max_length=15, blank=True)
	data_checked_id = models.CharField(max_length=25, blank=True, null=True)
	date_data_checked = models.CharField(max_length=15, blank=True)
	is_save_all = models.NullBooleanField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant.participant_id)+ ", participant_name : "+unicode(self.participant.name )+ ", child_name : "+unicode(self.child_name )+ ", interviewer_id : "+unicode(self.interviewer_id )+ ", data_entry_id : "+unicode(self.data_entry_id )+ ", is_save_all : "+unicode(self.is_save_all )+ ", date_data_checked : "+ unicode(self.date_data_checked )+"]"

class D1InfantGrowth(models.Model):
	d_form = models.ForeignKey(DInfant, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d1c_ur_number = models.CharField(max_length=25, blank=True)
	d1c_first_name = models.CharField(max_length=25, blank=True)
	d1c_surname = models.CharField(max_length=25, blank=True)
	d1c_dob = models.CharField(max_length=15, blank=True)
	d1c_weight_1st = models.CharField(max_length=25, blank=True)
	d1c_weight_2nd = models.CharField(max_length=25, blank=True)
	d1c_length_1st = models.CharField(max_length=25, blank=True)
	d1c_length_2nd = models.CharField(max_length=25, blank=True)
	d1c_hc_1st = models.CharField(max_length=25, blank=True)
	d1c_hc_2nd = models.CharField(max_length=25, blank=True)
	d1c_chest_1st = models.CharField(max_length=25, blank=True)
	d1c_chest_2nd = models.CharField(max_length=25, blank=True)
	d1c_ac_1st = models.CharField(max_length=25, blank=True)
	d1c_ac_2nd = models.CharField(max_length=25, blank=True)
	d1c_vaccination_history = models.NullBooleanField(blank=True)
	d1c_bcg = models.NullBooleanField(blank=True)
	d1c_bcg_date = models.CharField(max_length=15, blank=True)
	d1c_hep_b = models.NullBooleanField(blank=True)
	d1c_hep_b_date = models.CharField(max_length=15, blank=True)
	d1c_dpt = models.NullBooleanField(blank=True)
	d1c_dpt_date = models.CharField(max_length=15, blank=True)
	d1c_ipv = models.NullBooleanField(blank=True)
	d1c_ipv_date = models.CharField(max_length=15, blank=True)
	d1c_opv = models.NullBooleanField(blank=True)
	d1c_opv_date = models.CharField(max_length=15, blank=True)
	d1c_hib = models.NullBooleanField(blank=True)
	d1c_hib_date = models.CharField(max_length=15, blank=True)
	d1c_rotavirus = models.NullBooleanField(blank=True)
	d1c_rotavirus_date = models.CharField(max_length=15, blank=True)
	d1c_pneumococcus = models.NullBooleanField(blank=True)
	d1c_pneumococcus_date = models.CharField(max_length=15, blank=True)
	d1c_influenza = models.NullBooleanField(blank=True)
	d1c_influenza_date = models.CharField(max_length=15, blank=True)
	d1_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D2InfantFeeding(models.Model):
	d_form = models.ForeignKey(DInfant, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d2c_breast_feeding_status = models.NullBooleanField(blank=True)
	d2c_supplementary_food = models.NullBooleanField(blank=True)
	d2c_infant_formula = models.NullBooleanField(blank=True)
	d2c_age_formula = models.CharField(max_length=15, blank=True)
	d2c_cows_milk_formula = models.NullBooleanField(blank=True)
	d2c_soy_formula = models.NullBooleanField(blank=True)
	d2c_hypo_allergen_formula = models.NullBooleanField(blank=True)
	d2c_hydrolized_formula = models.NullBooleanField(blank=True)
	d2c_amino_formula = models.NullBooleanField(blank=True)
	d2c_weaning_food = models.NullBooleanField(blank=True)
	d2c_age_weaning_food = models.CharField(max_length=15, blank=True)
	d2_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D3InfantCardiovascular(models.Model):
	d_form = models.ForeignKey(DInfant, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d3c_date_blood_pressure = models.CharField(max_length=15, blank=True)
	d3c_examiner_bp = models.CharField(max_length=25, blank=True)
	d3c_systolic_1st = models.CharField(max_length=25, blank=True)
	d3c_systolic_2nd = models.CharField(max_length=25, blank=True)
	d3c_systolic_3rd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_1st = models.CharField(max_length=25, blank=True)
	d3c_diastolic_2nd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_3rd = models.CharField(max_length=25, blank=True)
	d3c_pulse_1st = models.CharField(max_length=25, blank=True)
	d3c_pulse_2nd = models.CharField(max_length=25, blank=True)
	d3c_pulse_3rd = models.CharField(max_length=25, blank=True)
	d3c_date_echo = models.CharField(max_length=15, blank=True)
	d3c_examiner_echo = models.CharField(max_length=25, blank=True)
	CINELOOPS_OBTAINED_STATUS_LIST = (
						('', ''),
						('1', '4 chamber view'),
						('2', '5 chamber view'),
						('3', 'Parasternal long axis'),
						('4', 'Short axis view'),		
	)
	#d3c_cineloops = models.CharField(choices=CINELOOPS_OBTAINED_STATUS_LIST, max_length=1, default="")
	d3c_cineloops = models.CharField(choices=CINELOOPS_OBTAINED_STATUS_LIST, max_length=1, blank=True)
	d3c_heart_abnormality = models.NullBooleanField(blank=True)
	d3c_heart_abnormality_detail = models.CharField(max_length=25, blank=True)
	d3c_lvidd_1st = models.CharField(max_length=25, blank=True)
	d3c_lvidd_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvidd_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvids_1st = models.CharField(max_length=25, blank=True)
	d3c_lvids_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvids_3rd = models.CharField(max_length=25, blank=True)
	d3c_ivsd_1st = models.CharField(max_length=25, blank=True)
	d3c_ivsd_2nd = models.CharField(max_length=25, blank=True)
	d3c_ivsd_3rd = models.CharField(max_length=25, blank=True)
	d3c_ivss_1st = models.CharField(max_length=25, blank=True)
	d3c_ivss_2nd = models.CharField(max_length=25, blank=True)
	d3c_ivss_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_1st = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvpws_1st = models.CharField(max_length=25, blank=True)
	d3c_lvpws_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvpws_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvef_1st = models.CharField(max_length=25, blank=True)
	d3c_lvef_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvef_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvfs_1st = models.CharField(max_length=25, blank=True)
	d3c_lvfs_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvfs_3rd = models.CharField(max_length=25, blank=True)
	d3c_tvr_1st = models.CharField(max_length=25, blank=True)
	d3c_tvr_2nd = models.CharField(max_length=25, blank=True)
	d3c_tvr_3rd = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_1st = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_2nd = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_3rd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_1st = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_2nd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_3rd = models.CharField(max_length=25, blank=True)
	d3c_tapse_1st = models.CharField(max_length=25, blank=True)
	d3c_tapse_2nd = models.CharField(max_length=25, blank=True)
	d3c_tapse_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_e_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_a_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_s_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_e_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_a_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_s_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_e_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_a_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_s_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_e_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_a_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_s_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_date_vaskular = models.CharField(max_length=15, blank=True)
	d3c_examiner_vaskular = models.CharField(max_length=25, blank=True)
	d3c_cineloops_abdominal = models.NullBooleanField(blank=True)
	d3c_imt_1st = models.CharField(max_length=25, blank=True)
	d3c_imt_2nd = models.CharField(max_length=25, blank=True)
	d3c_imt_3rd = models.CharField(max_length=25, blank=True)
	d3c_sdimt_1st = models.CharField(max_length=25, blank=True)
	d3c_sdimt_2nd = models.CharField(max_length=25, blank=True)
	d3c_sdimt_3rd = models.CharField(max_length=25, blank=True)
	d3c_distension_1st = models.CharField(max_length=25, blank=True)
	d3c_distension_2nd = models.CharField(max_length=25, blank=True)
	d3c_distension_3rd = models.CharField(max_length=25, blank=True)
	d3c_diameter_1st = models.CharField(max_length=25, blank=True)
	d3c_diameter_2nd = models.CharField(max_length=25, blank=True)
	d3c_diameter_3rd = models.CharField(max_length=25, blank=True)
	d3_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"


class D4InfantLungFunction(models.Model):
	d_form = models.ForeignKey(DInfant, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d4c_date_lung = models.CharField(max_length=15, blank=True)
	d4c_examiner_lung = models.CharField(max_length=25, blank=True)
	d4c_resistance_1st = models.CharField(max_length=25, blank=True)
	d4c_resistance_2nd = models.CharField(max_length=25, blank=True)
	d4c_compliance_1st = models.CharField(max_length=25, blank=True)
	d4c_compliance_2nd = models.CharField(max_length=25, blank=True)
	d4c_time_constant_1st = models.CharField(max_length=25, blank=True)
	d4c_time_constant_2nd = models.CharField(max_length=25, blank=True)
	d4c_fvc_1st = models.CharField(max_length=25, blank=True)
	d4c_fvc_2nd = models.CharField(max_length=25, blank=True)
	d4c_fev1_1st = models.CharField(max_length=25, blank=True)
	d4c_fev1_2nd = models.CharField(max_length=25, blank=True)
	d4c_respiratory_symptom = models.NullBooleanField(blank=True)
	FREQUENCY_STATUS_LIST = (
						('', ''),
						('0', 'Not at all'),
						('1', 'Once'),
						('2', 'Twice'),
						('3', '3 or more'),
						('4', 'Every day'),		
	)
	#d4c_dry_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, default="")
	d4c_dry_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_phlegmy_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_runny_nose = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_stuffed_nose = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_wheeze = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_breath_shortness = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_rattly_chest = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_snoring = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_stridor = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D5InfantBiological(models.Model):
	d_form = models.ForeignKey(DInfant, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d5c_blood = models.NullBooleanField(blank=True)
	d5c_blood_date = models.CharField(max_length=15, blank=True)
	# d5c_buccal_swab = models.NullBooleanField(blank=True)
	# d5c_buccal_swab_date = models.CharField(max_length=15, blank=True)
	d5c_hair_1 = models.NullBooleanField(blank=True)
	d5c_hair_1_date = models.CharField(max_length=15, blank=True)
	d5c_hair_6 = models.NullBooleanField(blank=True)
	d5c_hair_6_date = models.CharField(max_length=15, blank=True)
	d5c_nail_1 = models.NullBooleanField(blank=True)
	d5c_nail_1_date = models.CharField(max_length=15, blank=True)
	d5c_nail_6 = models.NullBooleanField(blank=True)
	d5c_nail_6_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_2 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_2_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_4 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_4_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_6 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_6_date = models.CharField(max_length=15, blank=True)
	d5_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D6CurrentSmoking(models.Model):
	d_form = models.ForeignKey(DInfant, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	SMOKING_STATUS_LIST = (
					('', ''),
					('1', 'Smoker'),
					('2', 'Ex-smoker'),
					('0', 'Never smoke'),
		)
	SMOKING_FREQUENCY_LIST = (
						('', ''),
						('1','Daily'),
						('2','Weekly'),
						('3', 'Monthly'),
						('0','Never'),
		)
	#d6m_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, default="")
	d6m_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, blank=True)
	d6m_quitting_smoke = models.NullBooleanField(blank=True)
	d6m_quitting_duration = models.CharField(max_length=15, blank=True)
	d6m_cigar_number = models.CharField(max_length=15, blank=True)
	d6m_cigar_type = models.NullBooleanField(blank=True)
	d6m_smoking_household = models.NullBooleanField(blank=True)
	d6m_household_number = models.CharField(max_length=15, blank=True)
	d6m_household_cigar_number = models.CharField(max_length=15, blank=True)
	d6m_household_presence = models.NullBooleanField(blank=True)

	d6f_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, blank=True)
	d6f_quitting_duration = models.CharField(max_length=15, blank=True)
	d6f_cigar_number = models.CharField(max_length=15, blank=True)
	d6f_cigar_type = models.NullBooleanField(blank=True)
	d6f_smoking_frequency = models.CharField(choices=SMOKING_FREQUENCY_LIST, max_length=1, blank=True)
	d6f_smoking_presence = models.NullBooleanField(blank=True)
	d6_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D7Infection(models.Model):
	d_form = models.ForeignKey(DInfant, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d7c_infection = models.NullBooleanField(blank=True)
	d7c_infection_upper_respi = models.NullBooleanField(blank=True)
	d7c_infection_lower_respi = models.NullBooleanField(blank=True)
	d7c_infection_gastro = models.NullBooleanField(blank=True)
	d7c_infection_urinary = models.NullBooleanField(blank=True)
	d7c_infection_cns = models.NullBooleanField(blank=True)
	d7c_infection_sepsis = models.NullBooleanField(blank=True)
	d7c_infection_dengue = models.NullBooleanField(blank=True)
	d7c_infection_others = models.NullBooleanField(blank=True)
	d7c_infection_others_detail = models.CharField(max_length=25, blank=True)
	d7c_infection_unknown = models.NullBooleanField(blank=True)
	d7c_physician_clinic = models.CharField(max_length=25, blank=True)
	#d7c_contact = models.CharField(max_length=25, blank=True)
	d7c_infection_symptoms = models.NullBooleanField(blank=True)
	d7c_symptoms_respi = models.NullBooleanField(blank=True)
	d7c_symptoms_gastro = models.NullBooleanField(blank=True)
	d7c_symptoms_skin = models.NullBooleanField(blank=True)
	d7c_symptoms_nervous = models.NullBooleanField(blank=True)
	d7c_hospitalization = models.NullBooleanField(blank=True)
	d7c_admission_date = models.CharField(max_length=15, blank=True)
	d7c_discharged_date = models.CharField(max_length=15, blank=True)
	d7c_hospital = models.CharField(max_length=25, blank=True)
	d7c_physician = models.CharField(max_length=25, blank=True)
	d7c_hospital_contact = models.CharField(max_length=25, blank=True)
	WARD_STATUS_LIST = (
						('', ''),
						('1','Emergency room only'),
						('2','One day care'),
						('3', 'General Ward'),
						('4','High care/intensive care'),
		)
	#d7c_ward = models.CharField(choices=WARD_STATUS_LIST, max_length=1, default="")
	d7c_ward = models.CharField(choices=WARD_STATUS_LIST, max_length=1, blank=True)
	d7c_additional_test = models.NullBooleanField(blank=True)
	d7c_blood_test = models.NullBooleanField(blank=True)
	d7c_blood_count = models.NullBooleanField(blank=True)
	d7c_crp = models.NullBooleanField(blank=True)
	d7c_procalcitonin = models.NullBooleanField(blank=True)
	d7c_blood_culture = models.NullBooleanField(blank=True)
	d7c_blood_culture_date = models.CharField(max_length=15, blank=True)
	d7c_blood_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_blood_microorganism = models.CharField(max_length=25, blank=True)
	d7c_typhoid = models.NullBooleanField(blank=True)
	d7c_dengue_ns_1 = models.NullBooleanField(blank=True)
	d7c_dengue = models.NullBooleanField(blank=True)
	d7c_nasopharyngeal = models.NullBooleanField(blank=True)
	d7c_urine = models.NullBooleanField(blank=True)
	d7c_urinalysis = models.NullBooleanField(blank=True)
	d7c_urinalysis_date = models.CharField(max_length=15, blank=True)
	d7c_urine_culture = models.NullBooleanField(blank=True)
	d7c_urine_date = models.CharField(max_length=15, blank=True)
	d7c_urine_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_urine_microorganism = models.CharField(max_length=25, blank=True)
	d7c_csf = models.NullBooleanField(blank=True)
	d7c_csf_date = models.CharField(max_length=15, blank=True)
	d7c_csf_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_csf_microorganism = models.CharField(max_length=25, blank=True)
	d7c_faecal_analysis = models.NullBooleanField(blank=True)
	d7c_faecal_analysis_date = models.CharField(max_length=15, blank=True)
	d7c_faecal_culture = models.NullBooleanField(blank=True)
	d7c_faecal_date = models.CharField(max_length=15, blank=True)
	d7c_faecal_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_faecal_microorganism = models.CharField(max_length=25, blank=True)
	d7c_chest_xray = models.NullBooleanField(blank=True)
	d7c_chest_xray_findings = models.CharField(max_length=25, blank=True)
	d7c_usg = models.NullBooleanField(blank=True)
	d7c_usg_type = models.CharField(max_length=25, blank=True)
	d7c_usg_date = models.CharField(max_length=15, blank=True)
	d7c_usg_findings = models.CharField(max_length=25, blank=True)
	d7c_mri = models.NullBooleanField(blank=True)
	d7c_mri_type = models.CharField(max_length=25, blank=True)
	d7c_mri_date = models.CharField(max_length=15, blank=True)
	d7c_mri_findings = models.CharField(max_length=25, blank=True)
	d7c_other_test = models.NullBooleanField(blank=True)
	d7c_other_test_type = models.CharField(max_length=25, blank=True)
	d7c_other_test_date = models.CharField(max_length=15, blank=True)
	d7c_other_test_findings = models.CharField(max_length=25, blank=True)
	d7c_medication = models.NullBooleanField(blank=True)
	d7c_med1_name = models.CharField(max_length=25, blank=True)
	d7c_med1_dosage = models.CharField(max_length=25, blank=True)
	d7c_med1_start_date = models.CharField(max_length=15, blank=True)
	d7c_med1_end_date = models.CharField(max_length=15, blank=True)
	d7c_med2_name = models.CharField(max_length=25, blank=True)
	d7c_med2_dosage = models.CharField(max_length=25, blank=True)
	d7c_med2_start_date = models.CharField(max_length=15, blank=True)
	d7c_med2_end_date = models.CharField(max_length=15, blank=True)
	d7c_med3_name = models.CharField(max_length=25, blank=True)
	d7c_med3_dosage = models.CharField(max_length=25, blank=True)
	d7c_med3_start_date = models.CharField(max_length=15, blank=True)
	d7c_med3_end_date = models.CharField(max_length=15, blank=True)
	d7c_med4_name = models.CharField(max_length=25, blank=True)
	d7c_med4_dosage = models.CharField(max_length=25, blank=True)
	d7c_med4_start_date = models.CharField(max_length=15, blank=True)
	d7c_med4_end_date = models.CharField(max_length=15, blank=True)
	d7c_med5_name = models.CharField(max_length=25, blank=True)
	d7c_med5_dosage = models.CharField(max_length=25, blank=True)
	d7c_med5_start_date = models.CharField(max_length=15, blank=True)
	d7c_med5_end_date = models.CharField(max_length=15, blank=True)
	d7_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D8PollutantExposure(models.Model):
	d_form = models.ForeignKey(DInfant, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d8m_charcoal = models.NullBooleanField(blank=True)
	d8m_kerosene = models.NullBooleanField(blank=True)
	d8m_wood = models.NullBooleanField(blank=True)
	d8m_gas = models.NullBooleanField(blank=True)
	d8m_electric = models.NullBooleanField(blank=True)
	d8m_other = models.NullBooleanField(blank=True)
	d8m_other_detail = models.CharField(max_length=25, blank=True)
	d8m_cooking_exhaust = models.NullBooleanField(blank=True)
	d8m_pesticide = models.NullBooleanField(blank=True)	
	GARBAGE_BURNING_STATUS_LIST = (
						('', ''),
						('0','No'),
						('1','Once per week or less'),
						('2', 'More than once per week but not daily'),
						('3','Daily'),
		)
	#d8m_garbage_burning = models.CharField(choices=GARBAGE_BURNING_STATUS_LIST, max_length=1, default="")
	d8m_garbage_burning = models.CharField(choices=GARBAGE_BURNING_STATUS_LIST, max_length=1, blank=True)
	d8m_pet = models.NullBooleanField(blank=True)
	d8m_pet_detail = models.CharField(max_length=25, blank=True)
	HOUSING_TYPE_LIST = (
						('', ''),
						('1','Landed House'),
						('2', 'Flat/Apartment'),
		)
	d8m_housing_type = models.CharField(choices=HOUSING_TYPE_LIST, max_length=1, blank=True)
	LANDED_HOUSE_TYPE_LIST = (
						('', ''),
						('1','One story building'),
						('2', 'More than one story building'),
		)
	d8m_landed_house_type = models.CharField(choices=LANDED_HOUSE_TYPE_LIST, max_length=1, blank=True)
	d8m_apartment_level_number = models.CharField(max_length=15, blank=True)
	d8m_dampness_house = models.NullBooleanField(blank=True)
	d8m_ac = models.NullBooleanField(blank=True)
	d8m_fan = models.NullBooleanField(blank=True)
	d8m_air_filter = models.NullBooleanField(blank=True)
	d8m_staying_out_history = models.NullBooleanField(blank=True)
	##
	d8m_staying_out_1st_street = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_rt = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_rw = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_district = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_city = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_zipcode = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_duration = models.CharField(max_length=15, blank=True)

	d8m_staying_out_2nd_street = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_rt = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_rw = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_district = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_city = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_zipcode = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_duration = models.CharField(max_length=15, blank=True)
	d8_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"


###### End of First Visit ######


###### Second Visit ######

class DInfant2(models.Model):
	participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
	date_admission = models.CharField(max_length=15, blank=True)
	child_id = models.CharField(max_length=12, blank=True)
	child_name = models.CharField(max_length=25, blank=True)
	interviewer_id = models.CharField(max_length=25, blank=True)
	date_interviewed = models.CharField(max_length=15, blank=True)
	data_entry_id = models.CharField(max_length=25, blank=True)
	date_data_entered = models.CharField(max_length=15, blank=True)
	data_checked_id = models.CharField(max_length=25, blank=True, null=True)
	date_data_checked = models.CharField(max_length=15, blank=True)
	is_save_all = models.NullBooleanField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", participant_name : "+unicode(self.participant.name )+ ", child_name : "+unicode(self.child_name )+ ", interviewer_id : "+unicode(self.interviewer_id )+ ", data_entry_id : "+unicode(self.data_entry_id )+ ", is_save_all : "+unicode(self.is_save_all )+ ", date_data_checked : "+ unicode(self.date_data_checked )+"]"

class D1InfantGrowth2(models.Model):
	d_form = models.ForeignKey(DInfant2, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d1c_ur_number = models.CharField(max_length=25, blank=True)
	d1c_first_name = models.CharField(max_length=25, blank=True)
	d1c_surname = models.CharField(max_length=25, blank=True)
	d1c_dob = models.CharField(max_length=15, blank=True)
	d1c_weight_1st = models.CharField(max_length=25, blank=True)
	d1c_weight_2nd = models.CharField(max_length=25, blank=True)
	d1c_length_1st = models.CharField(max_length=25, blank=True)
	d1c_length_2nd = models.CharField(max_length=25, blank=True)
	d1c_hc_1st = models.CharField(max_length=25, blank=True)
	d1c_hc_2nd = models.CharField(max_length=25, blank=True)
	d1c_chest_1st = models.CharField(max_length=25, blank=True)
	d1c_chest_2nd = models.CharField(max_length=25, blank=True)
	d1c_ac_1st = models.CharField(max_length=25, blank=True)
	d1c_ac_2nd = models.CharField(max_length=25, blank=True)
	d1c_vaccination_history = models.NullBooleanField(blank=True)
	d1c_bcg = models.NullBooleanField(blank=True)
	d1c_bcg_date = models.CharField(max_length=15, blank=True)
	d1c_hep_b = models.NullBooleanField(blank=True)
	d1c_hep_b_date = models.CharField(max_length=15, blank=True)
	d1c_dpt = models.NullBooleanField(blank=True)
	d1c_dpt_date = models.CharField(max_length=15, blank=True)
	d1c_ipv = models.NullBooleanField(blank=True)
	d1c_ipv_date = models.CharField(max_length=15, blank=True)
	d1c_opv = models.NullBooleanField(blank=True)
	d1c_opv_date = models.CharField(max_length=15, blank=True)
	d1c_hib = models.NullBooleanField(blank=True)
	d1c_hib_date = models.CharField(max_length=15, blank=True)
	d1c_rotavirus = models.NullBooleanField(blank=True)
	d1c_rotavirus_date = models.CharField(max_length=15, blank=True)
	d1c_pneumococcus = models.NullBooleanField(blank=True)
	d1c_pneumococcus_date = models.CharField(max_length=15, blank=True)
	d1c_influenza = models.NullBooleanField(blank=True)
	d1c_influenza_date = models.CharField(max_length=15, blank=True)
	d1_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D2InfantFeeding2(models.Model):
	d_form = models.ForeignKey(DInfant2, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d2c_breast_feeding_status = models.NullBooleanField(blank=True)
	d2c_supplementary_food = models.NullBooleanField(blank=True)
	d2c_infant_formula = models.NullBooleanField(blank=True)
	d2c_age_formula = models.CharField(max_length=15, blank=True)
	d2c_cows_milk_formula = models.NullBooleanField(blank=True)
	d2c_soy_formula = models.NullBooleanField(blank=True)
	d2c_hypo_allergen_formula = models.NullBooleanField(blank=True)
	d2c_hydrolized_formula = models.NullBooleanField(blank=True)
	d2c_amino_formula = models.NullBooleanField(blank=True)
	d2c_weaning_food = models.NullBooleanField(blank=True)
	d2c_age_weaning_food = models.CharField(max_length=15, blank=True)
	d2_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D3InfantCardiovascular2(models.Model):
	d_form = models.ForeignKey(DInfant2, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d3c_date_blood_pressure = models.CharField(max_length=15, blank=True)
	d3c_examiner_bp = models.CharField(max_length=25, blank=True)
	d3c_systolic_1st = models.CharField(max_length=25, blank=True)
	d3c_systolic_2nd = models.CharField(max_length=25, blank=True)
	d3c_systolic_3rd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_1st = models.CharField(max_length=25, blank=True)
	d3c_diastolic_2nd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_3rd = models.CharField(max_length=25, blank=True)
	d3c_pulse_1st = models.CharField(max_length=25, blank=True)
	d3c_pulse_2nd = models.CharField(max_length=25, blank=True)
	d3c_pulse_3rd = models.CharField(max_length=25, blank=True)
	d3c_date_echo = models.CharField(max_length=15, blank=True)
	d3c_examiner_echo = models.CharField(max_length=25, blank=True)
	CINELOOPS_OBTAINED_STATUS_LIST = (
						('', ''),
						('1', '4 chamber view'),
						('2', '5 chamber view'),
						('3', 'Parasternal long axis'),
						('4', 'Short axis view'),		
	)
	#d3c_cineloops = models.CharField(choices=CINELOOPS_OBTAINED_STATUS_LIST, max_length=1, default="")
	d3c_cineloops = models.CharField(choices=CINELOOPS_OBTAINED_STATUS_LIST, max_length=1, blank=True)
	d3c_heart_abnormality = models.NullBooleanField(blank=True)
	d3c_heart_abnormality_detail = models.CharField(max_length=25, blank=True)
	d3c_lvidd_1st = models.CharField(max_length=25, blank=True)
	d3c_lvidd_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvidd_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvids_1st = models.CharField(max_length=25, blank=True)
	d3c_lvids_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvids_3rd = models.CharField(max_length=25, blank=True)
	d3c_ivsd_1st = models.CharField(max_length=25, blank=True)
	d3c_ivsd_2nd = models.CharField(max_length=25, blank=True)
	d3c_ivsd_3rd = models.CharField(max_length=25, blank=True)
	d3c_ivss_1st = models.CharField(max_length=25, blank=True)
	d3c_ivss_2nd = models.CharField(max_length=25, blank=True)
	d3c_ivss_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_1st = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvpws_1st = models.CharField(max_length=25, blank=True)
	d3c_lvpws_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvpws_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvef_1st = models.CharField(max_length=25, blank=True)
	d3c_lvef_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvef_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvfs_1st = models.CharField(max_length=25, blank=True)
	d3c_lvfs_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvfs_3rd = models.CharField(max_length=25, blank=True)
	d3c_tvr_1st = models.CharField(max_length=25, blank=True)
	d3c_tvr_2nd = models.CharField(max_length=25, blank=True)
	d3c_tvr_3rd = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_1st = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_2nd = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_3rd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_1st = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_2nd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_3rd = models.CharField(max_length=25, blank=True)
	d3c_tapse_1st = models.CharField(max_length=25, blank=True)
	d3c_tapse_2nd = models.CharField(max_length=25, blank=True)
	d3c_tapse_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_e_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_a_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_s_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_e_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_a_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_s_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_e_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_a_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_s_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_e_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_a_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_s_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_date_vaskular = models.CharField(max_length=15, blank=True)
	d3c_examiner_vaskular = models.CharField(max_length=25, blank=True)
	d3c_cineloops_abdominal = models.NullBooleanField(blank=True)
	d3c_imt_1st = models.CharField(max_length=25, blank=True)
	d3c_imt_2nd = models.CharField(max_length=25, blank=True)
	d3c_imt_3rd = models.CharField(max_length=25, blank=True)
	d3c_sdimt_1st = models.CharField(max_length=25, blank=True)
	d3c_sdimt_2nd = models.CharField(max_length=25, blank=True)
	d3c_sdimt_3rd = models.CharField(max_length=25, blank=True)
	d3c_distension_1st = models.CharField(max_length=25, blank=True)
	d3c_distension_2nd = models.CharField(max_length=25, blank=True)
	d3c_distension_3rd = models.CharField(max_length=25, blank=True)
	d3c_diameter_1st = models.CharField(max_length=25, blank=True)
	d3c_diameter_2nd = models.CharField(max_length=25, blank=True)
	d3c_diameter_3rd = models.CharField(max_length=25, blank=True)
	d3_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"


class D4InfantLungFunction2(models.Model):
	d_form = models.ForeignKey(DInfant2, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d4c_date_lung = models.CharField(max_length=15, blank=True)
	d4c_examiner_lung = models.CharField(max_length=25, blank=True)
	d4c_resistance_1st = models.CharField(max_length=25, blank=True)
	d4c_resistance_2nd = models.CharField(max_length=25, blank=True)
	d4c_compliance_1st = models.CharField(max_length=25, blank=True)
	d4c_compliance_2nd = models.CharField(max_length=25, blank=True)
	d4c_time_constant_1st = models.CharField(max_length=25, blank=True)
	d4c_time_constant_2nd = models.CharField(max_length=25, blank=True)
	d4c_fvc_1st = models.CharField(max_length=25, blank=True)
	d4c_fvc_2nd = models.CharField(max_length=25, blank=True)
	d4c_fev1_1st = models.CharField(max_length=25, blank=True)
	d4c_fev1_2nd = models.CharField(max_length=25, blank=True)
	d4c_respiratory_symptom = models.NullBooleanField(blank=True)
	FREQUENCY_STATUS_LIST = (
						('', ''),
						('0', 'Not at all'),
						('1', 'Once'),
						('2', 'Twice'),
						('3', '3 or more'),
						('4', 'Every day'),		
	)
	#d4c_dry_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, default="")
	d4c_dry_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_phlegmy_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_runny_nose = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_stuffed_nose = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_wheeze = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_breath_shortness = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_rattly_chest = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_snoring = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_stridor = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D5InfantBiological2(models.Model):
	d_form = models.ForeignKey(DInfant2, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d5c_blood = models.NullBooleanField(blank=True)
	d5c_blood_date = models.CharField(max_length=15, blank=True)
	# d5c_buccal_swab = models.NullBooleanField(blank=True)
	# d5c_buccal_swab_date = models.CharField(max_length=15, blank=True)
	d5c_hair_1 = models.NullBooleanField(blank=True)
	d5c_hair_1_date = models.CharField(max_length=15, blank=True)
	d5c_hair_6 = models.NullBooleanField(blank=True)
	d5c_hair_6_date = models.CharField(max_length=15, blank=True)
	d5c_nail_1 = models.NullBooleanField(blank=True)
	d5c_nail_1_date = models.CharField(max_length=15, blank=True)
	d5c_nail_6 = models.NullBooleanField(blank=True)
	d5c_nail_6_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_2 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_2_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_4 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_4_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_6 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_6_date = models.CharField(max_length=15, blank=True)
	d5_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D6CurrentSmoking2(models.Model):
	d_form = models.ForeignKey(DInfant2, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	SMOKING_STATUS_LIST = (
					('', ''),
					('1', 'Smoker'),
					('2', 'Ex-smoker'),
					('0', 'Never smoke'),
		)
	SMOKING_FREQUENCY_LIST = (
						('', ''),
						('1','Daily'),
						('2','Weekly'),
						('3', 'Monthly'),
						('0','Never'),
		)
	#d6m_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, default="")
	d6m_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, blank=True)
	d6m_quitting_smoke = models.NullBooleanField(blank=True)
	d6m_quitting_duration = models.CharField(max_length=15, blank=True)
	d6m_cigar_number = models.CharField(max_length=15, blank=True)
	d6m_cigar_type = models.NullBooleanField(blank=True)
	d6m_smoking_household = models.NullBooleanField(blank=True)
	d6m_household_number = models.CharField(max_length=15, blank=True)
	d6m_household_cigar_number = models.CharField(max_length=15, blank=True)
	d6m_household_presence = models.NullBooleanField(blank=True)

	d6f_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, blank=True)
	d6f_quitting_duration = models.CharField(max_length=15, blank=True)
	d6f_cigar_number = models.CharField(max_length=15, blank=True)
	d6f_cigar_type = models.NullBooleanField(blank=True)
	d6f_smoking_frequency = models.CharField(choices=SMOKING_FREQUENCY_LIST, max_length=1, blank=True)
	d6f_smoking_presence = models.NullBooleanField(blank=True)
	d6_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D7Infection2(models.Model):
	d_form = models.ForeignKey(DInfant2, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d7c_infection = models.NullBooleanField(blank=True)
	d7c_infection_upper_respi = models.NullBooleanField(blank=True)
	d7c_infection_lower_respi = models.NullBooleanField(blank=True)
	d7c_infection_gastro = models.NullBooleanField(blank=True)
	d7c_infection_urinary = models.NullBooleanField(blank=True)
	d7c_infection_cns = models.NullBooleanField(blank=True)
	d7c_infection_sepsis = models.NullBooleanField(blank=True)
	d7c_infection_dengue = models.NullBooleanField(blank=True)
	d7c_infection_others = models.NullBooleanField(blank=True)
	d7c_infection_others_detail = models.CharField(max_length=25, blank=True)
	d7c_infection_unknown = models.NullBooleanField(blank=True)
	d7c_physician_clinic = models.CharField(max_length=25, blank=True)
	#d7c_contact = models.CharField(max_length=25, blank=True)
	d7c_infection_symptoms = models.NullBooleanField(blank=True)
	d7c_symptoms_respi = models.NullBooleanField(blank=True)
	d7c_symptoms_gastro = models.NullBooleanField(blank=True)
	d7c_symptoms_skin = models.NullBooleanField(blank=True)
	d7c_symptoms_nervous = models.NullBooleanField(blank=True)
	d7c_hospitalization = models.NullBooleanField(blank=True)
	d7c_admission_date = models.CharField(max_length=15, blank=True)
	d7c_discharged_date = models.CharField(max_length=15, blank=True)
	d7c_hospital = models.CharField(max_length=25, blank=True)
	d7c_physician = models.CharField(max_length=25, blank=True)
	d7c_hospital_contact = models.CharField(max_length=25, blank=True)
	WARD_STATUS_LIST = (
						('', ''),
						('1','Emergency room only'),
						('2','One day care'),
						('3', 'General Ward'),
						('4','High care/intensive care'),
		)
	#d7c_ward = models.CharField(choices=WARD_STATUS_LIST, max_length=1, default="")
	d7c_ward = models.CharField(choices=WARD_STATUS_LIST, max_length=1, blank=True)
	d7c_additional_test = models.NullBooleanField(blank=True)
	d7c_blood_test = models.NullBooleanField(blank=True)
	d7c_blood_count = models.NullBooleanField(blank=True)
	d7c_crp = models.NullBooleanField(blank=True)
	d7c_procalcitonin = models.NullBooleanField(blank=True)
	d7c_blood_culture = models.NullBooleanField(blank=True)
	d7c_blood_culture_date = models.CharField(max_length=15, blank=True)
	d7c_blood_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_blood_microorganism = models.CharField(max_length=25, blank=True)
	d7c_typhoid = models.NullBooleanField(blank=True)
	d7c_dengue_ns_1 = models.NullBooleanField(blank=True)
	d7c_dengue = models.NullBooleanField(blank=True)
	d7c_nasopharyngeal = models.NullBooleanField(blank=True)
	d7c_urine = models.NullBooleanField(blank=True)
	d7c_urinalysis = models.NullBooleanField(blank=True)
	d7c_urinalysis_date = models.CharField(max_length=15, blank=True)
	d7c_urine_culture = models.NullBooleanField(blank=True)
	d7c_urine_date = models.CharField(max_length=15, blank=True)
	d7c_urine_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_urine_microorganism = models.CharField(max_length=25, blank=True)
	d7c_csf = models.NullBooleanField(blank=True)
	d7c_csf_date = models.CharField(max_length=15, blank=True)
	d7c_csf_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_csf_microorganism = models.CharField(max_length=25, blank=True)
	d7c_faecal_analysis = models.NullBooleanField(blank=True)
	d7c_faecal_analysis_date = models.CharField(max_length=15, blank=True)
	d7c_faecal_culture = models.NullBooleanField(blank=True)
	d7c_faecal_date = models.CharField(max_length=15, blank=True)
	d7c_faecal_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_faecal_microorganism = models.CharField(max_length=25, blank=True)
	d7c_chest_xray = models.NullBooleanField(blank=True)
	d7c_chest_xray_findings = models.CharField(max_length=25, blank=True)
	d7c_usg = models.NullBooleanField(blank=True)
	d7c_usg_type = models.CharField(max_length=25, blank=True)
	d7c_usg_date = models.CharField(max_length=15, blank=True)
	d7c_usg_findings = models.CharField(max_length=25, blank=True)
	d7c_mri = models.NullBooleanField(blank=True)
	d7c_mri_type = models.CharField(max_length=25, blank=True)
	d7c_mri_date = models.CharField(max_length=15, blank=True)
	d7c_mri_findings = models.CharField(max_length=25, blank=True)
	d7c_other_test = models.NullBooleanField(blank=True)
	d7c_other_test_type = models.CharField(max_length=25, blank=True)
	d7c_other_test_date = models.CharField(max_length=15, blank=True)
	d7c_other_test_findings = models.CharField(max_length=25, blank=True)
	d7c_medication = models.NullBooleanField(blank=True)
	d7c_med1_name = models.CharField(max_length=25, blank=True)
	d7c_med1_dosage = models.CharField(max_length=25, blank=True)
	d7c_med1_start_date = models.CharField(max_length=15, blank=True)
	d7c_med1_end_date = models.CharField(max_length=15, blank=True)
	d7c_med2_name = models.CharField(max_length=25, blank=True)
	d7c_med2_dosage = models.CharField(max_length=25, blank=True)
	d7c_med2_start_date = models.CharField(max_length=15, blank=True)
	d7c_med2_end_date = models.CharField(max_length=15, blank=True)
	d7c_med3_name = models.CharField(max_length=25, blank=True)
	d7c_med3_dosage = models.CharField(max_length=25, blank=True)
	d7c_med3_start_date = models.CharField(max_length=15, blank=True)
	d7c_med3_end_date = models.CharField(max_length=15, blank=True)
	d7c_med4_name = models.CharField(max_length=25, blank=True)
	d7c_med4_dosage = models.CharField(max_length=25, blank=True)
	d7c_med4_start_date = models.CharField(max_length=15, blank=True)
	d7c_med4_end_date = models.CharField(max_length=15, blank=True)
	d7c_med5_name = models.CharField(max_length=25, blank=True)
	d7c_med5_dosage = models.CharField(max_length=25, blank=True)
	d7c_med5_start_date = models.CharField(max_length=15, blank=True)
	d7c_med5_end_date = models.CharField(max_length=15, blank=True)
	d7_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D8PollutantExposure2(models.Model):
	d_form = models.ForeignKey(DInfant2, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d8m_charcoal = models.NullBooleanField(blank=True)
	d8m_kerosene = models.NullBooleanField(blank=True)
	d8m_wood = models.NullBooleanField(blank=True)
	d8m_gas = models.NullBooleanField(blank=True)
	d8m_electric = models.NullBooleanField(blank=True)
	d8m_other = models.NullBooleanField(blank=True)
	d8m_other_detail = models.CharField(max_length=25, blank=True)
	d8m_cooking_exhaust = models.NullBooleanField(blank=True)
	d8m_pesticide = models.NullBooleanField(blank=True)	
	GARBAGE_BURNING_STATUS_LIST = (
						('', ''),
						('0','No'),
						('1','Once per week or less'),
						('2', 'More than once per week but not daily'),
						('3','Daily'),
		)
	#d8m_garbage_burning = models.CharField(choices=GARBAGE_BURNING_STATUS_LIST, max_length=1, default="")
	d8m_garbage_burning = models.CharField(choices=GARBAGE_BURNING_STATUS_LIST, max_length=1, blank=True)
	d8m_pet = models.NullBooleanField(blank=True)
	d8m_pet_detail = models.CharField(max_length=25, blank=True)
	HOUSING_TYPE_LIST = (
						('', ''),
						('1','Landed House'),
						('2', 'Flat/Apartment'),
		)
	#d8m_housing_type = models.CharField(choices=HOUSING_TYPE_LIST, max_length=1, default="")
	d8m_housing_type = models.CharField(choices=HOUSING_TYPE_LIST, max_length=1, blank=True)
	LANDED_HOUSE_TYPE_LIST = (
						('', ''),
						('1','One story building'),
						('2', 'More than one story building'),
		)
	#d8m_landed_house_type = models.CharField(choices=LANDED_HOUSE_TYPE_LIST, max_length=1, default="")
	d8m_landed_house_type = models.CharField(choices=LANDED_HOUSE_TYPE_LIST, max_length=1, blank=True)
	d8m_apartment_level_number = models.CharField(max_length=15, blank=True)
	d8m_dampness_house = models.NullBooleanField(blank=True)
	d8m_ac = models.NullBooleanField(blank=True)
	d8m_fan = models.NullBooleanField(blank=True)
	d8m_air_filter = models.NullBooleanField(blank=True)
	d8m_staying_out_history = models.NullBooleanField(blank=True)
	##
	d8m_staying_out_1st_street = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_rt = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_rw = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_district = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_city = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_zipcode = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_duration = models.CharField(max_length=15, blank=True)

	d8m_staying_out_2nd_street = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_rt = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_rw = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_district = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_city = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_zipcode = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_duration = models.CharField(max_length=15, blank=True)
	d8_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"


###### End of Second Visit ######


###### Third Visit ######

class DInfant3(models.Model):
	participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
	date_admission = models.CharField(max_length=15, blank=True)
	child_id = models.CharField(max_length=12, blank=True)
	child_name = models.CharField(max_length=25, blank=True)
	interviewer_id = models.CharField(max_length=25, blank=True)
	date_interviewed = models.CharField(max_length=15, blank=True)
	data_entry_id = models.CharField(max_length=25, blank=True)
	date_data_entered = models.CharField(max_length=15, blank=True)
	data_checked_id = models.CharField(max_length=25, blank=True, null=True)
	date_data_checked = models.CharField(max_length=15, blank=True)
	is_save_all = models.NullBooleanField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", participant_name : "+unicode(self.participant.name )+ ", child_name : "+unicode(self.child_name )+ ", interviewer_id : "+unicode(self.interviewer_id )+ ", data_entry_id : "+unicode(self.data_entry_id )+ ", is_save_all : "+unicode(self.is_save_all )+ ", date_data_checked : "+ unicode(self.date_data_checked )+"]"

class D1InfantGrowth3(models.Model):
	d_form = models.ForeignKey(DInfant3, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d1c_ur_number = models.CharField(max_length=25, blank=True)
	d1c_first_name = models.CharField(max_length=25, blank=True)
	d1c_surname = models.CharField(max_length=25, blank=True)
	d1c_dob = models.CharField(max_length=15, blank=True)
	d1c_weight_1st = models.CharField(max_length=25, blank=True)
	d1c_weight_2nd = models.CharField(max_length=25, blank=True)
	d1c_length_1st = models.CharField(max_length=25, blank=True)
	d1c_length_2nd = models.CharField(max_length=25, blank=True)
	d1c_hc_1st = models.CharField(max_length=25, blank=True)
	d1c_hc_2nd = models.CharField(max_length=25, blank=True)
	d1c_chest_1st = models.CharField(max_length=25, blank=True)
	d1c_chest_2nd = models.CharField(max_length=25, blank=True)
	d1c_ac_1st = models.CharField(max_length=25, blank=True)
	d1c_ac_2nd = models.CharField(max_length=25, blank=True)
	d1c_vaccination_history = models.NullBooleanField(blank=True)
	d1c_bcg = models.NullBooleanField(blank=True)
	d1c_bcg_date = models.CharField(max_length=15, blank=True)
	d1c_hep_b = models.NullBooleanField(blank=True)
	d1c_hep_b_date = models.CharField(max_length=15, blank=True)
	d1c_dpt = models.NullBooleanField(blank=True)
	d1c_dpt_date = models.CharField(max_length=15, blank=True)
	d1c_ipv = models.NullBooleanField(blank=True)
	d1c_ipv_date = models.CharField(max_length=15, blank=True)
	d1c_opv = models.NullBooleanField(blank=True)
	d1c_opv_date = models.CharField(max_length=15, blank=True)
	d1c_hib = models.NullBooleanField(blank=True)
	d1c_hib_date = models.CharField(max_length=15, blank=True)
	d1c_rotavirus = models.NullBooleanField(blank=True)
	d1c_rotavirus_date = models.CharField(max_length=15, blank=True)
	d1c_pneumococcus = models.NullBooleanField(blank=True)
	d1c_pneumococcus_date = models.CharField(max_length=15, blank=True)
	d1c_influenza = models.NullBooleanField(blank=True)
	d1c_influenza_date = models.CharField(max_length=15, blank=True)
	d1_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D2InfantFeeding3(models.Model):
	d_form = models.ForeignKey(DInfant3, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d2c_breast_feeding_status = models.NullBooleanField(blank=True)
	d2c_supplementary_food = models.NullBooleanField(blank=True)
	d2c_infant_formula = models.NullBooleanField(blank=True)
	d2c_age_formula = models.CharField(max_length=15, blank=True)
	d2c_cows_milk_formula = models.NullBooleanField(blank=True)
	d2c_soy_formula = models.NullBooleanField(blank=True)
	d2c_hypo_allergen_formula = models.NullBooleanField(blank=True)
	d2c_hydrolized_formula = models.NullBooleanField(blank=True)
	d2c_amino_formula = models.NullBooleanField(blank=True)
	d2c_weaning_food = models.NullBooleanField(blank=True)
	d2c_age_weaning_food = models.CharField(max_length=15, blank=True)
	d2_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D3InfantCardiovascular3(models.Model):
	d_form = models.ForeignKey(DInfant3, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d3c_date_blood_pressure = models.CharField(max_length=15, blank=True)
	d3c_examiner_bp = models.CharField(max_length=25, blank=True)
	d3c_systolic_1st = models.CharField(max_length=25, blank=True)
	d3c_systolic_2nd = models.CharField(max_length=25, blank=True)
	d3c_systolic_3rd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_1st = models.CharField(max_length=25, blank=True)
	d3c_diastolic_2nd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_3rd = models.CharField(max_length=25, blank=True)
	d3c_pulse_1st = models.CharField(max_length=25, blank=True)
	d3c_pulse_2nd = models.CharField(max_length=25, blank=True)
	d3c_pulse_3rd = models.CharField(max_length=25, blank=True)
	d3c_date_echo = models.CharField(max_length=15, blank=True)
	d3c_examiner_echo = models.CharField(max_length=25, blank=True)
	CINELOOPS_OBTAINED_STATUS_LIST = (
						('', ''),
						('1', '4 chamber view'),
						('2', '5 chamber view'),
						('3', 'Parasternal long axis'),
						('4', 'Short axis view'),		
	)
	#d3c_cineloops = models.CharField(choices=CINELOOPS_OBTAINED_STATUS_LIST, max_length=1, default="")
	d3c_cineloops = models.CharField(choices=CINELOOPS_OBTAINED_STATUS_LIST, max_length=1, blank=True)
	d3c_heart_abnormality = models.NullBooleanField(blank=True)
	d3c_heart_abnormality_detail = models.CharField(max_length=25, blank=True)
	d3c_lvidd_1st = models.CharField(max_length=25, blank=True)
	d3c_lvidd_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvidd_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvids_1st = models.CharField(max_length=25, blank=True)
	d3c_lvids_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvids_3rd = models.CharField(max_length=25, blank=True)
	d3c_ivsd_1st = models.CharField(max_length=25, blank=True)
	d3c_ivsd_2nd = models.CharField(max_length=25, blank=True)
	d3c_ivsd_3rd = models.CharField(max_length=25, blank=True)
	d3c_ivss_1st = models.CharField(max_length=25, blank=True)
	d3c_ivss_2nd = models.CharField(max_length=25, blank=True)
	d3c_ivss_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_1st = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvpws_1st = models.CharField(max_length=25, blank=True)
	d3c_lvpws_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvpws_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvef_1st = models.CharField(max_length=25, blank=True)
	d3c_lvef_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvef_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvfs_1st = models.CharField(max_length=25, blank=True)
	d3c_lvfs_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvfs_3rd = models.CharField(max_length=25, blank=True)
	d3c_tvr_1st = models.CharField(max_length=25, blank=True)
	d3c_tvr_2nd = models.CharField(max_length=25, blank=True)
	d3c_tvr_3rd = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_1st = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_2nd = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_3rd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_1st = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_2nd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_3rd = models.CharField(max_length=25, blank=True)
	d3c_tapse_1st = models.CharField(max_length=25, blank=True)
	d3c_tapse_2nd = models.CharField(max_length=25, blank=True)
	d3c_tapse_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_e_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_a_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_s_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_e_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_a_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_s_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_e_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_a_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_s_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_e_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_a_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_s_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_date_vaskular = models.CharField(max_length=15, blank=True)
	d3c_examiner_vaskular = models.CharField(max_length=25, blank=True)
	d3c_cineloops_abdominal = models.NullBooleanField(blank=True)
	d3c_imt_1st = models.CharField(max_length=25, blank=True)
	d3c_imt_2nd = models.CharField(max_length=25, blank=True)
	d3c_imt_3rd = models.CharField(max_length=25, blank=True)
	d3c_sdimt_1st = models.CharField(max_length=25, blank=True)
	d3c_sdimt_2nd = models.CharField(max_length=25, blank=True)
	d3c_sdimt_3rd = models.CharField(max_length=25, blank=True)
	d3c_distension_1st = models.CharField(max_length=25, blank=True)
	d3c_distension_2nd = models.CharField(max_length=25, blank=True)
	d3c_distension_3rd = models.CharField(max_length=25, blank=True)
	d3c_diameter_1st = models.CharField(max_length=25, blank=True)
	d3c_diameter_2nd = models.CharField(max_length=25, blank=True)
	d3c_diameter_3rd = models.CharField(max_length=25, blank=True)
	d3_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"


class D4InfantLungFunction3(models.Model):
	d_form = models.ForeignKey(DInfant3, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d4c_date_lung = models.CharField(max_length=15, blank=True)
	d4c_examiner_lung = models.CharField(max_length=25, blank=True)
	d4c_resistance_1st = models.CharField(max_length=25, blank=True)
	d4c_resistance_2nd = models.CharField(max_length=25, blank=True)
	d4c_compliance_1st = models.CharField(max_length=25, blank=True)
	d4c_compliance_2nd = models.CharField(max_length=25, blank=True)
	d4c_time_constant_1st = models.CharField(max_length=25, blank=True)
	d4c_time_constant_2nd = models.CharField(max_length=25, blank=True)
	d4c_fvc_1st = models.CharField(max_length=25, blank=True)
	d4c_fvc_2nd = models.CharField(max_length=25, blank=True)
	d4c_fev1_1st = models.CharField(max_length=25, blank=True)
	d4c_fev1_2nd = models.CharField(max_length=25, blank=True)
	d4c_respiratory_symptom = models.NullBooleanField(blank=True)
	FREQUENCY_STATUS_LIST = (
						('', ''),
						('0', 'Not at all'),
						('1', 'Once'),
						('2', 'Twice'),
						('3', '3 or more'),
						('4', 'Every day'),		
	)
	#d4c_dry_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, default="")
	d4c_dry_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_phlegmy_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_runny_nose = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_stuffed_nose = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_wheeze = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_breath_shortness = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_rattly_chest = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_snoring = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_stridor = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D5InfantBiological3(models.Model):
	d_form = models.ForeignKey(DInfant3, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d5c_blood = models.NullBooleanField(blank=True)
	d5c_blood_date = models.CharField(max_length=15, blank=True)
	# d5c_buccal_swab = models.NullBooleanField(blank=True)
	# d5c_buccal_swab_date = models.CharField(max_length=15, blank=True)
	d5c_hair_1 = models.NullBooleanField(blank=True)
	d5c_hair_1_date = models.CharField(max_length=15, blank=True)
	d5c_hair_6 = models.NullBooleanField(blank=True)
	d5c_hair_6_date = models.CharField(max_length=15, blank=True)
	d5c_nail_1 = models.NullBooleanField(blank=True)
	d5c_nail_1_date = models.CharField(max_length=15, blank=True)
	d5c_nail_6 = models.NullBooleanField(blank=True)
	d5c_nail_6_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_2 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_2_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_4 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_4_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_6 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_6_date = models.CharField(max_length=15, blank=True)
	d5_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D6CurrentSmoking3(models.Model):
	d_form = models.ForeignKey(DInfant3, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	SMOKING_STATUS_LIST = (
					('', ''),
					('1', 'Smoker'),
					('2', 'Ex-smoker'),
					('0', 'Never smoke'),
		)
	SMOKING_FREQUENCY_LIST = (
						('', ''),
						('1','Daily'),
						('2','Weekly'),
						('3', 'Monthly'),
						('0','Never'),
		)
	#d6m_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, default="")
	d6m_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, blank=True)
	d6m_quitting_smoke = models.NullBooleanField(blank=True)
	d6m_quitting_duration = models.CharField(max_length=15, blank=True)
	d6m_cigar_number = models.CharField(max_length=15, blank=True)
	d6m_cigar_type = models.NullBooleanField(blank=True)
	d6m_smoking_household = models.NullBooleanField(blank=True)
	d6m_household_number = models.CharField(max_length=15, blank=True)
	d6m_household_cigar_number = models.CharField(max_length=15, blank=True)
	d6m_household_presence = models.NullBooleanField(blank=True)

	d6f_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, blank=True)
	d6f_quitting_duration = models.CharField(max_length=15, blank=True)
	d6f_cigar_number = models.CharField(max_length=15, blank=True)
	d6f_cigar_type = models.NullBooleanField(blank=True)
	d6f_smoking_frequency = models.CharField(choices=SMOKING_FREQUENCY_LIST, max_length=1, blank=True)
	d6f_smoking_presence = models.NullBooleanField(blank=True)
	d6_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D7Infection3(models.Model):
	d_form = models.ForeignKey(DInfant3, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d7c_infection = models.NullBooleanField(blank=True)
	d7c_infection_upper_respi = models.NullBooleanField(blank=True)
	d7c_infection_lower_respi = models.NullBooleanField(blank=True)
	d7c_infection_gastro = models.NullBooleanField(blank=True)
	d7c_infection_urinary = models.NullBooleanField(blank=True)
	d7c_infection_cns = models.NullBooleanField(blank=True)
	d7c_infection_sepsis = models.NullBooleanField(blank=True)
	d7c_infection_dengue = models.NullBooleanField(blank=True)
	d7c_infection_others = models.NullBooleanField(blank=True)
	d7c_infection_others_detail = models.CharField(max_length=25, blank=True)
	d7c_infection_unknown = models.NullBooleanField(blank=True)
	d7c_physician_clinic = models.CharField(max_length=25, blank=True)
	#d7c_contact = models.CharField(max_length=25, blank=True)
	d7c_infection_symptoms = models.NullBooleanField(blank=True)
	d7c_symptoms_respi = models.NullBooleanField(blank=True)
	d7c_symptoms_gastro = models.NullBooleanField(blank=True)
	d7c_symptoms_skin = models.NullBooleanField(blank=True)
	d7c_symptoms_nervous = models.NullBooleanField(blank=True)
	d7c_hospitalization = models.NullBooleanField(blank=True)
	d7c_admission_date = models.CharField(max_length=15, blank=True)
	d7c_discharged_date = models.CharField(max_length=15, blank=True)
	d7c_hospital = models.CharField(max_length=25, blank=True)
	d7c_physician = models.CharField(max_length=25, blank=True)
	d7c_hospital_contact = models.CharField(max_length=25, blank=True)
	WARD_STATUS_LIST = (
						('', ''),
						('1','Emergency room only'),
						('2','One day care'),
						('3', 'General Ward'),
						('4','High care/intensive care'),
		)
	#d7c_ward = models.CharField(choices=WARD_STATUS_LIST, max_length=1, default="")
	d7c_ward = models.CharField(choices=WARD_STATUS_LIST, max_length=1, blank=True)
	d7c_additional_test = models.NullBooleanField(blank=True)
	d7c_blood_test = models.NullBooleanField(blank=True)
	d7c_blood_count = models.NullBooleanField(blank=True)
	d7c_crp = models.NullBooleanField(blank=True)
	d7c_procalcitonin = models.NullBooleanField(blank=True)
	d7c_blood_culture = models.NullBooleanField(blank=True)
	d7c_blood_culture_date = models.CharField(max_length=15, blank=True)
	d7c_blood_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_blood_microorganism = models.CharField(max_length=25, blank=True)
	d7c_typhoid = models.NullBooleanField(blank=True)
	d7c_dengue_ns_1 = models.NullBooleanField(blank=True)
	d7c_dengue = models.NullBooleanField(blank=True)
	d7c_nasopharyngeal = models.NullBooleanField(blank=True)
	d7c_urine = models.NullBooleanField(blank=True)
	d7c_urinalysis = models.NullBooleanField(blank=True)
	d7c_urinalysis_date = models.CharField(max_length=15, blank=True)
	d7c_urine_culture = models.NullBooleanField(blank=True)
	d7c_urine_date = models.CharField(max_length=15, blank=True)
	d7c_urine_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_urine_microorganism = models.CharField(max_length=25, blank=True)
	d7c_csf = models.NullBooleanField(blank=True)
	d7c_csf_date = models.CharField(max_length=15, blank=True)
	d7c_csf_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_csf_microorganism = models.CharField(max_length=25, blank=True)
	d7c_faecal_analysis = models.NullBooleanField(blank=True)
	d7c_faecal_analysis_date = models.CharField(max_length=15, blank=True)
	d7c_faecal_culture = models.NullBooleanField(blank=True)
	d7c_faecal_date = models.CharField(max_length=15, blank=True)
	d7c_faecal_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_faecal_microorganism = models.CharField(max_length=25, blank=True)
	d7c_chest_xray = models.NullBooleanField(blank=True)
	d7c_chest_xray_findings = models.CharField(max_length=25, blank=True)
	d7c_usg = models.NullBooleanField(blank=True)
	d7c_usg_type = models.CharField(max_length=25, blank=True)
	d7c_usg_date = models.CharField(max_length=15, blank=True)
	d7c_usg_findings = models.CharField(max_length=25, blank=True)
	d7c_mri = models.NullBooleanField(blank=True)
	d7c_mri_type = models.CharField(max_length=25, blank=True)
	d7c_mri_date = models.CharField(max_length=15, blank=True)
	d7c_mri_findings = models.CharField(max_length=25, blank=True)
	d7c_other_test = models.NullBooleanField(blank=True)
	d7c_other_test_type = models.CharField(max_length=25, blank=True)
	d7c_other_test_date = models.CharField(max_length=15, blank=True)
	d7c_other_test_findings = models.CharField(max_length=25, blank=True)
	d7c_medication = models.NullBooleanField(blank=True)
	d7c_med1_name = models.CharField(max_length=25, blank=True)
	d7c_med1_dosage = models.CharField(max_length=25, blank=True)
	d7c_med1_start_date = models.CharField(max_length=15, blank=True)
	d7c_med1_end_date = models.CharField(max_length=15, blank=True)
	d7c_med2_name = models.CharField(max_length=25, blank=True)
	d7c_med2_dosage = models.CharField(max_length=25, blank=True)
	d7c_med2_start_date = models.CharField(max_length=15, blank=True)
	d7c_med2_end_date = models.CharField(max_length=15, blank=True)
	d7c_med3_name = models.CharField(max_length=25, blank=True)
	d7c_med3_dosage = models.CharField(max_length=25, blank=True)
	d7c_med3_start_date = models.CharField(max_length=15, blank=True)
	d7c_med3_end_date = models.CharField(max_length=15, blank=True)
	d7c_med4_name = models.CharField(max_length=25, blank=True)
	d7c_med4_dosage = models.CharField(max_length=25, blank=True)
	d7c_med4_start_date = models.CharField(max_length=15, blank=True)
	d7c_med4_end_date = models.CharField(max_length=15, blank=True)
	d7c_med5_name = models.CharField(max_length=25, blank=True)
	d7c_med5_dosage = models.CharField(max_length=25, blank=True)
	d7c_med5_start_date = models.CharField(max_length=15, blank=True)
	d7c_med5_end_date = models.CharField(max_length=15, blank=True)
	d7_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D8PollutantExposure3(models.Model):
	d_form = models.ForeignKey(DInfant3, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d8m_charcoal = models.NullBooleanField(blank=True)
	d8m_kerosene = models.NullBooleanField(blank=True)
	d8m_wood = models.NullBooleanField(blank=True)
	d8m_gas = models.NullBooleanField(blank=True)
	d8m_electric = models.NullBooleanField(blank=True)
	d8m_other = models.NullBooleanField(blank=True)
	d8m_other_detail = models.CharField(max_length=25, blank=True)
	d8m_cooking_exhaust = models.NullBooleanField(blank=True)
	d8m_pesticide = models.NullBooleanField(blank=True)	
	GARBAGE_BURNING_STATUS_LIST = (
						('', ''),
						('0','No'),
						('1','Once per week or less'),
						('2', 'More than once per week but not daily'),
						('3','Daily'),
		)
	#d8m_garbage_burning = models.CharField(choices=GARBAGE_BURNING_STATUS_LIST, max_length=1, default="")
	d8m_garbage_burning = models.CharField(choices=GARBAGE_BURNING_STATUS_LIST, max_length=1, blank=True)
	d8m_pet = models.NullBooleanField(blank=True)
	d8m_pet_detail = models.CharField(max_length=25, blank=True)
	HOUSING_TYPE_LIST = (
						('', ''),
						('1','Landed House'),
						('2', 'Flat/Apartment'),
		)
	#d8m_housing_type = models.CharField(choices=HOUSING_TYPE_LIST, max_length=1, default="")
	d8m_housing_type = models.CharField(choices=HOUSING_TYPE_LIST, max_length=1, blank=True)
	LANDED_HOUSE_TYPE_LIST = (
						('', ''),
						('1','One story building'),
						('2', 'More than one story building'),
		)
	#d8m_landed_house_type = models.CharField(choices=LANDED_HOUSE_TYPE_LIST, max_length=1, default="")
	d8m_landed_house_type = models.CharField(choices=LANDED_HOUSE_TYPE_LIST, max_length=1, blank=True)
	d8m_apartment_level_number = models.CharField(max_length=15, blank=True)
	d8m_dampness_house = models.NullBooleanField(blank=True)
	d8m_ac = models.NullBooleanField(blank=True)
	d8m_fan = models.NullBooleanField(blank=True)
	d8m_air_filter = models.NullBooleanField(blank=True)
	d8m_staying_out_history = models.NullBooleanField(blank=True)
	##
	d8m_staying_out_1st_street = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_rt = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_rw = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_district = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_city = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_zipcode = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_duration = models.CharField(max_length=15, blank=True)

	d8m_staying_out_2nd_street = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_rt = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_rw = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_district = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_city = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_zipcode = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_duration = models.CharField(max_length=15, blank=True)
	d8_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"


###### End of Third Visit ######


###### Fourth Visit ######

class DInfant4(models.Model):
	participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
	date_admission = models.CharField(max_length=15, blank=True)
	child_id = models.CharField(max_length=12, blank=True)
	child_name = models.CharField(max_length=25, blank=True)
	interviewer_id = models.CharField(max_length=25, blank=True)
	date_interviewed = models.CharField(max_length=15, blank=True)
	data_entry_id = models.CharField(max_length=25, blank=True)
	date_data_entered = models.CharField(max_length=15, blank=True)
	data_checked_id = models.CharField(max_length=25, blank=True, null=True)
	date_data_checked = models.CharField(max_length=15, blank=True)
	is_save_all = models.NullBooleanField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", participant_name : "+unicode(self.participant.name )+ ", child_name : "+unicode(self.child_name )+ ", interviewer_id : "+unicode(self.interviewer_id )+ ", data_entry_id : "+unicode(self.data_entry_id )+ ", is_save_all : "+unicode(self.is_save_all )+ ", date_data_checked : "+ unicode(self.date_data_checked )+"]"

class D1InfantGrowth4(models.Model):
	d_form = models.ForeignKey(DInfant4, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d1c_ur_number = models.CharField(max_length=25, blank=True)
	d1c_first_name = models.CharField(max_length=25, blank=True)
	d1c_surname = models.CharField(max_length=25, blank=True)
	d1c_dob = models.CharField(max_length=15, blank=True)
	d1c_weight_1st = models.CharField(max_length=25, blank=True)
	d1c_weight_2nd = models.CharField(max_length=25, blank=True)
	d1c_length_1st = models.CharField(max_length=25, blank=True)
	d1c_length_2nd = models.CharField(max_length=25, blank=True)
	d1c_hc_1st = models.CharField(max_length=25, blank=True)
	d1c_hc_2nd = models.CharField(max_length=25, blank=True)
	d1c_chest_1st = models.CharField(max_length=25, blank=True)
	d1c_chest_2nd = models.CharField(max_length=25, blank=True)
	d1c_ac_1st = models.CharField(max_length=25, blank=True)
	d1c_ac_2nd = models.CharField(max_length=25, blank=True)
	d1c_vaccination_history = models.NullBooleanField(blank=True)
	d1c_bcg = models.NullBooleanField(blank=True)
	d1c_bcg_date = models.CharField(max_length=15, blank=True)
	d1c_hep_b = models.NullBooleanField(blank=True)
	d1c_hep_b_date = models.CharField(max_length=15, blank=True)
	d1c_dpt = models.NullBooleanField(blank=True)
	d1c_dpt_date = models.CharField(max_length=15, blank=True)
	d1c_ipv = models.NullBooleanField(blank=True)
	d1c_ipv_date = models.CharField(max_length=15, blank=True)
	d1c_opv = models.NullBooleanField(blank=True)
	d1c_opv_date = models.CharField(max_length=15, blank=True)
	d1c_hib = models.NullBooleanField(blank=True)
	d1c_hib_date = models.CharField(max_length=15, blank=True)
	d1c_rotavirus = models.NullBooleanField(blank=True)
	d1c_rotavirus_date = models.CharField(max_length=15, blank=True)
	d1c_pneumococcus = models.NullBooleanField(blank=True)
	d1c_pneumococcus_date = models.CharField(max_length=15, blank=True)
	d1c_influenza = models.NullBooleanField(blank=True)
	d1c_influenza_date = models.CharField(max_length=15, blank=True)
	d1_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D2InfantFeeding4(models.Model):
	d_form = models.ForeignKey(DInfant4, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d2c_breast_feeding_status = models.NullBooleanField(blank=True)
	d2c_supplementary_food = models.NullBooleanField(blank=True)
	d2c_infant_formula = models.NullBooleanField(blank=True)
	d2c_age_formula = models.CharField(max_length=15, blank=True)
	d2c_cows_milk_formula = models.NullBooleanField(blank=True)
	d2c_soy_formula = models.NullBooleanField(blank=True)
	d2c_hypo_allergen_formula = models.NullBooleanField(blank=True)
	d2c_hydrolized_formula = models.NullBooleanField(blank=True)
	d2c_amino_formula = models.NullBooleanField(blank=True)
	d2c_weaning_food = models.NullBooleanField(blank=True)
	d2c_age_weaning_food = models.CharField(max_length=15, blank=True)
	d2_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D3InfantCardiovascular4(models.Model):
	d_form = models.ForeignKey(DInfant4, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d3c_date_blood_pressure = models.CharField(max_length=15, blank=True)
	d3c_examiner_bp = models.CharField(max_length=25, blank=True)
	d3c_systolic_1st = models.CharField(max_length=25, blank=True)
	d3c_systolic_2nd = models.CharField(max_length=25, blank=True)
	d3c_systolic_3rd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_1st = models.CharField(max_length=25, blank=True)
	d3c_diastolic_2nd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_3rd = models.CharField(max_length=25, blank=True)
	d3c_pulse_1st = models.CharField(max_length=25, blank=True)
	d3c_pulse_2nd = models.CharField(max_length=25, blank=True)
	d3c_pulse_3rd = models.CharField(max_length=25, blank=True)
	d3c_date_echo = models.CharField(max_length=15, blank=True)
	d3c_examiner_echo = models.CharField(max_length=25, blank=True)
	CINELOOPS_OBTAINED_STATUS_LIST = (
						('', ''),
						('1', '4 chamber view'),
						('2', '5 chamber view'),
						('3', 'Parasternal long axis'),
						('4', 'Short axis view'),		
	)
	#d3c_cineloops = models.CharField(choices=CINELOOPS_OBTAINED_STATUS_LIST, max_length=1, default="")
	d3c_cineloops = models.CharField(choices=CINELOOPS_OBTAINED_STATUS_LIST, max_length=1, blank=True)
	d3c_heart_abnormality = models.NullBooleanField(blank=True)
	d3c_heart_abnormality_detail = models.CharField(max_length=25, blank=True)
	d3c_lvidd_1st = models.CharField(max_length=25, blank=True)
	d3c_lvidd_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvidd_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvids_1st = models.CharField(max_length=25, blank=True)
	d3c_lvids_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvids_3rd = models.CharField(max_length=25, blank=True)
	d3c_ivsd_1st = models.CharField(max_length=25, blank=True)
	d3c_ivsd_2nd = models.CharField(max_length=25, blank=True)
	d3c_ivsd_3rd = models.CharField(max_length=25, blank=True)
	d3c_ivss_1st = models.CharField(max_length=25, blank=True)
	d3c_ivss_2nd = models.CharField(max_length=25, blank=True)
	d3c_ivss_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_1st = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvpwd_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvpws_1st = models.CharField(max_length=25, blank=True)
	d3c_lvpws_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvpws_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvef_1st = models.CharField(max_length=25, blank=True)
	d3c_lvef_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvef_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvfs_1st = models.CharField(max_length=25, blank=True)
	d3c_lvfs_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvfs_3rd = models.CharField(max_length=25, blank=True)
	d3c_tvr_1st = models.CharField(max_length=25, blank=True)
	d3c_tvr_2nd = models.CharField(max_length=25, blank=True)
	d3c_tvr_3rd = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_1st = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_2nd = models.CharField(max_length=25, blank=True)
	d3c_systolic_lv_3rd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_1st = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_2nd = models.CharField(max_length=25, blank=True)
	d3c_diastolic_lv_3rd = models.CharField(max_length=25, blank=True)
	d3c_tapse_1st = models.CharField(max_length=25, blank=True)
	d3c_tapse_2nd = models.CharField(max_length=25, blank=True)
	d3c_tapse_3rd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_e_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_a_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvwall_s_1st = models.CharField(max_length=25, blank=True)
	d3c_lvwall_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_e_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_a_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_s_1st = models.CharField(max_length=25, blank=True)
	d3c_lvseptal_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_e_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_a_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvwall_s_1st = models.CharField(max_length=25, blank=True)
	d3c_rvwall_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_e_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_e_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_a_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_a_2nd = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_s_1st = models.CharField(max_length=25, blank=True)
	d3c_rvseptal_s_2nd = models.CharField(max_length=25, blank=True)
	d3c_date_vaskular = models.CharField(max_length=15, blank=True)
	d3c_examiner_vaskular = models.CharField(max_length=25, blank=True)
	d3c_cineloops_abdominal = models.NullBooleanField(blank=True)
	d3c_imt_1st = models.CharField(max_length=25, blank=True)
	d3c_imt_2nd = models.CharField(max_length=25, blank=True)
	d3c_imt_3rd = models.CharField(max_length=25, blank=True)
	d3c_sdimt_1st = models.CharField(max_length=25, blank=True)
	d3c_sdimt_2nd = models.CharField(max_length=25, blank=True)
	d3c_sdimt_3rd = models.CharField(max_length=25, blank=True)
	d3c_distension_1st = models.CharField(max_length=25, blank=True)
	d3c_distension_2nd = models.CharField(max_length=25, blank=True)
	d3c_distension_3rd = models.CharField(max_length=25, blank=True)
	d3c_diameter_1st = models.CharField(max_length=25, blank=True)
	d3c_diameter_2nd = models.CharField(max_length=25, blank=True)
	d3c_diameter_3rd = models.CharField(max_length=25, blank=True)
	d3_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"


class D4InfantLungFunction4(models.Model):
	d_form = models.ForeignKey(DInfant4, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d4c_date_lung = models.CharField(max_length=15, blank=True)
	d4c_examiner_lung = models.CharField(max_length=25, blank=True)
	d4c_resistance_1st = models.CharField(max_length=25, blank=True)
	d4c_resistance_2nd = models.CharField(max_length=25, blank=True)
	d4c_compliance_1st = models.CharField(max_length=25, blank=True)
	d4c_compliance_2nd = models.CharField(max_length=25, blank=True)
	d4c_time_constant_1st = models.CharField(max_length=25, blank=True)
	d4c_time_constant_2nd = models.CharField(max_length=25, blank=True)
	d4c_fvc_1st = models.CharField(max_length=25, blank=True)
	d4c_fvc_2nd = models.CharField(max_length=25, blank=True)
	d4c_fev1_1st = models.CharField(max_length=25, blank=True)
	d4c_fev1_2nd = models.CharField(max_length=25, blank=True)
	d4c_respiratory_symptom = models.NullBooleanField(blank=True)
	FREQUENCY_STATUS_LIST = (
						('', ''),
						('0', 'Not at all'),
						('1', 'Once'),
						('2', 'Twice'),
						('3', '3 or more'),
						('4', 'Every day'),		
	)
	#d4c_dry_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, default="")
	d4c_dry_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_phlegmy_cough = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_runny_nose = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_stuffed_nose = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_wheeze = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_breath_shortness = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_rattly_chest = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_snoring = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4c_stridor = models.CharField(choices=FREQUENCY_STATUS_LIST, max_length=1, blank=True)
	d4_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D5InfantBiological4(models.Model):
	d_form = models.ForeignKey(DInfant4, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d5c_blood = models.NullBooleanField(blank=True)
	d5c_blood_date = models.CharField(max_length=15, blank=True)
	# d5c_buccal_swab = models.NullBooleanField(blank=True)
	# d5c_buccal_swab_date = models.CharField(max_length=15, blank=True)
	d5c_hair_1 = models.NullBooleanField(blank=True)
	d5c_hair_1_date = models.CharField(max_length=15, blank=True)
	d5c_hair_6 = models.NullBooleanField(blank=True)
	d5c_hair_6_date = models.CharField(max_length=15, blank=True)
	d5c_nail_1 = models.NullBooleanField(blank=True)
	d5c_nail_1_date = models.CharField(max_length=15, blank=True)
	d5c_nail_6 = models.NullBooleanField(blank=True)
	d5c_nail_6_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_2 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_2_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_4 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_4_date = models.CharField(max_length=15, blank=True)
	d5c_nasopharyngeal_6 = models.NullBooleanField(blank=True)
	d5c_nasopharyngeal_6_date = models.CharField(max_length=15, blank=True)
	d5_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D6CurrentSmoking4(models.Model):
	d_form = models.ForeignKey(DInfant4, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	SMOKING_STATUS_LIST = (
					('', ''),
					('1', 'Smoker'),
					('2', 'Ex-smoker'),
					('0', 'Never smoke'),
		)
	SMOKING_FREQUENCY_LIST = (
						('', ''),
						('1','Daily'),
						('2','Weekly'),
						('3', 'Monthly'),
						('0','Never'),
		)
	#d6m_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, default="")
	d6m_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, blank=True)
	d6m_quitting_smoke = models.NullBooleanField(blank=True)
	d6m_quitting_duration = models.CharField(max_length=15, blank=True)
	d6m_cigar_number = models.CharField(max_length=15, blank=True)
	d6m_cigar_type = models.NullBooleanField(blank=True)
	d6m_smoking_household = models.NullBooleanField(blank=True)
	d6m_household_number = models.CharField(max_length=15, blank=True)
	d6m_household_cigar_number = models.CharField(max_length=15, blank=True)
	d6m_household_presence = models.NullBooleanField(blank=True)

	d6f_smoking_status = models.CharField(choices=SMOKING_STATUS_LIST, max_length=1, blank=True)
	d6f_quitting_duration = models.CharField(max_length=15, blank=True)
	d6f_cigar_number = models.CharField(max_length=15, blank=True)
	d6f_cigar_type = models.NullBooleanField(blank=True)
	d6f_smoking_frequency = models.CharField(choices=SMOKING_FREQUENCY_LIST, max_length=1, blank=True)
	d6f_smoking_presence = models.NullBooleanField(blank=True)
	d6_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D7Infection4(models.Model):
	d_form = models.ForeignKey(DInfant4, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d7c_infection = models.NullBooleanField(blank=True)
	d7c_infection_upper_respi = models.NullBooleanField(blank=True)
	d7c_infection_lower_respi = models.NullBooleanField(blank=True)
	d7c_infection_gastro = models.NullBooleanField(blank=True)
	d7c_infection_urinary = models.NullBooleanField(blank=True)
	d7c_infection_cns = models.NullBooleanField(blank=True)
	d7c_infection_sepsis = models.NullBooleanField(blank=True)
	d7c_infection_dengue = models.NullBooleanField(blank=True)
	d7c_infection_others = models.NullBooleanField(blank=True)
	d7c_infection_others_detail = models.CharField(max_length=25, blank=True)
	d7c_infection_unknown = models.NullBooleanField(blank=True)
	d7c_physician_clinic = models.CharField(max_length=25, blank=True)
	#d7c_contact = models.CharField(max_length=25, blank=True)
	d7c_infection_symptoms = models.NullBooleanField(blank=True)
	d7c_symptoms_respi = models.NullBooleanField(blank=True)
	d7c_symptoms_gastro = models.NullBooleanField(blank=True)
	d7c_symptoms_skin = models.NullBooleanField(blank=True)
	d7c_symptoms_nervous = models.NullBooleanField(blank=True)
	d7c_hospitalization = models.NullBooleanField(blank=True)
	d7c_admission_date = models.CharField(max_length=15, blank=True)
	d7c_discharged_date = models.CharField(max_length=15, blank=True)
	d7c_hospital = models.CharField(max_length=25, blank=True)
	d7c_physician = models.CharField(max_length=25, blank=True)
	d7c_hospital_contact = models.CharField(max_length=25, blank=True)
	WARD_STATUS_LIST = (
						('', ''),
						('1','Emergency room only'),
						('2','One day care'),
						('3', 'General Ward'),
						('4','High care/intensive care'),
		)
	#d7c_ward = models.CharField(choices=WARD_STATUS_LIST, max_length=1, default="")
	d7c_ward = models.CharField(choices=WARD_STATUS_LIST, max_length=1, blank=True)
	d7c_additional_test = models.NullBooleanField(blank=True)
	d7c_blood_test = models.NullBooleanField(blank=True)
	d7c_blood_count = models.NullBooleanField(blank=True)
	d7c_crp = models.NullBooleanField(blank=True)
	d7c_procalcitonin = models.NullBooleanField(blank=True)
	d7c_blood_culture = models.NullBooleanField(blank=True)
	d7c_blood_culture_date = models.CharField(max_length=15, blank=True)
	d7c_blood_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_blood_microorganism = models.CharField(max_length=25, blank=True)
	d7c_typhoid = models.NullBooleanField(blank=True)
	d7c_dengue_ns_1 = models.NullBooleanField(blank=True)
	d7c_dengue = models.NullBooleanField(blank=True)
	d7c_nasopharyngeal = models.NullBooleanField(blank=True)
	d7c_urine = models.NullBooleanField(blank=True)
	d7c_urinalysis = models.NullBooleanField(blank=True)
	d7c_urinalysis_date = models.CharField(max_length=15, blank=True)
	d7c_urine_culture = models.NullBooleanField(blank=True)
	d7c_urine_date = models.CharField(max_length=15, blank=True)
	d7c_urine_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_urine_microorganism = models.CharField(max_length=25, blank=True)
	d7c_csf = models.NullBooleanField(blank=True)
	d7c_csf_date = models.CharField(max_length=15, blank=True)
	d7c_csf_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_csf_microorganism = models.CharField(max_length=25, blank=True)
	d7c_faecal_analysis = models.NullBooleanField(blank=True)
	d7c_faecal_analysis_date = models.CharField(max_length=15, blank=True)
	d7c_faecal_culture = models.NullBooleanField(blank=True)
	d7c_faecal_date = models.CharField(max_length=15, blank=True)
	d7c_faecal_microorganism_exist = models.NullBooleanField(blank=True)
	d7c_faecal_microorganism = models.CharField(max_length=25, blank=True)
	d7c_chest_xray = models.NullBooleanField(blank=True)
	d7c_chest_xray_findings = models.CharField(max_length=25, blank=True)
	d7c_usg = models.NullBooleanField(blank=True)
	d7c_usg_type = models.CharField(max_length=25, blank=True)
	d7c_usg_date = models.CharField(max_length=15, blank=True)
	d7c_usg_findings = models.CharField(max_length=25, blank=True)
	d7c_mri = models.NullBooleanField(blank=True)
	d7c_mri_type = models.CharField(max_length=25, blank=True)
	d7c_mri_date = models.CharField(max_length=15, blank=True)
	d7c_mri_findings = models.CharField(max_length=25, blank=True)
	d7c_other_test = models.NullBooleanField(blank=True)
	d7c_other_test_type = models.CharField(max_length=25, blank=True)
	d7c_other_test_date = models.CharField(max_length=15, blank=True)
	d7c_other_test_findings = models.CharField(max_length=25, blank=True)
	d7c_medication = models.NullBooleanField(blank=True)
	d7c_med1_name = models.CharField(max_length=25, blank=True)
	d7c_med1_dosage = models.CharField(max_length=25, blank=True)
	d7c_med1_start_date = models.CharField(max_length=15, blank=True)
	d7c_med1_end_date = models.CharField(max_length=15, blank=True)
	d7c_med2_name = models.CharField(max_length=25, blank=True)
	d7c_med2_dosage = models.CharField(max_length=25, blank=True)
	d7c_med2_start_date = models.CharField(max_length=15, blank=True)
	d7c_med2_end_date = models.CharField(max_length=15, blank=True)
	d7c_med3_name = models.CharField(max_length=25, blank=True)
	d7c_med3_dosage = models.CharField(max_length=25, blank=True)
	d7c_med3_start_date = models.CharField(max_length=15, blank=True)
	d7c_med3_end_date = models.CharField(max_length=15, blank=True)
	d7c_med4_name = models.CharField(max_length=25, blank=True)
	d7c_med4_dosage = models.CharField(max_length=25, blank=True)
	d7c_med4_start_date = models.CharField(max_length=15, blank=True)
	d7c_med4_end_date = models.CharField(max_length=15, blank=True)
	d7c_med5_name = models.CharField(max_length=25, blank=True)
	d7c_med5_dosage = models.CharField(max_length=25, blank=True)
	d7c_med5_start_date = models.CharField(max_length=15, blank=True)
	d7c_med5_end_date = models.CharField(max_length=15, blank=True)
	d7_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"

class D8PollutantExposure4(models.Model):
	d_form = models.ForeignKey(DInfant4, on_delete=models.PROTECT)
	created_by = models.CharField(max_length=25, blank=True)
	updated_by = models.CharField(max_length=25, blank=True)
	created_time = models.CharField(max_length=28, blank=True)
	updated_time = models.CharField(max_length=28, blank=True)
	participant_id = models.CharField(max_length=10, blank=True)
	child_id = models.CharField(max_length=12, blank=True)

	d8m_charcoal = models.NullBooleanField(blank=True)
	d8m_kerosene = models.NullBooleanField(blank=True)
	d8m_wood = models.NullBooleanField(blank=True)
	d8m_gas = models.NullBooleanField(blank=True)
	d8m_electric = models.NullBooleanField(blank=True)
	d8m_other = models.NullBooleanField(blank=True)
	d8m_other_detail = models.CharField(max_length=25, blank=True)
	d8m_cooking_exhaust = models.NullBooleanField(blank=True)
	d8m_pesticide = models.NullBooleanField(blank=True)	
	GARBAGE_BURNING_STATUS_LIST = (
						('', ''),
						('0','No'),
						('1','Once per week or less'),
						('2', 'More than once per week but not daily'),
						('3','Daily'),
		)
	#d8m_garbage_burning = models.CharField(choices=GARBAGE_BURNING_STATUS_LIST, max_length=1, default="")
	d8m_garbage_burning = models.CharField(choices=GARBAGE_BURNING_STATUS_LIST, max_length=1, blank=True)
	d8m_pet = models.NullBooleanField(blank=True)
	d8m_pet_detail = models.CharField(max_length=25, blank=True)
	HOUSING_TYPE_LIST = (
						('', ''),
						('1','Landed House'),
						('2', 'Flat/Apartment'),
		)
	#d8m_housing_type = models.CharField(choices=HOUSING_TYPE_LIST, max_length=1, default="")
	d8m_housing_type = models.CharField(choices=HOUSING_TYPE_LIST, max_length=1, blank=True)
	LANDED_HOUSE_TYPE_LIST = (
						('', ''),
						('1','One story building'),
						('2', 'More than one story building'),
		)
	#d8m_landed_house_type = models.CharField(choices=LANDED_HOUSE_TYPE_LIST, max_length=1, default="")
	d8m_landed_house_type = models.CharField(choices=LANDED_HOUSE_TYPE_LIST, max_length=1, blank=True)
	d8m_apartment_level_number = models.CharField(max_length=15, blank=True)
	d8m_dampness_house = models.NullBooleanField(blank=True)
	d8m_ac = models.NullBooleanField(blank=True)
	d8m_fan = models.NullBooleanField(blank=True)
	d8m_air_filter = models.NullBooleanField(blank=True)
	d8m_staying_out_history = models.NullBooleanField(blank=True)
	##
	d8m_staying_out_1st_street = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_rt = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_rw = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_district = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_city = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_zipcode = models.CharField(max_length=25, blank=True)
	d8m_staying_out_1st_duration = models.CharField(max_length=15, blank=True)

	d8m_staying_out_2nd_street = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_rt = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_rw = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_district = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_city = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_zipcode = models.CharField(max_length=25, blank=True)
	d8m_staying_out_2nd_duration = models.CharField(max_length=15, blank=True)
	d8_notes = models.TextField(blank=True)
	def __str__(self):
		return "[participant_id : " + unicode(self.participant_id)+ ", child_id : "+unicode(self.child_id )+"]"


###### End of Fourth Visit ######