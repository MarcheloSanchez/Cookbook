
import os
import re

INGREDIENT_FOLDER = r"C:\Users\MarcelMachanec\Documents\Můza\Ingredients"

ingredient_data = {
    "Vejce": {
        "BoughtCost": "39.90",
        "BoughtSize": "10ks",
        "PortionSize": "1ks"
    },
    "Kuřecí maso": {
        "BoughtCost": "129.90",
        "BoughtSize": "1000g",
        "PortionSize": "150g"
    },
    "Mleté maso": {
        "BoughtCost": "159.90",
        "BoughtSize": "1000g",
        "PortionSize": "150g"
    },
    "Tvaroh tvrdý": {
        "BoughtCost": "34.90",
        "BoughtSize": "250g",
        "PortionSize": "125g"
    },
    "Tofu": {
        "BoughtCost": "29.90",
        "BoughtSize": "200g",
        "PortionSize": "100g"
    },
    "Šunka": {
        "BoughtCost": "24.90",
        "BoughtSize": "100g",
        "PortionSize": "50g"
    },
    "Plátkový sýr": {
        "BoughtCost": "22.90",
        "BoughtSize": "100g",
        "PortionSize": "30g"
    },
    "Tuňák v konzervě": {
        "BoughtCost": "49.90",
        "BoughtSize": "185g",
        "PortionSize": "90g"
    },
    "Losos": {
        "BoughtCost": "399.90",
        "BoughtSize": "1000g",
        "PortionSize": "150g"
    },
    "Bílý jogurt": {
        "BoughtCost": "22.90",
        "BoughtSize": "500g",
        "PortionSize": "150g"
    },
    "Mléko": {
        "BoughtCost": "23.90",
        "BoughtSize": "1000ml",
        "PortionSize": "250ml"
    },
    "Máslo": {
        "BoughtCost": "64.90",
        "BoughtSize": "250g",
        "PortionSize": "10g"
    },
    "Smetana na vaření": {
        "BoughtCost": "19.90",
        "BoughtSize": "200ml",
        "PortionSize": "50ml"
    },
    "Cottage sýr": {
        "BoughtCost": "26.90",
        "BoughtSize": "150g",
        "PortionSize": "75g"
    },
    "Mozzarella": {
        "BoughtCost": "27.90",
        "BoughtSize": "125g",
        "PortionSize": "60g"
    },
    "Chleba": {
        "BoughtCost": "34.90",
        "BoughtSize": "500g",
        "PortionSize": "80g"
    },
    "Rohlík": {
        "BoughtCost": "2.80",
        "BoughtSize": "1ks",
        "PortionSize": "1ks"
    },
    "Tousty": {
        "BoughtCost": "29.90",
        "BoughtSize": "500g",
        "PortionSize": "60g"
    },
    "Tortilla": {
        "BoughtCost": "39.90",
        "BoughtSize": "6ks",
        "PortionSize": "1ks"
    },
    "Kuskus": {
        "BoughtCost": "44.90",
        "BoughtSize": "500g",
        "PortionSize": "70g"
    },
    "Rýže": {
        "BoughtCost": "59.90",
        "BoughtSize": "1000g",
        "PortionSize": "75g"
    },
    "Těstoviny": {
        "BoughtCost": "34.90",
        "BoughtSize": "500g",
        "PortionSize": "80g"
    },
    "Brambory": {
        "BoughtCost": "19.90",
        "BoughtSize": "1000g",
        "PortionSize": "200g"
    },
    "Quinoa": {
        "BoughtCost": "89.90",
        "BoughtSize": "500g",
        "PortionSize": "60g"
    },
    "Ovesné vločky": {
        "BoughtCost": "19.90",
        "BoughtSize": "500g",
        "PortionSize": "50g"
    },
    "Mrkev": {
        "BoughtCost": "24.90",
        "BoughtSize": "1000g",
        "PortionSize": "100g"
    },
    "Cibule": {
        "BoughtCost": "22.90",
        "BoughtSize": "1000g",
        "PortionSize": "50g"
    },
    "Česnek": {
        "BoughtCost": "29.90",
        "BoughtSize": "100g",
        "PortionSize": "10g"
    },
    "Paprika": {
        "BoughtCost": "79.90",
        "BoughtSize": "1000g",
        "PortionSize": "100g"
    },
    "Rajče": {
        "BoughtCost": "59.90",
        "BoughtSize": "1000g",
        "PortionSize": "100g"
    },
    "Květák": {
        "BoughtCost": "34.90",
        "BoughtSize": "1ks",
        "PortionSize": "0.25ks"
    },
    "Brokolice": {
        "BoughtCost": "29.90",
        "BoughtSize": "1ks",
        "PortionSize": "0.25ks"
    }
}

