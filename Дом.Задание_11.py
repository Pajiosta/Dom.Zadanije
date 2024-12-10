import pandas as pd


def chickenpox_by_sex():
    df = pd.read_csv('data.csv')
    vaccinated = df[df['P_NUMVRC'] > 0]

    illed = vaccinated[vaccinated['HAD_CPOX'] == 1]

    not_illed = vaccinated[vaccinated['HAD_CPOX'] == 2]

    male_ratio = len(illed[illed['SEX'] == 1]) / len(not_illed[not_illed['SEX'] == 1])
    female_ratio = len(illed[illed['SEX'] == 2]) / len(not_illed[not_illed['SEX'] == 2])

    return {"male": male_ratio, "female": female_ratio}

result = chickenpox_by_sex()
print(result)
