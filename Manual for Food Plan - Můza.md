
GPT vytvořil skript pro aktualizaci ingrediencí. Vyplnil jsem tak ceny pro Albert a rohlík. 
skript: update_ingredient_costs_simple

Další je i Výpočet pro položky níže. 
skript: fill_and_calculate_ingredients.py

## Ingredients



## 🧾 Vysvětlení a návrh naplnění atributů

### ✅ `BoughtCost` _(celková cena za nákup balení)_

- **Např.:** koupil jsi 500g těstovin za 34,90 Kč → `BoughtCost: 34.90`
    
- ✅ Hodí se, pokud **nepoužíváš jednotkové ceny z obchodu**, ale eviduješ konkrétní nákup.
    

### ✅ `BoughtSize` _(hmotnost nebo objem daného nákupu)_

- Formát: `500g`, `1kg`, `1l`, `3ks` – co odpovídá.
    
- Příklad: `BoughtSize: 500g`
    
- **Poznámka:** Lze kombinovat s `BoughtCost` → výpočet jednotkové ceny.
    

### ✅ `PortionSize` _(kolik typicky použiješ na jednu porci)_

- Např.: `80g`, `1ks`, `2pl` (polévkové lžíce), `50ml`
    
- Pomáhá pro výpočet `CostPerMeal` (viz níže)
    

### ✅ `PotentialMeals` _(kolik porcí lze připravit z daného balení)_

- Může být:
    
    - vypočteno jako `BoughtSize / PortionSize`
        
    - nebo zapsáno odhadem (např. 4 porce z jednoho květáku)
        

### ✅ `CostPerMeal` _(náklad na 1 porci)_

- Můžeš spočítat ze vzorce:

    `CostPerMeal = BoughtCost / PotentialMeals`

- nebo


    `CostPerMeal = jednotková cena * PortionSize`
    
    > Např. 1 vejce stojí 4 Kč → `CostPerMeal: 4`
    
## Recipe