def hemo(**kwargs):
    hemoglobin_input = kwargs.get('hemoglobin', None)
    
    if hemoglobin_input >= 13.5 and hemoglobin_input <= 17.5:
        hemoglobin_inter = 'Normal'
    else:
        hemoglobin_inter = 'Abnormal'
    
    output = {
        'hemoglobin_value': hemoglobin_input,
        'hemoglobin_interpretation': hemoglobin_inter,
    }
    return output


def hemato(**kwargs):
    hemat_input = kwargs.get('hematocrit', None)
    
    if hemat_input >= 40 and hemat_input <= 55:
        hemat_inter = 'Normal'
    else:
        hemat_inter = 'Abnormal'
    
    output = {
        'hematocrit_value': hemat_input,
        'hematocrit_interpretation': hemat_inter,
    }
    return output