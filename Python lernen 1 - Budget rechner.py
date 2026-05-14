# 1. Gehalt abfragen

gehalt = float(input("geben sie ihr monatliches gehalt an: "))


# 2. Ausgaben sammeln (Das Dictionary)
ausgaben = {}

print("\n--- Ausgaben eintragen ---")

# Die Endlosschleife für beliebig viele Einträge
while True:
    name = input("Geben Sie den Namen Ihrer Ausgabe an (oder 'x' zum Beenden): ")
    
    # Die Notbremse
    if name == "x":
        break
        
    betrag = float(input("Geben Sie den Betrag in Euro an: "))
    
    # Das Paar in die Kiste legen
    ausgaben[name] = betrag 

# 3. Die Mathematik und Auswertung
print("\n--- Auswertung ---")
print("Deine Ausgaben sind also nun:", ausgaben)

# Alle Beträge aus der Kiste zusammenrechnen
gesamtausgaben = sum(ausgaben.values())
print("Deine Gesamtausgaben sind:", gesamtausgaben)

# Das restliche Geld berechnen
restbudget = gehalt - gesamtausgaben
print("Dein übriges Geld ist:", restbudget)

array = [gesamtausgaben, restbudget]

# 4. Ausgabe der Ergebnisse als diagramm
import matplotlib.pyplot as plt
labels = ['Ausgaben', 'Restbudget']
plt.pie(array, labels=labels, autopct='%1.1f%%')
plt.title('Ausgaben vs Restbudget')
plt.show()
