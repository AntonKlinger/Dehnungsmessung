import pandas as pd
import matplotlib.pyplot as plt

# Liste der Dateipfade
csv_dateien = [
    'Aufgabe2viertel(1)0g.csv',
    'Aufgabe2viertel(1)55_33g.csv',
    'Aufgabe2viertel(1)87_04g.csv',
    'Aufgabe2viertel(1)142_10g.csv',
    'Aufgabe2viertel(1)193_46g.csv',
    'Aufgabe2viertel(1)250_00g.csv',
    'Aufgabe2viertel(1)290_81g.csv',
    'Aufgabe2viertel(1)347_47g.csv',
    'Aufgabe2viertel(1)380_12g.csv',
    'Aufgabe2viertel(1)416_72g.csv'
]

# Farben und Marker für unterschiedliche Plots
farben = ['blue', 'red', 'green', 'purple', 'orange', 'brown', 'pink', 'gray', 'cyan', 'magenta']
marker = ['o', 'x', '^', 's', 'D', '*', 'P', 'h', 'v', '>']

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
