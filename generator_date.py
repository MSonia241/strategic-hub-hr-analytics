import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# setăm seed-ul pentru rezultate constante
np.random.seed(101)

num_angajati_unici = 200
luni_de_analiza = 12

manageri = ['Andrei P.', 'Maria I.', 'Ion V.', 'Elena D.', 'George R.', 'Ana S.', 'Mihai O.', 'Cristina D.']
departamente = ['Vanzari', 'IT', 'HR', 'Marketing']
nivele_senioritate = ['Junior', 'Mid', 'Senior']

orase_romania = ['Bucuresti', 'Cluj-Napoca', 'Timisoara', 'Iasi', 'Brasov', 'Sibiu', 'Constanta']

# generare
ids = range(1000, 1000 + num_angajati_unici)
orase_alese = np.random.choice(orase_romania, num_angajati_unici)

base_data = {
    'ID_Angajat': ids,
    'Manager': np.random.choice(manageri, num_angajati_unici),
    'Departament': np.random.choice(departamente, num_angajati_unici),
    'Senioritate': np.random.choice(nivele_senioritate, num_angajati_unici, p=[0.4, 0.4, 0.2]),
    'Oras': orase_alese
}
df_base = pd.DataFrame(base_data)

# generare date lunare
all_monthly_data = []
start_date = datetime(2023, 1, 1)

for i in range(luni_de_analiza):
    current_date = start_date + pd.DateOffset(months=i)
    df_month = df_base.copy()
    df_month['Data'] = current_date

    # date variabile
    df_month['Ore_Lucrate'] = np.random.randint(140, 260, num_angajati_unici)
    df_month['Proiecte_Finalizate'] = np.random.randint(1, 15, num_angajati_unici)
    df_month['Feedback_Clienti'] = np.random.uniform(1, 5, num_angajati_unici).round(1)
    df_month['Training_Ore'] = np.random.randint(0, 40, num_angajati_unici)

    df_month['Scor_Performanta'] = (df_month['Proiecte_Finalizate'] * 10) + \
                                   (df_month['Ore_Lucrate'] * 0.5) + \
                                   (df_month['Feedback_Clienti'] * 20)

    df_month.loc[df_month['Senioritate'] == 'Senior', 'Scor_Performanta'] += 50

    df_month['Risc_Plecare_Scor'] = 0.0
    df_month.loc[(df_month['Ore_Lucrate'] > 200) & (df_month['Feedback_Clienti'] < 3), 'Risc_Plecare_Scor'] = 1.0
    df_month.loc[df_month['Training_Ore'] > 20, 'Risc_Plecare_Scor'] -= 0.2
    df_month['Risc_Plecare_Scor'] = df_month['Risc_Plecare_Scor'].clip(lower=0)

    conditions = [
        (df_month['Risc_Plecare_Scor'] > 0.5),
        (df_month['Scor_Performanta'] > 300) & (df_month['Risc_Plecare_Scor'] <= 0.5),
    ]
    choices = ['Risc Ridicat', 'Potential']
    df_month['Status_Risc'] = np.select(conditions, choices, default='Stabil')

    all_monthly_data.append(df_month)

# concatenare
df_final = pd.concat(all_monthly_data, ignore_index=True)

# export
nume_fisier = r"C:\Users\Sonia\OneDrive\Desktop\licenta\date_angajati_istoric.csv"
df_final.to_csv(nume_fisier, index=False)

print(f"GATA! Am salvat fisierul '{nume_fisier}'.")
print(f"Coloanele sunt: {df_final.columns.tolist()}")
print(f"Distributie Status_Risc:\n{df_final['Status_Risc'].value_counts()}")
