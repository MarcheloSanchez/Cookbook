
import os

# 🔁 ZDE změň cestu ke složce se surovinami
INGREDIENT_FOLDER = r"C:\Users\MarcelMachanec\Documents\Můza\Ingredients"

# Slovník cen – název souboru (bez .md) a jejich ceny
ingredient_prices = {
    "Vejce": {"Shop 1": 39.90, "Shop 2": 42.90},
    "Kuřecí maso": {"Shop 1": 129.90, "Shop 2": 134.90},
    "Mleté maso": {"Shop 1": 159.90, "Shop 2": 164.90},
    "Tvaroh tvrdý": {"Shop 1": 34.90, "Shop 2": 36.90},
    "Tofu": {"Shop 1": 29.90, "Shop 2": 31.90},
    "Šunka": {"Shop 1": 24.90, "Shop 2": 26.90},
    "Plátkový sýr": {"Shop 1": 22.90, "Shop 2": 24.90},
    "Tuňák v konzervě": {"Shop 1": 49.90, "Shop 2": 52.90},
    "Losos": {"Shop 1": 399.90, "Shop 2": 419.90},
    "Bílý jogurt": {"Shop 1": 22.90, "Shop 2": 24.90},
    "Mléko": {"Shop 1": 23.90, "Shop 2": 25.90},
    "Máslo": {"Shop 1": 64.90, "Shop 2": 67.90},
    "Smetana na vaření": {"Shop 1": 19.90, "Shop 2": 21.90},
    "Cottage sýr": {"Shop 1": 26.90, "Shop 2": 28.90},
    "Mozzarella": {"Shop 1": 27.90, "Shop 2": 29.90},
    "Chleba": {"Shop 1": 34.90, "Shop 2": 36.90},
    "Rohlík": {"Shop 1": 2.80, "Shop 2": 3.00},
    "Tousty": {"Shop 1": 29.90, "Shop 2": 31.90},
    "Tortilla": {"Shop 1": 39.90, "Shop 2": 42.90},
    "Kuskus": {"Shop 1": 44.90, "Shop 2": 47.90},
    "Rýže": {"Shop 1": 59.90, "Shop 2": 62.90},
    "Těstoviny": {"Shop 1": 34.90, "Shop 2": 36.90},
    "Brambory": {"Shop 1": 19.90, "Shop 2": 21.90},
    "Quinoa": {"Shop 1": 89.90, "Shop 2": 94.90},
    "Ovesné vločky": {"Shop 1": 19.90, "Shop 2": 21.90},
    "Mrkev": {"Shop 1": 24.90, "Shop 2": 26.90},
    "Cibule": {"Shop 1": 22.90, "Shop 2": 24.90},
    "Česnek": {"Shop 1": 29.90, "Shop 2": 31.90},
    "Paprika": {"Shop 1": 79.90, "Shop 2": 84.90},
    "Rajče": {"Shop 1": 59.90, "Shop 2": 62.90},
    "Květák": {"Shop 1": 34.90, "Shop 2": 36.90},
    "Brokolice": {"Shop 1": 29.90, "Shop 2": 31.90}
}

def update_cost_text(yaml_lines, prices):
    new_yaml = []
    inside_cost = False
    cost_written = False

    for line in yaml_lines:
        if line.strip().startswith("Cost:"):
            new_yaml.append("Cost:")
            new_yaml.append(f"  Shop 1: {prices['Shop 1']}")
            new_yaml.append(f"  Shop 2: {prices['Shop 2']}")
            inside_cost = True
            cost_written = True
        elif inside_cost and (line.startswith("  Shop ") or line.strip() == ""):
            continue
        else:
            inside_cost = False
            new_yaml.append(line)

    if not cost_written:
        # Pokud Cost: sekce neexistuje, přidej na konec frontmatteru
        new_yaml.append("Cost:")
        new_yaml.append(f"  Shop 1: {prices['Shop 1']}")
        new_yaml.append(f"  Shop 2: {prices['Shop 2']}")

    return new_yaml

def process_file(filepath, prices):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines[0].strip() != "---":
        print(f"⚠️ YAML nenalezen v souboru: {filepath}")
        return

    # Najdi konec YAML frontmatteru
    try:
        end_index = lines[1:].index("---\n") + 1
    except ValueError:
        print(f"⚠️ Chybný frontmatter v: {filepath}")
        return

    yaml_lines = [line.rstrip("\n") for line in lines[1:end_index]]
    rest_of_file = lines[end_index+1:]

    updated_yaml = update_cost_text(yaml_lines, prices)
    updated_content = "---\n" + "\n".join(updated_yaml) + "\n---\n" + "".join(rest_of_file)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated_content)
        print(f"✅ Upraveno: {os.path.basename(filepath)}")

def main():
    for filename in os.listdir(INGREDIENT_FOLDER):
        if filename.endswith(".md"):
            name = filename.replace(".md", "")
            if name in ingredient_prices:
                filepath = os.path.join(INGREDIENT_FOLDER, filename)
                process_file(filepath, ingredient_prices[name])

if __name__ == "__main__":
    main()
