

import math


def volumen1():
    länge = float(input("geben sie die länge des Zylinders an (in cm): "))
    radius = float(input("geben sie den Radius des Zylinders an (in cm): "))
    zylinder = math.pi * (radius**2) * länge
    print("Die Masse deines Bauteils, beträgt (in gramm ): ")
   
    return zylinder


def volumen2(): 
    länge = float(input("geben sie die länge des Rechtecks an (in cm): "))
    höhe = float(input("geben sie die höhe des Rehctecks an (in cm): "))
    breite = float(input("geben sie die Breite des Rechtecks an (in cm) : "))
    Quader = länge * höhe * breite
    print("Die Masse deines Bauteils, beträgt (in gramm ): ")

    return Quader

Materialien =   {
    "Stahl" : 7.85,
    "Aluminium" : 2.70,
    "Titan" : 4.50
}

Volumenkörper =  {

    "Zylinder ",
    "Quader "

}



print("Welches Material willst du für die Berechnung nutzen? (g/cm^3) ")
print(Materialien)
ausgewählte_materialien = input("")



print("Welches Volumen willst du für die Berchnung nutzen? " )
print(Volumenkörper)

ausgewählte_volumenkörper = input("")


if ausgewählte_volumenkörper == "Zylinder":
    print(volumen1() * Materialien[ausgewählte_materialien])

elif ausgewählte_volumenkörper == "Quader":
    print( volumen2() * Materialien[ausgewählte_materialien])



