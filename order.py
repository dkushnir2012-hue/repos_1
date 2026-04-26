import letter

name = input("Введіть ім'я та прізвище: ")
date = input("Введіть дату поїздки: ")
persons = int(input("Введіть кількість осіб: "))

price_per_person = 15000

total_price = persons * price_per_person

if persons > 5:
    discount = total_price * 0.05
else:
    discount = 0

final_price = total_price - discount

letter_text = letter.LETTER_TEMPLATE.format(
    name=name,
    date=date,
    persons=persons,
    price_per_person=price_per_person,
    total_price=total_price,
    discount=int(discount),
    final_price=int(final_price)
)

print(letter_text)