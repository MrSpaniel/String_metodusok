"""5️⃣ Szó elejének/végének ellenőrzése – email ellenőrzés
Feladat: Kérj be egy email címet a regisztrációhoz, majd ellenőrizd, hogy Gmail-es-e.
"""
email = input("Add meg az email címed:")
if email.endswith("@gmail.com"):
    print(f"Az email címed Gmail-es")

else :
   print("Ez nem Gmail!")