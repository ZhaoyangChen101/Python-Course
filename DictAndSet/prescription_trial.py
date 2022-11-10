from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    # if warfarin in prescription:  # 这个比较会比较耗时，毕竟不满足的会是少数。这里适合用exception。
    #     prescription.remove(warfarin)  # discard此处不适合了。
    #     prescription.add(edoxaban)
    # else:
    #     print(f"Patient {patient} is not taking Warfarin."
    #           f" Please remove {patient} from the trial.")
    try:  # 这个比较会比较耗时，毕竟不满足的会是少数。这里适合用exception。
        prescription.remove(warfarin)  # discard此处不适合了。
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial.")
    print(patient, prescription)