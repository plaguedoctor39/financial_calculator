salary = int(input("Введите заработанную плату в месяц: "))
mortgage = int(input("Введите сколько процентов уходит на ипотеку: "))
for_life = int(input("Введите сколько процентов уходит на жизнь: "))
premium = int(input("Введите количество премий за год: "))

print("На ипотеку было потрачено:", int((salary * mortgage / 100) * 12), "рублей")
print("Было накоплено:", int((salary - salary * ((mortgage + for_life) / 100)) * 12 + (salary * premium) * 0.5),
      "рублей")
