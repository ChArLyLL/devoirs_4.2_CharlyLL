from scipy import constants
from typing import Final
ZÉRO_ABSOLU: Final = -constants.zero_Celsius
TRILLION: Final = constants.exa
température: float
température = float(input("Quel est le température de l'eau ? "))
if température < ZÉRO_ABSOLU:
    print(" Impossible , vérifiez la valeur saisie. ")
elif température < 0:
    print("Solide : Glace ")
elif température < 100:
    print("Liquide ")
elif température < 2200:
    print("Gaz avec moins de 3% d'atomes libres")
elif température < 12e3:
    print("Gaz avec très peu d'atomes libres")
elif température < 4 * TRILLION:
    print("Gaz ionisé (plasma) d'hydrogène et d'oxygène. ")
else:
    print("Ce n'est clairement plus de l'eau!")
