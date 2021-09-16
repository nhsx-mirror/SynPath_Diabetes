import datetime     # enables the start time elements in date and time format

# All the interactions at the gp
# "measure_hba1c",
# "medication_change1",
# "medication_change2",
# "insulin_prescription",
# "highrisk_management",
# "exercise_prescription",
# "prediabetes_diagnosis",
# "t2dm_diagnosis",
# "glucose_management",
# "annual_health_check",
# "hypertension_management",
# "complications_id_mant",
# "glucose_clinic",

# This is gp 0 (the first gp clinic, where patients are referred to community and hospital 1)

# Diabetes interaction 1: blood test, measure hba1c
# Blood test at the GP to measure hba1c level (glucose level in diabetes)

def measure_hba1c(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "measure_hba1c",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "measure hba1c", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 4,      # to be updated for an accurate figure
        "glucose": 0,   # dummy glucose impact, to be updated
        "carbon": 6,    # update for more accurate figure
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.9, 29: 0.1}  # gp, outpatient diabetes

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 2: medication (metformin) 
# Appointment at a GP for a prescription of metformin, the first-line medication treatment

def medication_metformin(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "medication metformin",
        "start": patient_time,
    }

    entry = { 
        "resource_type" : "MedicationRequest",
        "name": "metformin", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 72.33,  # regular cost of GP appointment plus average prescription cost (PSSRU 2018-19)
        "glucose": -1,  # dummy glucose impact, update for more accurate figure  
        "carbon": 23,   # carbon impact for a ten minute appointment (6) and a prescription (17)
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.88, 7: 0.12} # gp, online lifestyle education

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        7: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )    

# Diabetes interaction 3: medication change 1 (double therapy)
# Appointment for GP appointment for prescription of adjuvant therapy (add a sulfonylurea to metformin, e.g. glicazide) alongside metformin
# Should be updated so that if hba1c hasn't changed in 6 months this happens,it shouldn't happen on the first appointment

def medication_change1(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "medication change 1",
        "start": patient_time,
    }

    entry = { 
        "resource_type" : "MedicationRequest",
        "name": "double therapy", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "value": {
          #  "value": 60,
          #  "unit": "mg",
          #  "system": "http://unitsofmeasure.org",
          #  "code": "mg",
        },
        "cost": 72.33,      # regular cost of GP appointment plus average prescription cost(PSSRU 2018-19)
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 23,       # carbon impact for a ten minute appointment (6) and a prescription (17) (PSSRU 2018-19)
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 7: 0.3, 29: 0.2} # gp, online lifestyle education, outpatient diabetes consultation

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        7: datetime.timedelta(days=20),
        29: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 4: medication change 2 (triple therapy)
# Appointment for a prescription of a third medication (to metformin and sulf.) for type 2 diabetes 
# To be updated: Shouldn't happen on the first appointment, or before the first two lines of therapy

def medication_change2(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "medication_change2",
        "start": patient_time,
    }

    entry = { 
        "resource_type" : "MedicationRequest",
        "name": "double therapy", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "value": {
          #  "value": 60,
          #  "unit": "mg",
          #  "system": "http://unitsofmeasure.org",
          #  "code": "mg",
        },
        "cost": 72.33,      # regular cost of GP appointment plus average prescription cost(PSSRU 2018-19)
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 23,       # carbon impact for a ten minute appointment (6) and a prescription (17) (PSSRU 2018-19)
    }

    new_patient_record_entries = [entry]

    next_environment_id_to_prob = {0: 0.5, 7: 0.3, 29: 0.2} # gp, online lifestyle education, outpatient diabetes consultation

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        7: datetime.timedelta(days=20),
        29: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 5: insulin
# Prescription of insulin for people with diabetes who require insulin
# To be updated: rule to be applied so this affects the relevant population

def insulin_prescription(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "insulin",
        "start": patient_time,
    }

    entry = { 
        "resource_type" : "MedicationRequest",
        "name": "insulin", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 72.33,      # regular cost of GP appointment plus average prescription cost(PSSRU 2018-19)
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 23,       # carbon impact for a ten minute appointment (6) and a prescription (17) (PSSRU 2018-19)
    }

    new_patient_record_entries = [entry]

    next_environment_id_to_prob = {0: 0.5, 7: 0.3, 29: 0.2} # gp, online lifestyle education, outpatient diabetes consultation

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        7: datetime.timedelta(days=20),
        29: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 6: high risk (of type 2 diabetes) management
# Management in primary care of care for people at high risk of developing type 2 diabetes
# To be updated: include a rule to call if hba1c is between 42 and 48 mmol/mol 

def highrisk_management(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "high risk management",
        "start": patient_time,
    }

    entry = { 
        "resource_type" : "ServiceRequest",
        "name": "high risk management", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 72.33,      # regular cost of GP appointment and prescription cost (PSSRU 2018-19)
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 6,        # carbon impact for a ten minute appointment (PSSRU 2018-19)
    }

    new_patient_record_entries = [entry]

    next_environment_id_to_prob = {0: 0.5, 9: 0.5}  # gp, digital diabetes prevention programme (ddpp)

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )    

