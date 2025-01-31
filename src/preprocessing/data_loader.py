# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Définir le style des visualisations
plt.style.use('default')
sns.set_theme()
sns.set_palette("husl")

def load_data():
    try:
        # Chargement des données avec chemins directs
        flights_df = pd.read_csv('../../data/raw/flights.csv')
        airlines_df = pd.read_csv('../../data/raw/airlines.csv')
        airports_df = pd.read_csv('../../data/raw/airports.csv')
        return flights_df, airlines_df, airports_df
    except FileNotFoundError as e:
        print(f"Erreur de fichier: {str(e)}")
        return None, None, None
    except Exception as e:
        print(f"Une erreur s'est produite: {str(e)}")
        return None, None, None

def explore_data():
    # Charger les données
    flights_df, airlines_df, airports_df = load_data()
    
    if flights_df is not None:
        # Afficher les premières informations sur chaque dataset
        print("=== APERÇU DU DATASET DES VOLS ===")
        print(flights_df.head())
        print("\nInformations sur le dataset des vols:")
        print(flights_df.info())

        print("\n=== APERÇU DU DATASET DES COMPAGNIES AÉRIENNES ===")
        print(airlines_df.head())
        print("\nInformations sur le dataset des compagnies:")
        print(airlines_df.info())

        print("\n=== APERÇU DU DATASET DES AÉROPORTS ===")
        print(airports_df.head())
        print("\nInformations sur le dataset des aéroports:")
        print(airports_df.info())

        return flights_df, airlines_df, airports_df
    return None, None, None

# Création d'une fonction de sauvegarde
def save_verified_data(flights_df, airlines_df, airports_df):
    flights_df.to_csv('../../data/processed/verified_flights.csv', index=False)
    airlines_df.to_csv('../../data/processed/verified_airlines.csv', index=False)
    airports_df.to_csv('../../data/processed/verified_airports.csv', index=False)
if __name__ == "__main__":
    flights_df, airlines_df, airports_df = explore_data()
    # Vérification des dimensions
    print("Dimensions des datasets :")
    print(f"Vols : {flights_df.shape}")
    print(f"Compagnies : {airlines_df.shape}")
    print(f"Aéroports : {airports_df.shape}")

    # Vérification des valeurs manquantes
    print("\nValeurs manquantes dans le dataset des vols :")
    print(flights_df.isnull().sum())