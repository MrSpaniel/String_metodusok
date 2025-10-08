"""2️⃣ Szóhossz meghatározása – tweet vagy SMS ellenőrzés
Feladat: Kérj be egy üzenetet a felhasználótól, majd írd ki, hány karakterből áll. Hasznos lehet például Twitter/SMS hosszkorlátozás ellenőrzéséhez.
"""

uzenet = input("Írd le az üzeneted:")
szam = len(uzenet)
print(f"Az üzenet hossza {szam} karakterből áll.")