# Diabetes interaction 7: exercise prescription
# Prescription in primary care of exercise (for example access to local gym facilities)

def exercise_prescription(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "exercise_prescription",
        "start": patient_time,
    }

    entry = { 
        "resource_type" : "ServiceRequest",
        "name": "exercise prescription", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 100.60,     # 2011 NIHR report, to be updated for a more up to date figure
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 23,       # carbon impact for a ten minute appointment (6) and a prescription (17) (PSSRU 2018-19)
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.8, 5: 0.2}  # gp, group education (e.g. DESMOND programme)

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        5: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 8: prediabetes diagnosis
# To be updated: include a rule to call if hba1c is between 42 and 48 mmol/mol

def prediabetes_diagnosis(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "prediabetes diagnosis",
        "start": patient_time,
    }

    condition = {
        "resource_type": "Condition",
        "name" : "prediabetes",
        "start": patient_time,
    }

    entry = { 
        "resource_type" : "ServiceRequest",
        "name": "prediabetes diagnosis", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 39.23,   # regular cost of GP appointment
        "glucose": -1,   # dummy glucose impact, to be updated
        "carbon": 23,    # carbon impact for a ten minute appointment (6) and a prescription (17) (PSSRU 2018-19)
    }

    new_patient_record_entries = [encounter, condition, entry]

    next_environment_id_to_prob = {0: 0.8, 9: 0.2} # gp, digital diabetes prevention programme (ddpp)

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Diabetes interaction 9: type 2 diabetes diagnosis
# Call if hba1c is over 48 mmol/mol

def t2dm_diagnosis(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "t2dm diagnosis",
        "start": patient_time,
    }

    condition = {
        "resource_type": "Condition",
        "name" : "t2dm diagnosis",
        "start": patient_time,
    }

    entry = { # should be hba1c in this one
        "resource_type" : "ServiceRequest",
        "name": "t2dm diagnosis", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 39.23,      # regular cost of GP appointment
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 6,        # carbon impact for a ten minute appointment (6)
    }

    new_patient_record_entries = [encounter, condition, entry]

    next_environment_id_to_prob = {0: 0.88, 5: 0.06, 7: 0.06} # gp, group education, online lifestyle programme

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        5: datetime.timedelta(days=20),
        7: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Diabetes interaction 10: glucose management
# Ongoing management of glucose by a GP (every 6 months if stable, or otherwise every 3 months) 

def glucose_management(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "glucose management",
        "start": patient_time,
    }

    entry = { # should be hba1c in this one
        "resource_type" : "ServiceRequest",
        "name": "glucose management",
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 39.23,      # regular cost of a GP appointment
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 6,        # carbon impact for a ten minute appointment (6)
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 29: 0.25, 31: 0.25}  # gp, outpatient diabetes, outpatient urology

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
        31: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )
    
# Diabetes interaction 11: annual health check.
# To be updated: rule needed so that this happens on an annual basis.

def annual_health_check(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "annual_health_check",
        "start": patient_time,
    }

    entry = { 
        "resource_type" : "ServiceRequest",
        "name": "annual_health_check", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 39.23,      # regular cost of a GP appointment
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 6,        # carbon impact for a ten minute appointment (6)
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 19: 0.3, 23: 0.1, 35: 0.1} # gp, smoking service, eye care, foot clinic

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        19: datetime.timedelta(days=20),
        23: datetime.timedelta(days=20),
        35: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 12: hypertension management
# measure blood pressure 

def hypertension_management(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "hypertension management",
        "start": patient_time,
    }

    entry = { # should be hba1c in this one
        "resource_type" : "ServiceRequest",
        "name": "hypertension management", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 39.23,      # regular cost of a GP appointment
        "glucose": 0,       # dummy glucose impact, to be updated
        "carbon": 6,        # carbon impact for a ten minute appointment (6)
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 29: 0.5} # gp, outpatient diabetes

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 13: complications/ conditions identification and management 

def complications_id_mant(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "complications id and management",
        "start": patient_time,
    }

    entry = { # should be foot health, mental health, maternity in this one
        "resource_type" : "ServiceRequest",
        "name": "complications id and management", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 39.23,      # regular cost of a GP appointment
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 6,        # carbon impact for a ten minute appointment (6)
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {35: 0.5, 13: 0.3, 17: 0.2} # foot clinic, mental health service, maternity service

    next_environment_id_to_time = {
        35: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        13: datetime.timedelta(days=20),
        17: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 14: glucose clinic 
# primary care glucose clinic rather than GP managing glucose in 8.

def glucose_clinic(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "glucose_clinic",
        "start": patient_time,
    }

    entry = { 
        "resource_type" : "ServiceRequest",
        "name": "glucose_clinic", 
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "cost": 39.23,       # regular cost of a GP appointment (to update to primary care nurse cost)
        "glucose": -1,      # dummy glucose impact, to be updated
        "carbon": 6,        # carbon impact for a ten minute appointment (6)
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.9, 29: 0.1} # gp, outpatient diabetes

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )