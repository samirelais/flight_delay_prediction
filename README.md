# Prédiction des Retards de Vols

## Description
Ce projet vise à développer un système de prédiction des retards et annulations de vols en utilisant diverses techniques de Machine Learning et de Deep Learning.

## Objectifs
- Prédire la probabilité de retard d'un vol
- Estimer la durée précise du retard
- Prédire les risques d'annulation
- Identifier et analyser les facteurs principaux influençant les retards/annulations

## Données
Dataset "Flight Delays and Cancellations" de Kaggle comprenant :
- **flights.csv** : Données détaillées des vols (horaires, retards, etc.)
- **airlines.csv** : Informations sur les compagnies aériennes
- **airports.csv** : Caractéristiques des aéroports

## Méthodologie
1. **Préparation des données**
   - Nettoyage et validation des données
   - Feature engineering avancé
   - Fusion intelligente des différentes sources
   - Traitement des valeurs manquantes

2. **Analyse exploratoire**
   - Distribution et patterns des retards
   - Analyse temporelle (horaire/journalière/saisonnière)
   - Impact des compagnies aériennes et aéroports
   - Visualisations interactives

3. **Modélisation**
   - **Classification** : Random Forest, XGBoost, LightGBM, SVM, Neural Networks
   - **Régression** : Linear/Ridge/Lasso, Gradient Boosting, Random Forest
   - **Séries Temporelles** : ARIMA/SARIMA, Prophet, LSTM, VAR
   - **Approches Hybrides** : Combinaison de modèles et stacking

## Features Importantes
- **Temporelles** : Heure, Jour, Mois, Saison, Jours fériés
- **Spatiales** : Aéroports (départ/arrivée), Routes aériennes
- **Historiques** : Retards précédents, Performances des compagnies

## Installation
```bash
# Créer un environnement virtuel
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Structure du Projet
```
flight_delay_prediction/
├── notebooks/          # Notebooks d'analyse
├── src/               # Code source
├── data/              # Données
└── reports/           # Rapports et figures
```

## Utilisation
1. Cloner le repository
2. Installer les dépendances
3. Exécuter les notebooks dans l'ordre numérique
4. Consulter les rapports pour les résultats

## Résultats
[En cours ^^]


## Données
Les fichiers de données ne sont pas inclus dans ce repository en raison de leur taille.

Pour obtenir les données :
1. Visitez [Flight Delays Dataset sur Kaggle](https://www.kaggle.com/datasets/usdot/flight-delays)
2. Téléchargez les fichiers CSV :
   - flights.csv
   - airlines.csv
   - airports.csv
3. Placez ces fichiers dans le dossier `data/raw/`

### flights.csv (données principales des vols) :

- Variables temporelles :

   YEAR, MONTH, DAY : Date du vol

   DAY_OF_WEEK : Jour de la semaine

   SCHEDULED_DEPARTURE, DEPARTURE_TIME : Heures de départ

   SCHEDULED_ARRIVAL, ARRIVAL_TIME : Heures d'arrivée


- Variables de retard :

   DEPARTURE_DELAY : Retard au départ en minutes

   ARRIVAL_DELAY : Retard à l'arrivée en minutes

   LATE_AIRCRAFT_DELAY, WEATHER_DELAY, etc. : Causes des retards


- Variables de vol :

   FLIGHT_NUMBER : Numéro du vol

   AIRLINE : Code de la compagnie aérienne

   ORIGIN_AIRPORT, DESTINATION_AIRPORT : Codes des aéroports

   DISTANCE : Distance en miles


### airlines.csv (informations compagnies) :

      IATA_CODE : Code unique de la compagnie (ex: AA, UA)

      AIRLINE : Nom complet de la compagnie

### airports.csv (informations aéroports) :

      IATA_CODE : Code unique de l'aéroport (ex: LAX, JFK)

      AIRPORT : Nom de l'aéroport

      CITY, STATE : Localisation

      LATITUDE, LONGITUDE : Coordonnées géographiques


## Contact
- **Nom** : Samir EL AISSAOUY
- **Email** : elaissaouy.samir12@gmail.com
- **LinkedIn** : www.linkedin.com/in/samir-el-aissaouy

## License
Ce projet est sous licence MIT

## Droits d'utilisation
© 2024 Samir EL AISSAOUY. Tous droits réservés.
- Ce code est partagé publiquement à des fins de démonstration et de portfolio
- La consultation et l'étude du code sont autorisées
- Toute modification, redistribution ou utilisation du code est strictement interdite sans autorisation écrite