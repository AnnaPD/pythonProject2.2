price_ticket = 0
while True:
    ticket = int(input("Введите количество билетов "))
    if type(ticket) == int:
        break
for n in range(ticket):
    n += 1
    while True:
        age_ticket = int(input(f"Введите возраст для билета № {n} "))
        if age_ticket < 18:
            print("Билет бесплатный")
        elif 18 <= age_ticket < 25:
            price_ticket += 990
            print("Стоимость билета 990 рублей")
        else:
            price_ticket += 1390
            print("Стоимость билета 1390 рублей")
        if type(age_ticket) == int:
            break
if ticket > 3:
    price_ticket = price_ticket - ((price_ticket / 100) * 10)
    print(f'Сумма к оплате {price_ticket} руб. с учетом 10%-ой скидки за покупку более 3-х билетов')
else:
    print(f'Сумма к оплате {price_ticket} руб.')