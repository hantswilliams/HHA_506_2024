from hantsfunctions import hemo, hemato

# import hantsfunctions as labfunctions # this also works but is not recommend 
# labfunctions.hemo()
# labfunctions.hemato(hematocrit=34)

#### Lists 


listofPeople = ['Hants', 'John', 'Alex']
listofPeople[0]
listofPeople[:2]

listofPeople.append('Mike')
listofPeople.remove('Hants')

simpleDictionary_1 = {
    'patient_name': 'Hants',
    'age': 30,
    }

simpleDictionary_2 = {
    'patient_name': 'Williams',
    'age': 40,
    }


simpleDictionary_1['patient_name']
simpleDictionary_1['age']

simpleDictionary_2.get('123')

print('This is NOW going to run....')
print(simpleDictionary_1)
print('----------')
print(simpleDictionary_2)


def specialFunction():
    variableName = 'Hants'
    return f'The persons name is: {variableName}'

specialFunction()


def specialFunction2(name):
    receivedValue = name
    return f'The persons name is: {receivedValue}'

inputtedNamed = 3
specialFunction2(inputtedNamed)


def specialFunction2(value1, value2):
    if type(value1) != int:
        return 'Please enter a valid number for value 1'
    if type(value2) != int:
        return 'Please enter a valid number for value 2'
    calculation = value1 + value2
    return calculation

def specialFunction3(value1, value2):
    if type(value1) != int:
        return 'Please enter a valid number for value 1'
    if type(value2) != int:
        return 'Please enter a valid number for value 2'
    calculation = value1 + value2
    calculation2 = value1 * value2
    return calculation, calculation2

def specialFunction4(value1, value2):
    if type(value1) != int:
        return 'Please enter a valid number for value 1'
    if type(value2) != int:
        return 'Please enter a valid number for value 2'
    calculation = value1 + value2
    calculation2 = value1 * value2
    output = {
        'calculation1': calculation,
        'calculation2': calculation2
    }
    return output

specialFunction3(2, 7) ### this will not save the output 
specialFunction3(50, 23) ### this will not save the output 
specialFunction3(24, 42) ### this will not save the output 
specialFunction3(15, 23) ### this will not save the output 
specialFunction3(12, 43) ### this will not save the output 

output1, output2 = specialFunction3(5, 10) ## this will save the output as output1 and output2

output = specialFunction3(5, 10) ## this will save the output as output
output[0]

output4 = specialFunction4(300, 200)
type(output4)
output4.keys()
output4['calculation1']
output4['calculation2']


def labValueAnalysis(**kwargs):
    platelets_input = kwargs.get('platelets', None)
    hemoglobin_input = kwargs.get('hemoglobin', None)
    wbc_input = kwargs.get('wbc', None)
    
    if platelets_input >= 100 and platelets_input < 450:
        platelet_inter = 'Normal'
    else:
        platelet_inter = 'Abnormal'

    if hemoglobin_input >= 13.5 and hemoglobin_input <= 17.5:
        hemoglobin_inter = 'Normal'
    else:
        hemoglobin_inter = 'Abnormal'
    
    output = {
        'platelets_value': platelets_input,
        'platelets_interpretation': platelet_inter,
        'hemoglobin_value': hemoglobin_input,
        'hemoglobin_interpretation': hemoglobin_inter,
        'wbc': wbc_input,
    }
    return output

labValueAnalysis(platelets=99, hemoglobin=10, wbc=2000)





# labanalysis_hemoglobin(hemoglobin=10)
# labanalysis_hemoglobin(hemoglobin=15)
# labanalysis_hemoglobin(hemoglobin=30)
# labanalysis_hemoglobin(hemoglobin=50)
# labanalysis_hemoglobin(hemoglobin=23)
# labanalysis_hemoglobin(hemoglobin=24.5)

