# Strategic Hub — Sistem de Analiză a Performanței și Riscului Resurselor Umane

Dashboard Power BI de analiză predictivă a riscului de burnout / plecare a angajaților, cu Machine Learning integrat (Python) direct în raport: regresie liniară, K-Means clustering, simulări what-if.

Proiect de licență — toate datele folosite sunt **sintetice** (generate cu seed fix, fără date reale sau informații personale).

## Ce face proiectul

- Monitorizează performanța a 200 de angajați simulați, pe 12 luni (2023)
- Clasifică riscul de plecare (Stabil / Potential / Risc Ridicat) pe baza unor reguli de business
- Prezice probabilitatea de risc cu un model **Random Forest** antrenat direct în Power Query (Python)
- Segmentează angajații cu **K-Means Clustering** (Low / Core / Top performers)
- Identifică factorii determinanți ai performanței cu **regresie liniară**
- Simulează impactul orelor de training asupra scorului de performanță și riscului (what-if analysis)
- 15 pagini de raport, de la hub-ul de navigare până la un rezumat executiv cu priorități și recomandări

## Tehnologii

- **Power BI Desktop** (format PBIP — Power BI Project, text-based)
- **DAX** pentru măsuri (Scor_Estimat, Procent_Risc, Prag_Burnout etc.)
- **Python** (pandas, scikit-learn) — integrat ca vizualizări native și în Power Query pentru scoring ML
- **Power Query (M)** pentru ETL

## Structura repo-ului

```
licenta_sonia.Report/          # definiția raportului (pagini, vizuale) — format PBIP
licenta_sonia.SemanticModel/   # modelul semantic (tabele, măsuri DAX, relații) — format TMDL
licentavs.pbix                 # fișierul Power BI complet, gata de deschis în Power BI Desktop
data/
  generator_date.py            # scriptul care generează datele sintetice
  date_angajati_istoric.csv    # setul de date (2400 înregistrări: 200 angajați x 12 luni)
docs/                          # lucrarea de licență și prezentarea
DOCUMENTATIE_LICENTA.md        # documentația tehnică detaliată a proiectului
screenshots/                   # capturi ale celor 15 pagini ale raportului
```

## Paginile raportului

_(screenshot-uri și descrieri detaliate mai jos)_
