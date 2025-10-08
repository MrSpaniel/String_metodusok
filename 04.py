"""4️⃣ Szó cseréje másikra – ételrendelés módosítása
Feladat: A rendelésben az „alma” helyett cseréld „körtére”, ha a boltban nincs alma."""

rendeles = input("Mit rendelsz?")
uj_rendeles = rendeles.replace("alma", "körte")
print(f"A rendelésed módosítva: {uj_rendeles}")