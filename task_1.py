age =int(input("How old are you? "))

if age < 12:
    print("You can only watch U films and PG films if accompanied by parents")
elif 12 <= age < 15:
    print("You can watch U, PG AND 12 films")
elif 15 <= age < 18:
    print("You can watch U, PG, 12 AND 15 films")
elif age >= 18:
    print("You can watch any film available")
else:
    print("ERROR")       