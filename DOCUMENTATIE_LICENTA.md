
# DOCUMENTAȚIE PROIECT LICENȚĂ
## Sistem de Analiză a Performanței și Riscului Resurselor Umane
### Dashboard Power BI cu Machine Learning integrat

---

## CUPRINS

1. [Prezentare Generală](#1-prezentare-generală)
2. [Contextul Academic și Motivația Proiectului](#2-contextul-academic-și-motivația-proiectului)
3. [Generarea și Structura Datelor Sintetice](#3-generarea-și-structura-datelor-sintetice)
4. [Arhitectura Datelor — Modelul Semantic Power BI](#4-arhitectura-datelor--modelul-semantic-power-bi)
5. [Logica de Calcul — Măsuri DAX](#5-logica-de-calcul--măsuri-dax)
6. [Structura Raportului — Cele 14 Pagini](#6-structura-raportului--cele-14-pagini)
7. [Componente de Machine Learning și Statistică Avansată](#7-componente-de-machine-learning-și-statistică-avansată)
8. [Simulări What-If](#8-simulări-what-if)
9. [Tehnologii și Instrumente Utilizate](#9-tehnologii-și-instrumente-utilizate)
10. [Funcționalități Cheie ale Sistemului](#10-funcționalități-cheie-ale-sistemului)
11. [Fluxul de Navigare](#11-fluxul-de-navigare)
12. [Structura Fișierelor Proiectului](#12-structura-fișierelor-proiectului)
13. [Configurare Tehnică Raport](#13-configurare-tehnică-raport)
14. [Contribuții Academice și Concluzii](#14-contribuții-academice-și-concluzii)

---

## 1. PREZENTARE GENERALĂ

**Titlul proiectului:** Sistem de Analiză a Performanței și Riscului Resurselor Umane (Strategic Hub)  
**Tehnologie principală:** Microsoft Power BI Desktop (format PBIP — Power BI Project)  
**Limbă interfață:** Română (ro-RO)  
**Număr de pagini (ecrane) Power BI:** 15  
**Sursa de date:** Fișier CSV (`date_angajati_istoric.csv`) — date istorice simulate despre angajați  
**Perioada analizată:** Ianuarie 2023 — Decembrie 2023 (12 luni)  
**Număr angajați simulați:** 200  
**Număr total înregistrări:** 2.400 (200 angajați × 12 luni)  

**Scopul general al proiectului:**  
Proiectul reprezintă un sistem complet de Business Intelligence (BI) destinat departamentelor de Resurse Umane și managementului executiv. Sistemul permite monitorizarea performanței angajaților, identificarea și predicția riscului de fluctuație a personalului (employee turnover), analiza factorilor care influențează performanța și simularea impactului intervențiilor de tip training. Sunt integrate tehnici de analiză statistică avansată și algoritmi de machine learning (K-Means Clustering, Regresie Liniară) direct în mediul Power BI, prin vizualizări Python personalizate.

---

## 2. CONTEXTUL ACADEMIC ȘI MOTIVAȚIA PROIECTULUI

### 2.1 Problematica abordată

Fluctuația personalului (*employee turnover*) reprezintă una dintre cele mai costisitoare provocări ale managementului modern de resurse umane. Studiile din literatura de specialitate estimează că înlocuirea unui angajat costă între 50% și 200% din salariul anual al acestuia, incluzând costurile de recrutare, onboarding, pierderea productivității și transferul de cunoștințe. În acest context, capacitatea de a anticipa riscul de plecare al unui angajat înainte ca acesta să devină efectiv reprezintă un avantaj competitiv semnificativ.

Totodată, analiza performanței individuale și de echipă, corelată cu factori observabili (ore lucrate, participare la training, feedback clienți), permite organizațiilor să ia decizii bazate pe date (*data-driven decisions*) în loc de intuiție managerială.

### 2.2 Obiectivele specifice ale proiectului

1. **Crearea unui set de date realist** prin simulare statistică controlată, reproducând caracteristici din mediul organizațional real (distribuții de senioritate, variabilitate lunară, corelații între factori)
2. **Construirea unui model semantic** în Power BI care să permită analize temporale, geografice și dimensionale
3. **Implementarea unui sistem de clasificare a riscului** pe trei niveluri, bazat pe reguli de business explicabile
4. **Integrarea algoritmilor de machine learning** (regresie liniară, clustering K-Means) în mediul BI
5. **Dezvoltarea unui sistem de simulare What-If** pentru evaluarea impactului intervențiilor de training
6. **Proiectarea unui dashboard interactiv** cu UX intuitiv, navigare structurată și vizualizări statistice avansate

### 2.3 Relevanța domeniului Business Intelligence în HR

Business Intelligence aplicat în Resurse Umane (denumit uneori *People Analytics* sau *Workforce Analytics*) este un domeniu în expansiune rapidă. Conform rapoartelor Deloitte și Gartner, peste 70% din organizațiile Fortune 500 investesc în soluții de HR Analytics, iar platformele BI precum Power BI, Tableau sau Qlik Sense au devenit instrumente standard în departamentele de HR modernizate.

Proiectul de față demonstrează cum o platformă BI accesibilă (Power BI) poate fi extinsă cu capabilități de Machine Learning prin integrarea Python, obținând funcționalități comparabile cu soluțiile enterprise dedicate.

---

## 3. GENERAREA ȘI STRUCTURA DATELOR SINTETICE

### 3.1 Justificarea utilizării datelor sintetice

Întrucât proiectul are caracter academic și nu are acces la date reale din organizații, a fost necesar să se genereze un set de date sintetic (*synthetic data*). Datele sintetice au avantajul că:
- Nu ridică probleme de confidențialitate sau GDPR
- Pot fi controlate statistic pentru a reflecta scenarii realiste
- Permit reproducibilitatea completă a rezultatelor (prin fixarea seed-ului aleator)
- Pot include corelații și distribuții specifice domeniului HR

### 3.2 Scriptul Python de generare a datelor

Datele au fost generate prin intermediul unui script Python utilizând bibliotecile `pandas` și `numpy`. Mai jos este prezentat scriptul complet, cu explicații detaliate pentru fiecare secțiune.

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Setăm seed-ul pentru rezultate constante
np.random.seed(101)
```

**Motivație tehnică:** Fixarea seed-ului (`np.random.seed(101)`) asigură că rulările repetate ale scriptului produc exact același set de date. Aceasta este o practică esențială în cercetarea reproductibilă (*reproducible research*), permițând oricui să regenereze datele identic.

---

#### 3.2.1 Configurarea parametrilor de simulare

```python
num_angajati_unici = 200
luni_de_analiza = 12

manageri = ['Andrei P.', 'Maria I.', 'Ion V.', 'Elena D.',
            'George R.', 'Ana S.', 'Mihai O.', 'Cristina D.']

departamente = ['Vanzari', 'IT', 'HR', 'Marketing']

nivele_senioritate = ['Junior', 'Mid', 'Senior']

orase_romania = ['Bucuresti', 'Cluj-Napoca', 'Timisoara',
                 'Iasi', 'Brasov', 'Sibiu', 'Constanta']
```

**Detalii de design:**
- **200 de angajați** reprezintă o dimensiune organizațională de tip *mid-size company*, suficient de mare pentru ca analizele statistice să fie semnificative
- **8 manageri** → raport mediu de ~25 de angajați per manager (în limitele normale: 15–30)
- **4 departamente** acoperă structura clasică a unei companii de servicii: Vânzări, IT, HR, Marketing
- **7 orașe** din România sunt alese pentru a reflecta distribuția geografică realistă a companiilor cu prezență națională
- Nivelele de senioritate urmează o distribuție ponderată (descrisă mai jos)

---

#### 3.2.2 Generarea bazei statice de angajați

```python
ids = range(1000, 1000 + num_angajati_unici)
orase_alese = np.random.choice(orase_romania, num_angajati_unici)

base_data = {
    'ID_Angajat': ids,
    'Manager': np.random.choice(manageri, num_angajati_unici),
    'Departament': np.random.choice(departamente, num_angajati_unici),
    'Senioritate': np.random.choice(
        nivele_senioritate, num_angajati_unici, p=[0.4, 0.4, 0.2]
    ),
    'Oras': orase_alese
}
df_base = pd.DataFrame(base_data)
```

**Distribuția seniorității** este definită prin vectorul de probabilități `p=[0.4, 0.4, 0.2]`:

| Nivel | Probabilitate | Angajați estimați |
|---|---|---|
| Junior | 40% | ~80 |
| Mid | 40% | ~80 |
| Senior | 20% | ~40 |

Această distribuție reflectă piramida tipică de senioritate dintr-o companie, unde seniorii reprezintă o minoritate valoroasă. Atributele statice (Manager, Departament, Senioritate, Oraș) sunt fixate la generare și rămân constante pe toată perioada de 12 luni — același angajat nu schimbă departamentul sau managerul, ceea ce corespunde realității organizaționale pe termen scurt.

---

#### 3.2.3 Generarea datelor lunare variabile

```python
for i in range(luni_de_analiza):
    current_date = start_date + pd.DateOffset(months=i)
    df_month = df_base.copy()
    df_month['Data'] = current_date

    df_month['Ore_Lucrate']        = np.random.randint(140, 260, num_angajati_unici)
    df_month['Proiecte_Finalizate'] = np.random.randint(1, 15, num_angajati_unici)
    df_month['Feedback_Clienti']   = np.random.uniform(1, 5, num_angajati_unici).round(1)
    df_month['Training_Ore']       = np.random.randint(0, 40, num_angajati_unici)
```

**Intervalele de generare și justificarea lor:**

| Coloană | Tip | Interval | Justificare |
|---|---|---|---|
| `Ore_Lucrate` | Întreg uniform | [140, 260] | Un angajat full-time lucrează ~168 h/lună (8h × 21 zile). Intervalul [140, 260] captează variabilitate: angajați part-time, ore suplimentare, concedii |
| `Proiecte_Finalizate` | Întreg uniform | [1, 15] | 1–2 proiecte lunare = volum scăzut; 10–15 = volum mare. Adecvat pentru roluri de tip vânzări sau IT |
| `Feedback_Clienti` | Real uniform | [1.0, 5.0] | Scală de tip Likert cu 1 zecimală, de la 1 (foarte slab) la 5 (excelent) |
| `Training_Ore` | Întreg uniform | [0, 40] | Intervalul acoperă angajați fără training (0) până la programe intensive (40h/lună) |

---

#### 3.2.4 Formula de calcul a Scorului de Performanță

```python
df_month['Scor_Performanta'] = (
    df_month['Proiecte_Finalizate'] * 10 +
    df_month['Ore_Lucrate'] * 0.5 +
    df_month['Feedback_Clienti'] * 20
)

# Bonus pentru angajații seniori
df_month.loc[df_month['Senioritate'] == 'Senior', 'Scor_Performanta'] += 50
```

**Formulă matematică:**

$$ScorPerformanta = (ProiecteFinalizate \times 10) + (OreLucrate \times 0.5) + (FeedbackClienti \times 20) + Bonus_{Senior}$$

unde:

$$Bonus_{Senior} = \begin{cases} 50 & \text{dacă Senioritate = "Senior"} \\ 0 & \text{altfel} \end{cases}$$

**Analiza intervalului rezultat:**

- Valoare minimă teoretică (fără Senior bonus):  
  $(1 \times 10) + (140 \times 0.5) + (1.0 \times 20) = 10 + 70 + 20 = 100$ puncte
- Valoare maximă teoretică (fără Senior bonus):  
  $(14 \times 10) + (259 \times 0.5) + (5.0 \times 20) = 140 + 129.5 + 100 = 369.5$ puncte
- Cu bonus Senior: se adaugă 50 de puncte → maxim ~419.5 puncte

**Ponderarea factorilor:**  
Coeficienții (10, 0.5, 20) au fost aleși astfel încât fiecare factor să contribuie proporțional la scor, dar feedback-ul clienților și proiectele finalizate să aibă un impact mai mare decât simpla prezență (ore lucrate), reflectând filozofia că *calitatea* muncii contează mai mult decât *cantitatea*.

---

#### 3.2.5 Formula de calcul a Riscului de Plecare

```python
df_month['Risc_Plecare_Scor'] = 0.0

# Condiție principală de risc
df_month.loc[
    (df_month['Ore_Lucrate'] > 200) & (df_month['Feedback_Clienti'] < 3),
    'Risc_Plecare_Scor'
] = 1.0

# Factor de reducere a riscului prin training
df_month.loc[df_month['Training_Ore'] > 20, 'Risc_Plecare_Scor'] -= 0.2

# Asigurăm că scorul nu scade sub 0
df_month['Risc_Plecare_Scor'] = df_month['Risc_Plecare_Scor'].clip(lower=0)
```

**Logica decizională — Risc_Plecare_Scor:**

$$RiscScor = \begin{cases} 1.0 & \text{dacă } OreLucrate > 200 \text{ ȘI } FeedbackClienti < 3.0 \\ 0.0 & \text{altfel} \end{cases} - \begin{cases} 0.2 & \text{dacă } TrainingOre > 20 \\ 0.0 & \text{altfel} \end{cases}$$

**Interpretare:**
- Un angajat cu **ore de muncă excesive** (>200h/lună, semn de supraîncărcare) **și** cu **feedback slab de la clienți** (<3.0, semn de dezengajament) este considerat la risc maxim (scor = 1.0)
- Dacă acel angajat beneficiază de **training intens** (>20h/lună), riscul se reduce cu 0.2, reflectând efectul pozitiv al investiției în dezvoltare profesională
- Scorul este *clipuit* la 0 pentru a preveni valori negative fără sens

---

#### 3.2.6 Clasificarea în categorii de Status_Risc

```python
conditions = [
    (df_month['Risc_Plecare_Scor'] > 0.5),
    (df_month['Scor_Performanta'] > 300) & (df_month['Risc_Plecare_Scor'] <= 0.5),
]
choices = ['Risc Ridicat', 'Potential']
df_month['Status_Risc'] = np.select(conditions, choices, default='Stabil')
```

**Tabel de decizie pentru Status_Risc:**

| Condiție | Categorie atribuită |
|---|---|
| `Risc_Plecare_Scor > 0.5` | **Risc Ridicat** |
| `Scor_Performanta > 300` ȘI `Risc_Plecare_Scor ≤ 0.5` | **Potential** |
| Altfel (nicio condiție nu e îndeplinită) | **Stabil** |

Funcția `np.select()` aplică condițiile în ordine, prima condiție adevărată câștigând. Categoria **Stabil** este *default* — angajații care nu sunt nici la risc, nici performeri excepționali.

**Distribuția așteptată a categoriilor** (aproximativă, bazată pe probabilitățile de generare):
- **Stabil:** ~70–75% — angajații cu performanță normală și risc scăzut
- **Potential:** ~15–20% — angajații cu scor ridicat dar fără semne de risc
- **Risc Ridicat:** ~10–15% — angajații cu supraîncărcare și feedback slab

---

#### 3.2.7 Export și structura fișierului CSV

```python
df_final = pd.concat(all_monthly_data, ignore_index=True)
df_final.to_csv(
    r"C:\Users\Sonia\OneDrive\Desktop\licenta\date_angajati_istoric.csv",
    index=False
)
```

**Structura finală a fișierului CSV:**

| Coloană | Tip Python | Tip Power BI | Origine |
|---|---|---|---|
| `ID_Angajat` | `int64` | Text | Statică (1000–1199) |
| `Manager` | `object` (string) | Text | Statică (8 valori) |
| `Departament` | `object` (string) | Text | Statică (4 valori) |
| `Senioritate` | `object` (string) | Text | Statică (3 valori) |
| `Oras` | `object` (string) | Text | Statică (7 valori) |
| `Data` | `datetime64` | Data/Timp | Lunară (ian–dec 2023) |
| `Ore_Lucrate` | `int64` | Număr întreg | Variabilă lunară |
| `Proiecte_Finalizate` | `int64` | Număr întreg | Variabilă lunară |
| `Feedback_Clienti` | `float64` | Număr zecimal | Variabilă lunară |
| `Training_Ore` | `int64` | Număr întreg | Variabilă lunară |
| `Scor_Performanta` | `float64` | Număr zecimal | Calculată |
| `Risc_Plecare_Scor` | `float64` | Număr zecimal | Calculată |
| `Status_Risc` | `object` (string) | Text | Calculată (3 categorii) |

**Dimensiunile setului de date:**
- Număr rânduri: **2.400** (200 angajați × 12 luni)
- Număr coloane: **13**
- Dimensiune estimată pe disc: ~350–450 KB

---

### 3.3 Proprietățile statistice ale datelor generate

Datorită generării prin distribuții uniforme și normale, setul de date prezintă următoarele caracteristici statistice așteptate:

**Ore_Lucrate** — Distribuție uniformă discretă U[140, 260]:
- Medie teoretică: 200 ore
- Deviație standard: ~34.6 ore

**Feedback_Clienti** — Distribuție uniformă continuă U[1.0, 5.0]:
- Medie teoretică: 3.0
- Deviație standard: ~1.15

**Scor_Performanta** — Distribuție derivată (sumă de variabile uniforme):
- Medie teoretică (non-Senior): ~235 puncte
- Medie teoretică (Senior): ~285 puncte

**Corelații așteptate:**
- `Ore_Lucrate` ↔ `Scor_Performanta`: corelație pozitivă moderată (~0.4–0.5), datorită termenului `Ore_Lucrate × 0.5` din formulă
- `Proiecte_Finalizate` ↔ `Scor_Performanta`: corelație pozitivă puternică (~0.6–0.7), datorită termenului `Proiecte × 10`
- `Feedback_Clienti` ↔ `Scor_Performanta`: corelație pozitivă moderată (~0.4–0.5)
- `Ore_Lucrate` ↔ `Risc_Plecare_Scor`: corelație pozitivă slabă (risc apare doar la ore >200)
- `Training_Ore` ↔ `Risc_Plecare_Scor`: corelație negativă slabă (training reduce riscul)

---

## 4. ARHITECTURA DATELOR — MODELUL SEMANTIC POWER BI

### 4.1 Sursa de date și importul

- **Tip sursă:** Fișier CSV importat în Power BI
- **Mod conectare:** Import (datele sunt încărcate complet în memoria Power BI, nu interogare live)
- **Avantajul modului Import:** Performanță maximă pentru vizualizări, calcule DAX rapide, funcționare offline
- **Encoding:** Windows-1250 (suportă caractere românești: ș, ț, â, î, ă)
- **Delimitator câmpuri:** Virgulă (`,`)
- **Prima linie:** Antet de coloane

### 4.2 Tabele din modelul semantic

#### Tabelul de fapte: `date_angajati`
Tabel principal care conține toate înregistrările istorice. Este de tip *fact table* în terminologia modelării dimensionale (schema stea), fiecare rând reprezentând o măsurătoare lunară pentru un angajat.

| Coloană | Tip Power BI | Rol în model |
|---|---|---|
| `ID_Angajat` | Text | Dimensiune — identificator unic angajat |
| `Manager` | Text | Dimensiune — filtrare pe manager |
| `Departament` | Text | Dimensiune — filtrare pe departament |
| `Senioritate` | Text | Dimensiune — filtrare pe nivel |
| `Oras` | Text | Dimensiune — filtrare geografică |
| `Data` | Data/Timp | Dimensiune timp — axa temporală |
| `Ore_Lucrate` | Număr întreg | Metrică (faptă) |
| `Proiecte_Finalizate` | Număr întreg | Metrică (faptă) |
| `Feedback_Clienti` | Număr zecimal | Metrică (faptă) |
| `Training_Ore` | Număr întreg | Metrică (faptă) |
| `Scor_Performanta` | Număr zecimal | Metrică calculată (faptă derivată) |
| `Risc_Plecare_Scor` | Număr zecimal | Metrică calculată (faptă derivată) |
| `Status_Risc` | Text | Dimensiune calculată — categorie risc |

#### Tabelul de parametri: `Simulare_Training`
Tabel calculat prin DAX folosind funcția `GENERATESERIES`. Conține o singură coloană cu valorile: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 (11 valori, cu pasul de 5).

```dax
Simulare_Training = GENERATESERIES(0, 50, 5)
```

**Scop:** Parametru interactiv de tip What-If. Utilizatorul selectează un număr de ore de training suplimentar prin slicer, iar măsurile DAX calculează automat impactul estimat asupra performanței.

#### Tabele sistem (ascunse):
- `LocalDateTable_...` — Tabel de date generat automat de Power BI din intervalul `MIN/MAX(date_angajati[Data])`. Activat automat pentru a permite funcțiile de **time intelligence** DAX (YTD, MTD, SAMEPERIODLASTYEAR etc.)
- `DateTableTemplate_...` — Șablon intern Power BI, necesar pentru generarea tabelelor de date

### 4.3 Relații între tabele

| De la (many) | La (one) | Cardinalitate | Filtru încrucișat |
|---|---|---|---|
| `date_angajati[Data]` | `LocalDateTable[Date]` | Many-to-One (*:1) | Unidirecțional |

`Simulare_Training` nu are relație formală — este referit direct în expresii DAX prin `SELECTEDVALUE()`.

### 4.4 Modelul de date — schema logică

```
┌─────────────────────────────┐
│     LocalDateTable          │
│  Date (PK) │ Year │ Month   │
└──────┬──────────────────────┘
       │ 1
       │
       │ *
┌──────┴──────────────────────────────────────────────────┐
│                    date_angajati                        │
│  ID_Angajat │ Manager │ Departament │ Senioritate       │
│  Oras │ Data │ Ore_Lucrate │ Proiecte_Finalizate        │
│  Feedback_Clienti │ Training_Ore │ Scor_Performanta     │
│  Risc_Plecare_Scor │ Status_Risc                        │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────┐
│     Simulare_Training       │
│  Simulare_Training (0–50)   │
│  [referit direct în DAX]    │
└─────────────────────────────┘
```

---

## 5. LOGICA DE CALCUL — MĂSURI DAX

DAX (*Data Analysis Expressions*) este limbajul de formule utilizat în Power BI, Excel Power Pivot și Analysis Services pentru crearea de calcule analitice. Toate măsurile sunt evaluate în contextul de filtrare curent (pagina, slicerele active, selecțiile vizuale).

### 5.1 Măsuri în tabelul `date_angajati`

---

**1. `Total_Angajati`**
```dax
Total_Angajati = DISTINCTCOUNT('date_angajati'[ID_Angajat])
```
Numără angajații unici din contextul de filtrare curent. Funcția `DISTINCTCOUNT` elimină duplicatele rezultate din structura longitudinală (un angajat apare de 12 ori — câte o dată per lună). Utilizare: card KPI principal pe meniul de start și pe pagini de analiză.

---

**2. `Procent_Risc`**
```dax
Procent_Risc =
DIVIDE(
    COUNTROWS(FILTER('date_angajati', 'date_angajati'[Status_Risc] = "Risc Ridicat")),
    COUNTROWS('date_angajati')
) * 100
```
Calculează procentul înregistrărilor lunare cu status „Risc Ridicat" față de totalul înregistrărilor din contextul curent. `DIVIDE` este preferată față de operatorul `/` deoarece gestionează elegant împărțirea la zero (returnează 0 în loc de eroare). Rezultat afișat cu o zecimală și simbolul `%`.

---

**3. `Top_Performers`**
```dax
Top_Performers = COUNTROWS(FILTER('date_angajati', 'date_angajati'[Status_Risc] = "Potential"))
```
Numără înregistrările lunare clasificate ca „Potential" (performeri de top cu risc scăzut). Utilizat ca KPI pentru monitorizarea angajaților cu potențial ridicat.

---

**4. `Dept_Burnout`**
```dax
Dept_Burnout =
TOPN(
    1,
    VALUES('date_angajati'[Departament]),
    CALCULATE(
        COUNTROWS(FILTER('date_angajati', 'date_angajati'[Status_Risc] = "Risc Ridicat")),
        ALLEXCEPT('date_angajati', 'date_angajati'[Departament])
    )
)
```
Identifică departamentul cu cel mai mare număr absolut de angajați la risc ridicat. `TOPN(1, ...)` extrage primul rând după criteriul de ordonare. `ALLEXCEPT` elimină toate filtrele active cu excepția filtrului pe `Departament`, permițând compararea departamentelor indiferent de alte filtre selectate.

---

**5. `Prag_Burnout`**
```dax
Prag_Burnout = 220
```
Constantă utilizată ca linie de referință în vizualizări (linie de prag pe graficele de ore lucrate). Valoarea 220 este aleasă ca prag de supraîncărcare — angajații care depășesc 220 ore/lună sunt considerați în zona de risc burnout. Funcționează și ca linie de referință vizuală în grafice.

---

**6. `Scor_Estimat`**
```dax
Scor_Estimat =
AVERAGE(date_angajati[Scor_Performanta])
+ (SELECTEDVALUE('Simulare_Training'[Simulare_Training]) * 0.5)
```
Estimează scorul de performanță după adăugarea orelor de training simulate. Factorul de multiplicare `0.5` puncte per oră de training este consistent cu coeficientul folosit și pentru `Ore_Lucrate` în scriptul de generare. `SELECTEDVALUE` extrage valoarea curent selectată din slicerul de simulare; dacă nu este selectată nicio valoare, returnează BLANK() (scenariul de bază).

---

**7. `Castig_Puncte`**
```dax
Castig_Puncte = [Scor_Estimat] - AVERAGE(date_angajati[Scor_Performanta])
```
Câștigul net de puncte față de scorul de bază, adus de training-ul simulat. Valoarea este 0 când nu este selectat niciun training, și crește proporțional cu orele selectate. Utilizat pentru a comunica clar beneficiul training-ului în termeni cuantificabili.

---

### 5.2 Măsuri în tabelul `Simulare_Training`

**8. `'Simulare_Training Value'`**
```dax
'Simulare_Training Value' = SELECTEDVALUE('Simulare_Training'[Simulare_Training], 0)
```
Extrage valoarea curent selectată din parametrul What-If. Al doilea argument (`0`) este valoarea implicită returnată când nicio valoare nu este selectată.

---

**9. `'Progres Training (%)'`**
```dax
'Progres Training (%)' =
DIVIDE(
    COUNTROWS(FILTER('date_angajati', 'date_angajati'[Training_Ore] >= 15)),
    COUNTROWS('date_angajati'),
    0
)
```
Procentul angajaților care au parcurs cel puțin 15 ore de training lunar. Pragul de 15 ore reprezintă o limită minimă de participare activă la programe de formare. Afișat ca procent cu o zecimală în card KPI.

---

## 6. STRUCTURA RAPORTULUI — CELE 15 PAGINI

### Pagina 1: Meniu Principal
**Dimensiuni:** 1400 × 1000 px | **Rol:** Pagină de start și navigare centralizată

Pagina de start constituie centrul de comandă (*hub*) al întregului raport. Designul se bazează pe principiul *progressive disclosure* — utilizatorul vede mai întâi KPI-urile de nivel înalt, apoi alege secțiunea relevantă.

**Componente:**
- **Titlu principal:** „Sistem de Analiză a Performanței și Riscului (Strategic Hub)"
- **4 carduri KPI de ansamblu:**
  - Total Angajați → `Total_Angajati`
  - Scor Mediu → `AVERAGE(Scor_Performanta)`
  - Procent Risc → `Procent_Risc`
  - Progres Training → `Progres Training (%)`
- **3 secțiuni tematice** cu butoane de navigare:
  - **Analiză Strategică** → analize statistice avansate
  - **Management și HR** → dashboarduri operaționale
  - **Inteligență Artificială** → ML și simulări
- Butoane `pageNavigator` configurate cu acțiuni de navigare directă

---

### Pagina 2: Analiza Performanță HR *(pagina implicită la deschidere)*
**Dimensiuni:** 1280 × 1100 px | **Rol:** Dashboard principal HR — privire de ansamblu

Aceasta este pagina cea mai frecvent accesată, concepută pentru utilizatorul de tip manager HR care dorește o imagine completă a stării organizației la un moment dat.

**Componente:**
- **Slicer Dată** (dropdown) — filtrare pe lună/an; permite compararea lunilor individuale
- **Grafic donut — Distribuția Status_Risc:**
  - Segment roșu (#FB0B1D): Risc Ridicat
  - Segment albastru: Stabil
  - Segment verde: Potential
  - Afișează procentul fiecărei categorii
- **Grafic pie — Structura pe Senioritate:** proporția Junior / Mid / Senior
- **2 carduri KPI:** Total Angajați + Scor Mediu
- **Vizualizare Python — Matrice de Corelație:**
  - Biblioteci: `matplotlib`, `seaborn`, `pandas`
  - Câmpuri utilizate: `Ore_Lucrate`, `Proiecte_Finalizate`, `Feedback_Clienti`, `Scor_Performanta`, `Risc_Plecare_Scor`
  - Metodă: `seaborn.heatmap()` cu `annot=True` (valorile coeficienților afișate în celule)
  - Colormap: `coolwarm` (albastru = corelație negativă, roșu = corelație pozitivă)
  - Scală: de la -1 la +1 (coeficienți Pearson)
  - Titlu: „Matricea de Corelație (Factori de Influență)"
- Buton **Back** pentru navigare la meniu

**Relevanță academică:** Matricea de corelație este un instrument standard din statistica descriptivă multivariată. Permite identificarea rapidă a relațiilor liniare între variabile și detectarea multicolinearității — informație esențială pentru interpretarea modelelor de regresie aplicate ulterior.

---

### Pagina 3: Suport Decizional — Dashboard de Analiză Predictivă
**Dimensiuni:** 1280 × 900 px | **Rol:** Sistem de Suport Decizional (DSS) bazat pe Machine Learning predictiv

Aceasta este pagina cu cel mai înalt grad de sofisticare analitică din întregul raport. Dacă paginile anterioare descriu *ce se întâmplă* și *ce s-a întâmplat*, această pagină răspunde la întrebarea *ce urmează să se întâmple* — trecând de la analiza descriptivă la cea **predictivă**. Arhitectura sa este structurată pe trei paliere de analiză complementare, de la viziunea de ansamblu la intervenția individualizată.

---

#### Palierul 1: Analiza Macro — Cardul „Risc Mediu Procentual"

**Tip vizualizare:** Card KPI  
**Valoare exemplu afișată:** 56,35%  
**Sursă calcul:** Media probabilităților individuale de risc calculate prin algoritmul **Random Forest**

Cardul funcționează ca un **barometru organizațional**: o singură cifră care surprinde starea de sănătate a întregii forțe de muncă la momentul curent. Valoarea de 56,35% semnifică faptul că, în medie, un angajat din organizație are o probabilitate de peste jumătate de a se afla în zona de vulnerabilitate.

**Interpretare managerială:**

| Interval valoare | Interpretare | Acțiune recomandată |
|---|---|---|
| < 30% | Organizație stabilă | Monitorizare periodică |
| 30% – 50% | Risc moderat | Intervenții selective |
| > 50% | Alertă organizațională | Politici de retenție la nivel global |

Spre deosebire de `Procent_Risc` (măsura DAX din alte pagini, care numără categorii pre-calculate), acest card utilizează probabilități continue generate de modelul Random Forest — o estimare mai nuanțată și mai precisă.

**Algoritmul Random Forest — context:**  
Random Forest este un algoritm de Machine Learning supervizat de tip *ensemble* care construiește un număr mare de arbori de decizie independenți și combină predicțiile lor prin votul majorității (clasificare) sau medie (regresie). Avantajele față de un singur arbore de decizie includ: rezistența la supraadaptare (*overfitting*), stabilitate crescută și capacitatea de a estima importanța fiecărei variabile.

---

#### Palierul 2: Analiza Factorială — Vizualul „Key Influencers"

**Tip vizualizare:** Key Influencers (vizualizare AI nativă Power BI)  
**Rol:** Identificarea automată a cauzelor care cresc riscul de burnout

Vizualul **Key Influencers** este una dintre componentele de Inteligență Artificială construite nativ în Power BI. Spre deosebire de toate celelalte vizualizări care prezintă *ce* se întâmplă, Key Influencers explică *de ce* — realizând automat o analiză cauzală bazată pe modele statistice de regresie și clasificare internă.

**Funcționarea internă:**  
Power BI analizează toate variabilele disponibile și calculează care dintre ele, și în ce direcție, contribuie cel mai mult la creșterea variabilei țintă (riscul de burnout/plecare). Rezultatele sunt prezentate ca factori ordonați descrescător după puterea de influență, cu explicații în limbaj natural.

**Factori critici identificați în proiect:**

| Factor | Direcție influență | Interpretare |
|---|---|---|
| `Feedback_Clienti` scăzut | Crește riscul | Angajații cu feedback slab de la clienți sunt dezangajați și frustrați |
| `Ore_Lucrate` ridicate | Crește riscul | Supraîncărcarea cronică este un predictor direct al burnout-ului |
| `Training_Ore` ridicate | Scade riscul | Investiția în dezvoltare profesională crește satisfacția și retenția |

**Valoarea managerială:** Managerul nu primește doar o alertă că există o problemă, ci are identificate exact pârghiile de intervenție — *ce anume* trebuie îmbunătățit pentru a reduce riscul. Aceasta transformă dashboard-ul dintr-un instrument de raportare într-un instrument de **decizie acționabilă**.

---

#### Palierul 3: Analiza Micro — Tabelul „Top 5 Angajați la Risc"

**Tip vizualizare:** Tabel filtrat și sortat  
**Rol:** Prioritizarea intervențiilor HR la nivel individual

Ultimul palier coboară de la nivel organizațional la nivel de persoană. Tabelul prezintă cele mai critice 5 cazuri din organizație la momentul curent, permițând HR-ului să aloce resursele de intervenție (conversații 1-la-1, reducere ore, training urgent) exact acolo unde impactul este maxim.

**Logica de construire a listei:**

1. **Filtrul principal:** Se iau toți angajații cu `Status_Risc = "Risc Ridicat"` sau cu probabilitate Random Forest > prag definit
2. **Ordonare primară:** Descrescător după probabilitatea de risc (angajatul cu cel mai mare risc — primul)
3. **Tie-breaking (factor de departajare):** La probabilități egale, angajatul cu mai multe `Ore_Lucrate` este prioritizat — combinând riscul *psihologic* cu supraîncărcarea *fizică*

**Coloane afișate în tabel:**

| Coloană | Semnificație pentru manager |
|---|---|
| `ID_Angajat` | Identificatorul — managerul știe exact cu cine să discute |
| `Probabilitate Risc (%)` | Cât de urgentă este intervenția |
| `Ore_Lucrate` | Gradul de suprasolicitare fizică |
| `Feedback_Clienti` | Indicatorul dezangajării profesionale |
| `Departament` | Permite direcționarea intervenției către managerul direct |

**Eficiență decizională:** În loc să analizeze manual toate cele 200 de înregistrări lunare, managerul HR primește un **top 5 acționabil** în câteva secunde.

---

#### Semnificația metodologică a paginii

Pagina de Suport Decizional marchează **trecerea de la HR Reactiv la HR Predictiv/Proactiv**:

| Tip HR | Caracteristică | Când acționează |
|---|---|---|
| **HR Reactiv** (tradițional) | Observă și înregistrează plecarile | *După* ce angajatul a demisionat |
| **HR Proactiv** (descriptiv) | Monitorizează indicatori de risc | Când riscul este deja vizibil |
| **HR Predictiv** (această pagină) | Calculează probabilitatea de plecare | *Înainte* ca angajatul să conștientizeze că vrea să plece |

Prin combinarea celor trei paliere de analiză — Macro (starea organizației), Factorial (cauzele) și Micro (cazurile individuale) — pagina implementează complet conceptul de **Sistem de Suport Decizional (Decision Support System, DSS)** definit în literatura de specialitate ca un sistem informatic care combină modele analitice cu date organizaționale pentru a sprijini procesul de luare a deciziilor manageriale.

---

### Pagina 4: Distribuția Geografică
**Dimensiuni:** 1280 × 1000 px | **Rol:** Analiză geografică a forței de muncă

**Componente:**
- **Hartă Azure Maps** — bule proporționale pe harta României:
  - Câmp Locație: `Oras`
  - Câmp Serie (culoare): `Departament`
  - Dimensiunea bulei: proporțională cu numărul de angajați
  - Centru hartă: 45.69°N, 24.94°E (centrul geografic al României)
  - Nivel zoom: 5.35 (vizualizare la nivel național)
- **Grafic bare orizontale** — Top orașe după scorul mediu de performanță, sortat descrescător
- **Card KPI** — Total Angajați (stilizat cu fundal #07452B — verde corporate)
- **Slicer Manager** (dropdown) — filtrare după manager direct

**Relevanță:** Analiza geografică ajută la identificarea disparităților de performanță între locații — informație critică pentru decizii de expansiune, redistribuire a resurselor sau programe de suport regional.

---

### Pagina 5: Evoluția Performanței Medii
**Dimensiuni:** 1280 × 1100 px  
**Titlu:** „Evoluția Performanței Medii pe Manageri (2023)"  
**Rol:** Analiza tendințelor temporale pe 12 luni

**Componente:**
- **Slicer Manager** (dropdown) — selecție individuală sau multiplă de manageri
- **Grafic linii/trend** — axa X: Data (lunile anului 2023); axa Y: media `Scor_Performanta`
- Fiecare linie reprezintă un manager; compararea vizuală permite identificarea managerilor cu echipe în declin sau în creștere

**Relevanță:** Analiza temporală este esențială în HR analytics deoarece tendința (trend) contează mai mult decât valoarea punctuală. Un manager cu scor mediu în creștere constantă este mai valoros decât unul cu scor stabil dar mai mare.

---

### Pagina 6: Analiza Multivariată
**Dimensiuni:** 1280 × 900 px  
**Titlu:** „Analiză Multivariată: Corelații între Efort, Dezvoltare și Risc"  
**Rol:** Analiză statistică avansată a distribuției performanței

**Componente:**
- **Slicer Senioritate** (vertical, multi-select) — filtrare pe nivel de experiență
- **Vizualizare Python — Violin Plot:**
  - Biblioteci: `matplotlib`, `seaborn`
  - Câmpuri: `Departament`, `Scor_Performanta`, `Status_Risc`
  - Tip: `seaborn.violinplot()` cu `inner='quartile'` (liniile interioare arată cuartilele Q1, mediană, Q3)
  - Hue (culoare): `Status_Risc`
    - Stabil → Albastru (#3498db)
    - Risc Ridicat → Roșu (#e74c3c)
    - Potential → Verde (#27ae60)
  - Grupare: câte un violin per departament, defalcat pe categorii de risc
  - Titlu: „Analiza Detaliată: Performanță vs. Risc pe Departamente"

**Relevanță:** Violin plot-ul este superior box plot-ului clasic deoarece vizualizează forma completă a distribuției (nu doar quartilele), permitând detectarea distribuțiilor bimodale sau asimetrice — situații frecvente în datele HR.

---

### Pagina 7: Analiza Statistică
**Dimensiuni:** 1280 × 1100 px | **Rol:** Analiză statistică descriptivă per oraș

**Componente:**
- **Vizualizare Python** — distribuție statistică (box plot sau violin plot) pe departamente, filtrate pe locație
- **Slicer Oraș** — filtrare geografică pentru comparație între locații
- Câmpuri: `Departament`, `Scor_Performanta`, `Status_Risc`

**Scopul paginii:** Permite managementului regional să compare performanța departamentelor dintr-un anumit oraș față de media națională.

---

### Pagina 8: Analiza Comparativă (Importanța Factorilor — AI)
**Dimensiuni:** 1280 × 850 px  
**Titlu:** „Impactul Factorilor asupra Performanței (AI)"  
**Rol:** Identificarea, prin machine learning, a factorilor cu cel mai mare impact

**Componente:**
- **Vizualizare Python — Regresie Liniară:**
  - Biblioteci: `sklearn.linear_model.LinearRegression`, `matplotlib`
  - Câmpuri input (features): `Ore_Lucrate`, `Training_Ore`, `Feedback_Clienti`
  - Câmp target (variabila dependentă): `Scor_Performanta`
  - Algoritm: model liniar antrenat pe datele filtrate, coeficienții modelului sunt extrași ca măsuri ale „puterii de influență"
  - Vizualizare: grafic cu bare orizontale, câte o bară per factor, lungimea proporțională cu coeficientul
  - Axa X: „Puterea de Influență (coeficient regresie)"
  - Axa Y: numele factorilor

**Relevanță academică:** Regresia liniară multiplă este una dintre tehnicile fundamentale de Machine Learning supervizat. Coeficienții modelului sunt direct interpretabili în contextul HR: un coeficient mare pentru `Feedback_Clienti` înseamnă că satisfacția clienților are cea mai mare influență asupra scorului de performanță.

**Notă metodologică:** Întrucât variabilele input au scări diferite (orele au valori 0–260, feedback-ul 1–5), coeficienții bruti nu sunt direct comparabili. Standardizarea (scalarea la media 0 și deviație standard 1) ar fi necesară pentru comparabilitate strictă — această limitare poate fi menționată în lucrare ca direcție de îmbunătățire.

---

### Pagina 9: Evaluarea Eficienței
**Dimensiuni:** 1280 × 900 px  
**Rol:** Evaluarea eficienței individuale și pe departamente

Pagina prezintă raportul eficiență/efort — cât de mare este scorul de performanță obținut per oră lucrată, pe departamente și manageri.

---

### Pagina 10: K-Means Clustering (Machine Learning)
**Dimensiuni:** 1280 × 720 px (FitToPage)  
**Rol:** Segmentare automată a angajaților prin algoritm nesupervizat

**Componente:**
- **Vizualizare Python — K-Means:**
  - Bibliotecă: `sklearn.cluster.KMeans`, `matplotlib`
  - Features utilizate: `Scor_Performanta`, `Ore_Lucrate`, `Training_Ore`, `Risc_Plecare_Scor`
  - Număr clustere: K = 3 (ales pentru a corespunde conceptual celor 3 categorii de risc)
  - Vizualizare: scatter plot 2D (de obicei `Scor_Performanta` vs. `Ore_Lucrate`) cu punctele colorate după cluster
  - Centroizii clusterelor marcați distinct

**Algoritmul K-Means — descriere:**  
K-Means este un algoritm iterativ de clasificare nesupervizată care grupează observațiile în K clustere, minimizând suma pătratelor distanțelor euclidiene față de centrul (centroidul) fiecărui cluster. Algoritmul:
1. Inițializează K centroizi aleator
2. Atribuie fiecare punct celui mai apropiat centroid
3. Recalculează centroizii ca medie a punctelor din cluster
4. Repetă pașii 2–3 până la convergență

**Relevanță:** Spre deosebire de clasificarea bazată pe reguli (Status_Risc), K-Means descoperă structuri *neexplicite* din date, potențial identificând tipare neanticipate de angajați. Compararea clusterelor K-Means cu categoriile Status_Risc validează sau infirmă logica de clasificare manuală.

---

### Pagina 11: Simulare Impact Training asupra Riscului
**Dimensiuni:** 1280 × 720 px (FitToPage)  
**Rol:** Analiză What-If — impactul orelor de training asupra riscului de plecare

**Componente:**
- **Slicer parametric** (slider) — ore training simulate: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
- **Vizualizare** — grafic care arată cum se modifică `Risc_Plecare_Scor` mediu și distribuția `Status_Risc` în funcție de valoarea selectată
- Măsuri utilizate: `Scor_Estimat`, `Castig_Puncte`, `Simulare_Training Value`

---

### Pagina 12: Simulare Impact Training (Performanță)
**Dimensiuni:** 1280 × 720 px (FitToPage)  
**Rol:** Scenariu alternativ de simulare — impactul training-ului pe performanță

**Componente:**
- Parametru What-If `Simulare_Training` (slicer)
- **Card**: Scor Estimat (`Scor_Estimat`)
- **Card**: Câștig de Puncte (`Castig_Puncte`)
- **Grafic comparativ**: scorul curent vs. scorul estimat post-training, vizualizat ca bare sau indicatoare de progres

**Interpretare practică:** Dacă scorul mediu curent este 240 de puncte și se simulează 20 de ore de training suplimentar, `Castig_Puncte = 20 × 0.5 = 10`, deci scorul estimat devine 250. Aceasta permite managementului să justifice bugetele de training cu date concrete.

---

### Pagina 13: Analiza Performanței Individuale
**Dimensiuni:** 1280 × 900 px  
**Rol:** Drill-down la nivel de angajat — profil complet individual

**Componente:**
- **Selector de angajat** (visual ID: `ed42ff146945e8d0d233`) — lista cu toți angajații, funcționează ca filtru master
- **Grafic detalii individual** (visual ID: `9a32d2bd5dcc939ad390`) — afișează datele lunare pentru angajatul selectat
- Interacțiune de tip `DataFilter` configurată explicit între cele două vizualizări
- Posibilă includere: grafic de evoluție lunară a scorului, comparație față de medie, distribuția riscului per lună

**Relevanță:** Analiza individuală este esențială în procesele de evaluare anuală (performance review) și permite managerilor să aibă conversații bazate pe date cu angajații.

---

### Pagina 14: Rezumat Strategic
**Dimensiuni:** 1280 × 1000 px | **Rol:** Sinteză executivă pentru top management

Pagina consolidează cele mai importante concluzii din toate analizele precedente:
- Departamentul cu cel mai mare risc (`Dept_Burnout`)
- Managerul cu cea mai bună evoluție a echipei
- Procentul global de risc (`Procent_Risc`)
- Progresul programelor de training (`Progres Training (%)`)
- Identificarea clusterelor K-Means cu caracteristicile lor principale

Destinat prezentărilor executive, unde timpul este limitat și claritatea mesajului este prioritară.

---

### Pagina 15: Priorități și Recomandări
**Dimensiuni:** 1280 × 850 px | **Rol:** Concluzii acționabile și planul de măsuri

Pagina transformă datele în acțiuni concrete:
- Lista departamentelor/echipelor care necesită intervenție imediată
- Recomandări specifice bazate pe analizele anterioare (ex: „creșterea orelor de training pentru angajații din cluster 2 ar reduce riscul cu X%")
- Priorități ordonate după urgență și impact
- Buton de navigare înapoi la meniu

---

---

## 7. COMPONENTE DE MACHINE LEARNING ȘI STATISTICĂ AVANSATĂ

### 7.1 Integrarea Python în Power BI

Power BI permite rularea scripturilor Python atât în **Power Query** (la etapa de transformare a datelor) cât și ca **vizualizări Python** (*Python Visual*) — grafice generate de Python afișate direct în dashboard.

**Fluxul de execuție al unui Python Visual:**
1. Power BI aplică filtrele active și transmite un DataFrame pandas vizualizării Python
2. Scriptul Python primește datele ca variabila `dataset` (DataFrame pandas)
3. Scriptul generează un grafic matplotlib/seaborn
4. Graficul este capturat și afișat în vizualizarea Power BI

**Limitări tehnice de știut:**
- Scriptul Python se execută la fiecare actualizare de filtru
- Stateful computing nu este suportat între execuții
- Vizualizările Python nu suportă tooltip-urile native Power BI
- Este necesară instalarea locală a Python și a bibliotecilor necesare

### 7.2 Matricea de Corelație (Pagina 2)

**Tehnică:** Corelație Pearson  
**Implementare:** `seaborn.heatmap(df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)`

Coeficientul de corelație Pearson $r$ pentru două variabile $X$ și $Y$ este:

$$r_{XY} = \frac{\sum_{i=1}^{n}(X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n}(X_i - \bar{X})^2 \cdot \sum_{i=1}^{n}(Y_i - \bar{Y})^2}}$$

Valorile $r \in [-1, 1]$ unde:
- $r = 1$: corelație pozitivă perfectă
- $r = 0$: nicio corelație liniară
- $r = -1$: corelație negativă perfectă

### 7.3 Violin Plot — Distribuție Multivariată (Paginile 5, 6)

Violin plot-ul combină **box plot** (quartile, outlieri) cu **kernel density estimation (KDE)** pentru a arăta forma completă a distribuției.

**Avantaj față de box plot:** Un box plot arată doar Q1, mediană, Q3 și outlieri — pierde informații despre forma distribuției (bimodalitate, asimetrie). Violin plot-ul arată densitatea completă.

**Implementare:**
```python
import seaborn as sns
sns.violinplot(
    data=dataset,
    x='Departament',
    y='Scor_Performanta',
    hue='Status_Risc',
    inner='quartile',
    palette={'Stabil': '#3498db', 'Risc Ridicat': '#e74c3c', 'Potential': '#27ae60'}
)
```

### 7.4 Regresia Liniară Multiplă (Pagina 7)

**Modelul:** $\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 + \varepsilon$

unde:
- $\hat{y}$ = `Scor_Performanta` (estimat)
- $x_1$ = `Ore_Lucrate`
- $x_2$ = `Training_Ore`
- $x_3$ = `Feedback_Clienti`
- $\beta_i$ = coeficienți (estimați prin metoda celor mai mici pătrate)
- $\varepsilon$ = termen de eroare

**Implementare scikit-learn:**
```python
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

features = ['Ore_Lucrate', 'Training_Ore', 'Feedback_Clienti']
X = dataset[features]
y = dataset['Scor_Performanta']

model = LinearRegression()
model.fit(X, y)

coefs = pd.Series(model.coef_, index=features)
coefs.sort_values().plot(kind='barh')
plt.xlabel('Puterea de Influență')
plt.title('Impactul Factorilor asupra Performanței (AI)')
```

**Coeficienți așteptați** (conform formulei de generare a datelor):
- `Proiecte_Finalizate`: ~10 (cel mai mare impact)
- `Feedback_Clienti`: ~20 (impact mare — dar scala 1–5 înmulțită cu 20)
- `Ore_Lucrate`: ~0.5 (impact moderat)

### 7.5 K-Means Clustering (Pagina 9)

**Algoritmul K-Means minimizează funcția obiectiv:**

$$J = \sum_{j=1}^{K} \sum_{x_i \in C_j} ||x_i - \mu_j||^2$$

unde $\mu_j$ este centroidul clusterului $C_j$.

**Implementare:**
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

features = ['Scor_Performanta', 'Ore_Lucrate', 'Training_Ore', 'Risc_Plecare_Scor']
X = dataset[features].dropna()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

plt.scatter(X['Scor_Performanta'], X['Ore_Lucrate'],
            c=labels, cmap='viridis', alpha=0.6)
plt.xlabel('Scor Performanță')
plt.ylabel('Ore Lucrate')
plt.title('K-Means Clustering — Segmentare Angajați')
```

**Notă:** Standardizarea (`StandardScaler`) este obligatorie înainte de K-Means, deoarece variabilele cu scale diferite (ex: `Ore_Lucrate` în sute vs. `Risc_Plecare_Scor` în [0,1]) ar domina distanța euclidiană fără normalizare.

---

## 8. SIMULĂRI WHAT-IF

### 8.1 Conceptul de analiză What-If în BI

Analiza What-If (*ce s-ar întâmpla dacă?*) permite utilizatorilor să exploreze scenarii ipotetice modificând parametri controlabili și observând impactul estimat asupra indicatorilor de interes. Este un instrument de planificare și decizie esențial în BI.

### 8.2 Implementarea în Power BI

**Tabelul parametric:**
```dax
Simulare_Training = GENERATESERIES(0, 50, 5)
-- Generează: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
```

**Slicer interactiv:** Utilizatorul selectează numărul de ore de training suplimentar din lista generată. Selecția actualizează imediat toate măsurile care referă `SELECTEDVALUE('Simulare_Training'[Simulare_Training])`.

**Lanțul de calcul:**
1. Utilizator selectează 20 de ore → `Simulare_Training Value = 20`
2. `Scor_Estimat = AVERAGE(Scor_Performanta) + (20 × 0.5) = medie + 10`
3. `Castig_Puncte = 10 puncte`
4. Cardurile și graficele se actualizează automat

### 8.3 Limitări ale simulării

Simularea implementată este lineară și deterministă — presupune că impactul training-ului este uniform pentru toți angajații și că relația este strict liniară. În realitate, efectele training-ului sunt nelineare (randament descrescător, diferențe individuale). Aceasta este o limitare asumată pentru simplitatea modelului academic.

---

## 9. TEHNOLOGII ȘI INSTRUMENTE UTILIZATE

| Tehnologie / Bibliotecă | Versiune recomandată | Utilizare în proiect |
|---|---|---|
| **Python** | 3.9+ | Runtime pentru vizualizări ML și statistică |
| **pandas** | 1.5+ | Manipularea DataFrame-urilor; generarea CSV; transformări date |
| **numpy** | 1.23+ | Generarea datelor aleatorii; calcule vectorizate |
| **matplotlib** | 3.6+ | Grafice personalizate: bare, scatter, heatmap |
| **seaborn** | 0.12+ | Violin plots, heatmap corelație cu stil statistic |
| **scikit-learn** | 1.1+ | LinearRegression (importanță factori); KMeans (clustering); RandomForestClassifier (predicție risc) |
| **Microsoft Power BI Desktop** | Feb 2024+ | Platformă principală de BI și vizualizare |
| **Format PBIP** | — | Format proiect Power BI editabil în Git (JSON) |
| **DAX** | — | Limbaj de calcul pentru măsuri și tabele calculate |
| **Power Query (M)** | — | Transformarea și importul datelor din CSV |
| **Azure Maps** | — | Harta interactivă România cu bule geografice |
| **Key Influencers (Power BI AI)** | — | Analiză cauzală automată — explică factorii care cresc riscul de burnout |
| **GENERATESERIES (DAX)** | — | Tabel parametric pentru simulări What-If |

---

## 10. FUNCȚIONALITĂȚI CHEIE ALE SISTEMULUI

### 10.1 Monitorizare KPI în timp real
- **Total angajați** (distinctivi, sensibil la filtre de departament/manager)
- **Scor mediu de performanță** (comparabil între departamente și luni)
- **Procent risc de plecare** (indicator de alertă pentru management)
- **Progres program de training** (% angajați cu ≥15h/lună)

### 10.2 Clasificarea Riscului de Fluctuație (Turnover Risk)
Sistem pe 3 niveluri care clasifică fiecare angajat lunar:

| Categorie | Semnificație | Culoare cod |
|---|---|---|
| **Risc Ridicat** | Supraîncărcat + feedback slab → probabilitate mare de plecare | Roșu #FB0B1D |
| **Stabil** | Performanță normală, niciun semn de risc | Albastru/Gri |
| **Potential** | Scor înalt, risc scăzut → candidat pentru promovare | Verde |

### 10.3 Analiză Statistică Multivariată
- **Matricea de corelație Pearson** — 5 variabile × 5 variabile
- **Violin plots** cu defalcare pe departamente și categorii de risc
- **Box plots** pentru distribuții statistice descriptive

### 10.4 Machine Learning Integrat în BI
- **Regresia liniară** — identifică și cuantifică impactul fiecărui factor
- **K-Means clustering** — segmentare automată în 3 profiluri de angajați, fără etichetare manuală
- **Random Forest** — model predictiv supervizat care calculează probabilitatea individuală de risc; utilizat în pagina de Suport Decizional
- **Key Influencers (AI nativ Power BI)** — analiză cauzală automată care identifică și explică factorii care cresc riscul de burnout

### 10.5 Simulări What-If
- Interval: 0–50 ore training suplimentar, pas de 5 ore
- Estimare automată a scorului post-training
- Vizualizarea impactului asupra riscului de plecare

### 10.6 Analiză Geografică
- Harta Azure Maps cu bule proportionale per oraș
- Colorare pe departamente pentru vizualizarea concentrației organizaționale
- Grafic complementar: top orașe după scorul mediu

### 10.7 Navigare și Interactivitate
- Sistem de navigare cu butoane `pageNavigator`
- Butoane Back pe fiecare pagină analitică
- Slicere contextuale: Dată, Manager, Departament, Oraș, Senioritate
- Filtrare cross-vizual (click → filtrare automată a altor vizualizări de pe pagină)
- Interacțiune DataFilter configurată explicit (pagina 12)

---

## 11. FLUXUL DE NAVIGARE

```
┌─────────────────────────────────────────────┐
│          MENIU PRINCIPAL (Start)            │
│  KPI: Total Angajați | Scor Mediu |         │
│        Procent Risc | Progres Training      │
└──────────────┬──────────────────────────────┘
               │
    ┌──────────┼───────────────┐
    │          │               │
    ▼          ▼               ▼
┌───────┐  ┌──────────┐  ┌────────────────────┐
│ANALIZĂ│  │MANAGEMENT│  │INTELIGENȚĂ         │
│STRAT. │  │ȘI HR     │  │ARTIFICIALĂ         │
└───┬───┘  └────┬─────┘  └─────────┬──────────┘
    │           │                   │
    ├─ P6: Analiză Multivariată     ├─ P10: K-Means Clustering
    ├─ P7: Analiză Statistică       ├─ P11: Simulare Training → Risc
    ├─ P8: Analiză Comparativă      └─ P12: Simulare Training → Perf.
    └─ P5: Evoluție Performanță
                │
                ├─ P2: Analiza Perf. HR (default)
                ├─ P3: Suport Decizional (DSS Predictiv)
                ├─ P4: Distribuție Geografică
                ├─ P9: Evaluarea Eficienței
                ├─ P13: Analiză Individuală
                ├─ P14: Rezumat Strategic
                └─ P15: Priorități și Recomandări
```

---

## 12. STRUCTURA FIȘIERELOR PROIECTULUI

```
d:\licenta_vs\
│
├── licenta_sonia.pbip                     ← Fișier principal proiect Power BI
│
├── licenta_sonia.Report\
│   ├── definition\
│   │   ├── report.json                    ← Configurare globală: temă, setări, metadata
│   │   ├── version.json                   ← Versiunea schemei (3.2.0)
│   │   └── pages\
│   │       ├── pages.json                 ← Ordinea și metadatele tuturor paginilor
│   │       │
│   │       ├── 45f820c...\                ← P1: Meniu principal
│   │       │   └── page.json
│   │       ├── 6823215...\                ← P2: Analiza performanta HR (default)
│   │       ├── [hash_dss]...\             ← P3: Suport Decizional (DSS Predictiv)
│   │       ├── 15270d9...\                ← P4: Distributia Geografica
│   │       ├── 26c0fbf...\                ← P5: Evolutia Performantei Medii
│   │       ├── 4853b6a...\                ← P6: Analiza Multivariata
│   │       ├── 435713b...\                ← P7: Analiza Statistica
│   │       ├── 7fafe91...\                ← P8: Analiza Comparativa (Regresie)
│   │       ├── b022d4c...\                ← P9: Evaluarea Eficientei
│   │       ├── 47616fd...\                ← P10: K-Means Clustering
│   │       ├── 0434515...\                ← P11: Simulare Impact Training → Risc
│   │       ├── e01ede0...\                ← P12: Simulare Impact Training → Perf.
│   │       ├── 4bf5c8d...\                ← P13: Analiza performantei individuale
│   │       ├── d4c7bac...\                ← P14: Rezumat Strategic
│   │       └── d441d97...\                ← P15: Prioritati si Recomandari
│   │
│   └── StaticResources\                   ← Resurse statice (imagini, fonturi custom)
│
├── licenta_sonia.SemanticModel\
│   └── definition\
│       ├── model.tmdl                     ← Configurare model semantic (TMDL format)
│       ├── database.tmdl                  ← Configurare bază de date
│       ├── relationships.tmdl             ← Relații între tabele
│       └── tables\
│           ├── date_angajati.tmdl         ← Definiție tabel principal + măsuri DAX
│           ├── Simulare_Training.tmdl     ← Definiție tabel parametric What-If
│           ├── LocalDateTable_....tmdl    ← Tabel de date (sistem, ascuns)
│           └── DateTableTemplate_....tmdl ← Șablon dată (sistem, ascuns)
│
└── DOCUMENTATIE_LICENTA.md                ← Acest fișier de documentație
```

**Notă despre formatul PBIP:**  
Formatul PBIP (*Power BI Project*) este formatul modern de proiect Power BI, introdus pentru a facilita integrarea cu sisteme de versionare (Git). Spre deosebire de formatul clasic `.pbix` (fișier binar), PBIP stochează toate componentele ca fișiere JSON/TMDL text, permițând urmărirea modificărilor, code review și colaborare în echipă.

---

## 13. CONFIGURARE TEHNICĂ RAPORT

| Parametru | Valoare |
|---|---|
| Versiune schemă | 3.2.0 |
| Temă vizuală | CY25SU12 (Microsoft Power BI Modern Theme) |
| Nivel compatibilitate model semantic | 1600 (Power BI Premium) |
| Visual personalizat inclus | Text Filter |
| Mod export date | Rezumat (Summarized) |
| Drill filter cross-visual | Activat |
| Tooltip îmbunătățit | Activat |
| Dimensiune canvas pagini standard | 1280 × 720 px sau 1280 × 900 px sau 1280 × 1100 px |
| Dimensiune canvas meniu principal | 1400 × 1000 px |
| Limbă raport | ro-RO (Română) |
| Encoding CSV sursă | Windows-1250 |
| Mod de conectare la date | Import (cache local) |

---

## 14. CONTRIBUȚII ACADEMICE ȘI CONCLUZII

### 14.1 Contribuțiile proiectului

Proiectul aduce următoarele contribuții în domeniul Business Intelligence aplicat în HR:

1. **Sistem complet integrat BI + ML:** Demonstrează că o platformă BI accesibilă (Power BI) poate fi extinsă cu capabilități de Machine Learning (sklearn, Random Forest) prin integrarea Python, fără a necesita platforme ML dedicate costisitoare

2. **Model de clasificare a riscului explicabil:** Sistemul de clasificare în 3 categorii (Risc Ridicat, Stabil, Potential) este bazat pe reguli de business transparente și auditabile — o alternativă *white-box* față de modelele ML *black-box*

3. **Sistem de Suport Decizional (DSS) pe trei paliere:** Pagina de Suport Decizional implementează un DSS complet — de la barometrul organizațional (Risc Mediu Procentual via Random Forest), la analiza cauzală (Key Influencers AI), până la lista de intervenție individualizată (Top 5 Angajați). Aceasta concretizează tranziția de la HR Reactiv la HR Predictiv.

4. **Simulări What-If pentru decizie managerială:** Parametrul interactiv de training permite managerilor să cuantifice ROI-ul programelor de formare înainte de a aloca bugete

5. **Analiză multidimensională:** Integrarea analizei temporale, geografice, departamentale și individuale într-un sistem unic permite o viziune 360° asupra forței de muncă

6. **Validare încrucișată ML vs. reguli:** Compararea clusterelor K-Means cu categoriile bazate pe reguli, coroborată cu predicțiile Random Forest, oferă o metodă de validare a logicii de clasificare pe multiple niveluri

### 14.2 Limitări și direcții viitoare

**Limitări actuale:**
- Datele sunt sintetice și nu validează modelul pe date reale din organizații
- Relația training → performanță este modelată liniar (simplificare a realității)
- Nu sunt incluși factori contextuali importanți: satisfacția la locul de muncă, raportul salariat/piață, factori demografici
- Modelul de risc este binar (risc/nu risc) — un model probabilistic ar fi mai nuanțat

**Direcții de extindere:**
- Integrarea datelor reale dintr-un HRIS (*Human Resources Information System*)
- Implementarea unui model predictiv de tip clasificator (Random Forest, Gradient Boosting) pentru predicția riscului de plecare cu mai mulți factori
- Adăugarea unui modul de notificări automate (alertă email când un angajat intră în categoria „Risc Ridicat")
- Integrarea cu Power BI Service pentru acces web și actualizări automate de date
- Extinderea analizei geografice cu heatmaps de densitate

### 14.3 Concluzii finale

Proiectul demonstrează viabilitatea construirii unui sistem complet de People Analytics folosind exclusiv instrumente accesibile și disponibile pe scară largă: Python (gratuit, open-source) și Microsoft Power BI (disponibil în organizații prin licențe Microsoft 365). 

Sistemul implementat oferă departamentelor de HR un instrument concret pentru trecerea de la managementul intuitiv al resurselor umane la decizii bazate pe date (*data-driven HR*), contribuind la reducerea costurilor asociate fluctuației de personal și la optimizarea programelor de dezvoltare profesională.

---

*Document de documentație academică — Proiect licență — d:\licenta_vs\licenta_sonia*  
*Generare date: script Python cu numpy.random.seed(101) — reproductibil*  
*Ultima actualizare: Aprilie 2026*