def parse_numeric(value):
    try:
        return float(re.findall(r"\d+(?:\.\d+)?", value)[0])
    except (IndexError, ValueError):
        return None

def get_unit(value):
    match = re.search(r"(g|kg|ml|l|ks|pl)", value)
    return match.group(1) if match else None

def normalize_unit(value, unit):
    if unit == "kg":
        return value * 1000
    if unit == "l":
        return value * 1000
    return value

def update_and_calculate(filepath, values):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        print("⚠️ YAML nenalezen:", filepath)
        return

    parts = content.split("---")
    if len(parts) < 3:
        print("⚠️ Chybný YAML v:", filepath)
        return

    yaml_lines = parts[1].split("\n")
    new_yaml = []
    keys_to_update = ["BoughtCost", "BoughtSize", "PortionSize"]
    potential_meals = None
    cost_per_meal = None

    bought_cost = parse_numeric(values["BoughtCost"])
    bought_size_val = parse_numeric(values["BoughtSize"])
    portion_size_val = parse_numeric(values["PortionSize"])
    bought_unit = get_unit(values["BoughtSize"])
    portion_unit = get_unit(values["PortionSize"])

    if bought_size_val and portion_size_val and bought_cost and bought_unit == portion_unit:
        bought_size_val = normalize_unit(bought_size_val, bought_unit)
        portion_size_val = normalize_unit(portion_size_val, portion_unit)
        try:
            potential_meals = round(bought_size_val / portion_size_val)
            cost_per_meal = round(bought_cost / potential_meals, 2)
        except ZeroDivisionError:
            pass

    updated = {k: False for k in keys_to_update + ["PotentialMeals", "CostPerMeal"]}

    for line in yaml_lines:
        stripped = line.strip()
        updated_line = line
        for k in keys_to_update:
            if stripped.startswith(f"{k}:"):
                updated_line = f"{k}: {values[k]}"
                updated[k] = True
                break
        if stripped.startswith("PotentialMeals:"):
            updated_line = f"PotentialMeals: {potential_meals if potential_meals is not None else 'NaN'}"
            updated["PotentialMeals"] = True
        elif stripped.startswith("CostPerMeal:"):
            updated_line = f"CostPerMeal: {cost_per_meal if cost_per_meal is not None else 'NaN'}"
            updated["CostPerMeal"] = True
        new_yaml.append(updated_line)

    for k in keys_to_update:
        if not updated[k]:
            new_yaml.append(f"{k}: {values[k]}")
    if not updated["PotentialMeals"]:
        new_yaml.append(f"PotentialMeals: {potential_meals if potential_meals is not None else 'NaN'}")
    if not updated["CostPerMeal"]:
        new_yaml.append(f"CostPerMeal: {cost_per_meal if cost_per_meal is not None else 'NaN'}")

    new_content = "---\n" + "\n".join(new_yaml) + "\n---\n" + "---".join(parts[2:]).lstrip()

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
        print("✅ Upraveno:", os.path.basename(filepath))

def main():
    for filename in os.listdir(INGREDIENT_FOLDER):
        if filename.endswith(".md"):
            name = filename.replace(".md", "")
            if name in ingredient_data:
                filepath = os.path.join(INGREDIENT_FOLDER, filename)
                update_and_calculate(filepath, ingredient_data[name])

if __name__ == "__main__":
    main()
