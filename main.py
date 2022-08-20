print("Us BEST BANK OF RUSSIA!")
def registration():
    my_name:str = input("Ваше имя: ")
    my_age = input("Ваш возраст: ")
    my_age = int(my_age)
    if my_age != 18:
        print("You have not 18 years old")
    else: 
        place_of_holder = input("Место жительства: ")
        password_data = input("Пароль от аккаунта: ")
        all_data = [my_name, my_age, place_of_holder, password_data]
        for datall in all_data:
            print(datall)
def count():
    my_count = 0 
    if my_count == 0:
	print("You have 0 money")
    company_it = 1000
    invest_company_it = input("You want invest in company IT: YES or NO: ")
    if invest_company_it == "YES":
	if my_count < 1000:
	     print("you can't)
count()
registration()

