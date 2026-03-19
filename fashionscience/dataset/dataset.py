import random
import csv

rows = []

# -----------------------------
# Basic attributes
# -----------------------------
genders = ["male", "female"]
seasons = ["summer", "winter", "spring", "autumn"]
occasions = ["office","casual","eid","mehndi","barat","walima","christmas","wedding"]
dress_types = ["eastern", "western"]

colors = ["red","green","blue","black","white","yellow","orange",
          "maroon","navy","gold","silver","pink","purple","beige","brown"]

# -----------------------------
# Outfit pairing logic
# -----------------------------
outfits = {

    "male": {

        "western": {
            "summer": [
                ["t shirt","jeans"],
                ["t shirt","shorts"],
                ["hawaiian shirt","chinos"]
            ],
            "winter": [
                ["hoodie","jeans"],
                ["turtle neck","jeans"],
                ["sweatshirt","joggers"],
                ["jacket","jeans"]
            ],
            "spring": [
                ["dress shirt","chinos"],
                ["t shirt","joggers"],
                ["blazer","jeans"]
            ],
            "autumn": [
                ["shirt","jeans"],
                ["light jacket","chinos"]
            ]
        },

        "eastern": {
            "summer": [
                ["kurta","pajama"],
                ["shalwar kameez"]
            ],
            "winter": [
                ["kurta","waistcoat"],
                ["shalwar kameez","shawl"]
            ],
            "spring": [
                ["kurta","pajama"]
            ],
            "autumn": [
                ["kurta","waistcoat"]
            ]
        }
    },

    "female": {

        "western": {

            "summer": [
                ["top","baggy jeans"],
                ["t shirt","skirt"],
                ["dress"]
            ],

            "winter": [
                ["hoodie","baggy jeans"],
                ["turtle neck","coat"],
                ["sweater","jeans"]
            ],

            "spring": [
                ["top","jeans"],
                ["dress shirt","pants"]
            ],

            "autumn": [
                ["light jacket","top","jeans"]
            ]
        },

        "eastern": {

            "summer": [
                ["long frock","tights"],
                ["short frock","plazo"],
                ["kurti","trouser"]
            ],

            "winter": [
                ["kurta","shawl"],
                ["long frock","coat"]
            ],

            "spring": [
                ["kurti","plazo"]
            ],

            "autumn": [
                ["kurti","trouser"]
            ]
        }
    }
}

# -----------------------------
# Shoes logic
# -----------------------------
shoes = {
    "male": {
        "western": ["sneakers","loafers","formal shoes","boots"],
        "eastern": ["peshawari chappal","khussa"]
    },

    "female": {
        "western": ["heels","sneakers","boots","sandals"],
        "eastern": ["khussa","flats","sandals"]
    }
}

# -----------------------------
# Accessories
# -----------------------------
accessories = {
    "male": ["watch","belt","cap"],
    "female": ["earrings","necklace","handbag","bracelet"]
}

# -----------------------------
# Occasion color logic
# -----------------------------
occasion_colors = {
    "mehndi": ["yellow","green","orange"],
    "barat": ["red","maroon","gold"],
    "wedding": ["red","gold","maroon"],
    "walima": ["white","silver"],
    "christmas": ["red","green"],
    "eid": ["white","pastel"]
}

# -----------------------------
# Fabric by season
# -----------------------------
season_fabric = {
    "summer": ["cotton","lawn","linen"],
    "winter": ["wool","leather","denim"],
    "spring": ["cotton","chiffon"],
    "autumn": ["linen","denim"]
}

# -----------------------------
# Dataset generation
# -----------------------------
for i in range(5000):

    gender = random.choice(genders)
    season = random.choice(seasons)
    occasion = random.choice(occasions)
    dress_type = random.choice(dress_types)

    # Choose outfit from logic
    outfit = random.choice(outfits[gender][dress_type][season])

    product = " + ".join(outfit)

    # Shoes
    shoe = random.choice(shoes[gender][dress_type])

    # Accessories
    if random.random() < 0.4:
        accessory = " + ".join(random.sample(accessories[gender], 2))
    else:
        accessory = random.choice(accessories[gender])

    # Color
    if occasion in occasion_colors:
        color = random.choice(occasion_colors[occasion])
    else:
        color = random.choice(colors)

    # Fabric
    fabric = random.choice(season_fabric[season])

    # Budget
    budget = random.randint(1000,20000)

    rows.append([
        gender,
        season,
        occasion,
        dress_type,
        product,
        shoe,
        accessory,
        color,
        fabric,
        budget
    ])

# -----------------------------
# Save CSV
# -----------------------------
with open("fashionscience/fashion_dataset.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "gender",
        "season",
        "occasion",
        "dress_type",
        "product",
        "shoes",
        "accessory",
        "color",
        "fabric",
        "budget"
    ])

    writer.writerows(rows)

print("Dataset created successfully with 5000 intelligent outfits")
