"""1️⃣ Kis- és nagybetűssé alakítás – névformázás
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
nagybetűs (pl. címkén vagy azonosítóban),


kisbetűs (pl. email összehasonlításhoz),


csak az első betű nagy (személyes üdvözlésnél).
"""

felhasznalonev = input("Kérlek add meg a felhasználóneved:")
nagybetus_szo = felhasznalonev.upper()
print(f"Csupa nagybetűs: {nagybetus_szo}")
kisbetus_szo = felhasznalonev.lower()
print(f"Csupa kisbetűs: {kisbetus_szo}")
elso_nagybetu = felhasznalonev.capitalize()
print(f"Első nmagybetű: {elso_nagybetu}")
