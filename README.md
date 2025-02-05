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

- Variables d'identification et de temps :


      YEAR : Année du vol
      MONTH : Mois du vol
      DAY : Jour du vol
      DAY_OF_WEEK : Jour de la semaine (1-7)
      FLIGHT_NUMBER : Numéro du vol
      TAIL_NUMBER : Numéro d'identification de l'avion


- Variables de compagnie et route :


      AIRLINE : Code IATA de la compagnie
      ORIGIN_AIRPORT : Code IATA de l'aéroport de départ
      DESTINATION_AIRPORT : Code IATA de l'aéroport d'arrivée
      DISTANCE : Distance en miles


- Variables d'horaires :


      SCHEDULED_DEPARTURE : Heure de départ prévue (format HHMM)
      DEPARTURE_TIME : Heure de départ réelle (format HHMM)
      DEPARTURE_DELAY : Retard au départ en minutes
      TAXI_OUT : Temps de roulage au départ en minutes
      WHEELS_OFF : Heure de décollage (format HHMM)
      SCHEDULED_TIME : Durée prévue du vol en minutes
      ELAPSED_TIME : Durée réelle du vol en minutes
      AIR_TIME : Temps en vol en minutes
      WHEELS_ON : Heure d'atterrissage (format HHMM)
      TAXI_IN : Temps de roulage à l'arrivée en minutes
      SCHEDULED_ARRIVAL : Heure d'arrivée prévue (format HHMM)
      ARRIVAL_TIME : Heure d'arrivée réelle (format HHMM)
      ARRIVAL_DELAY : Retard à l'arrivée en minutes


- Variables de retard par cause :


      CARRIER_DELAY : Retard dû à la compagnie en minutes
      WEATHER_DELAY : Retard dû à la météo en minutes
      NAS_DELAY : Retard dû au système national aérien en minutes
      SECURITY_DELAY : Retard dû à la sécurité en minutes
      LATE_AIRCRAFT_DELAY : Retard dû à un retard précédent de l'avion


- Variables d'état du vol :


      DIVERTED : Vol dérouté (1 = oui, 0 = non)
      CANCELLED : Vol annulé (1 = oui, 0 = non)
      CANCELLATION_REASON : Raison de l'annulation (A = compagnie, B = météo, C = NAS, D = sécurité)

### airlines.csv (informations compagnies) :

      IATA_CODE : Code unique de la compagnie (ex: AA, UA)

      AIRLINE : Nom complet de la compagnie

### airports.csv (informations aéroports) :

      IATA_CODE : Code unique de l'aéroport (ex: LAX, JFK)

      AIRPORT : Nom de l'aéroport

      CITY, STATE : Localisation

      LATITUDE, LONGITUDE : Coordonnées géographiques

### Relations entre les fichiers :
      flights.csv (AIRLINE) ←→ airlines.csv (IATA_CODE)

      flights.csv (ORIGIN_AIRPORT/DESTINATION_AIRPORT) ←→ airports.csv (IATA_CODE)
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