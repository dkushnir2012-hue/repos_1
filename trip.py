from pywebio.input import input as input_pw, NUMBER, select, slider
from pywebio.output import put_text, put_error
import prices

stu = input_pw("Кількість учнів", type=NUMBER)

if stu == 0:
    put_error("Помилка")

else:
    tch = input_pw("Кількість вчителів", type=NUMBER)

    tr = select("Тип транспорту", options=["Автобус", "Поїзд"])

    days = slider("Кількість днів", min_value=0, max_value=10, value=0)

    ppl = stu + tch

    if tr == "Автобус":
        bus = ppl // prices.BUS_CAPACITY
        if ppl % prices.BUS_CAPACITY != 0:
            bus += 1
        t_cost = bus * prices.BUS_PRICE
    else:
        bus = 0
        t_cost = ppl * prices.TRAIN_PRICE

    h_cost = ppl * prices.HOTEL_PRICE * days

    total = t_cost + h_cost

    if ppl > 30:
        total = total - total * prices.DISCOUNT_PERCENT / 100

    put_text("Людей:", ppl)

    if tr == "Автобус":
        put_text("Автобусів:", bus)

    put_text("Транспорт:", t_cost)
    put_text("Проживання:", h_cost)
    put_text("Всього:", int(total))