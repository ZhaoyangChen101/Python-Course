from prescription_data import patients
trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

while trial_patients:
    patient = trial_patients.pop()  # pop removes and returns
    print(patient, end=": ")
    prescription = patients[patient]
    print(prescription)

# set is unordered
