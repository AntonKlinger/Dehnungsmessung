import pandas as pd
import matplotlib.pyplot as plt

# Liste der Dateipfade
csv_dateien = [
    'Aufgabe1DMS1.csv',
    'Aufgabe1DMS2.csv',
    'Aufgabe1DMS3.csv',
    'Aufgabe1DMS4.csv',
    'Aufgabe1DMS5.csv'
]

# Farben und Marker für unterschiedliche Plots
farben = ['blue', 'red', 'green', 'purple', 'orange']
marker = ['o', 'x', '^', 's', 'D']

# Initialisiere das Diagramm
plt.figure(figsize=(12, 8))

# Schleife durch alle Dateien
for i, csv_datei in enumerate(csv_dateien):
    try:
        # Datei einlesen
        df = pd.read_csv(csv_datei, sep=r'\s+', header=None)
        df.columns = ['Spalte1', 'Spalte2', 'Spalte3', 'Spalte4']
        
        # Daten der vierten Spalte plotten
        plt.plot(df.index, df['Spalte4'], marker=marker[i % len(marker)], 
                 linestyle='-', color=farben[i % len(farben)], label=f'Datei {i+1}')

    except FileNotFoundError:
        print(f"Die Datei '{csv_datei}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Verarbeiten von Datei '{csv_datei}': {e}")

# Diagramm konfigurieren
plt.title('Plot der vierten Spalte aus bis zu 10 Dateien', fontsize=16)
plt.xlabel('Index', fontsize=14)
plt.ylabel('Wert der vierten Spalte', fontsize=14)
plt.legend(title='Dateien', fontsize=10)
plt.grid(True)

# Diagramm anzeigen
plt.show()
