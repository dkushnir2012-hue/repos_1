car = {
    "model": 'RAV4 Гібрид',
    "price": 2_026_125,
    "full_weight": '2135 кг',
    "max_speed": '180 км/год',
    "fuel_consumption": 4.9,
    "interior_features": [
        "Шкіряне кермо",
        "Підігрів сидінь",
        "Клімат-контроль",
        "Мультимедійна система"
    ]
}

car ["trailer_weight_with_brakes"] = 1650

print(car["model"])
print(car["price"])

print(car["interior_features"][0])

insurance_payment = car["price"] * 0.005
car["insurance_payment"] = insurance_payment
print(car["insurance_payment"])

fuel = car["fuel_consumption"]
fuel_for_200km = fuel / 100 * 200
trip_cost = fuel_for_200km * 93

print(trip_cost)