"""3️⃣ Szó keresése a szövegben – tartalom ellenőrzés
Feladat: Kérj be egy bejegyzést a közösségi oldalra, majd ellenőrizd, hogy szerepel-e benne a „Python” szó.
"""

szavacska = input("Írj be egy szöveget:")

szam = szavacska.count("python")

print(f"A Python szó {szam}-szor van benne a szövegedben.")