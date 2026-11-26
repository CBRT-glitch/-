class Country:
    def __init__(self, name, pexota, Boenie_mashin, balans, max_pexot, max_Boenie_mashin, cena_soldata, price_limit):
        self.name = name
        self.pexota = pexota
        self.Boenie_mashin = Boenie_mashin
        self.balans = balans
        self.max_pexot = max_pexot
        self.max_Boenie_mashin = max_Boenie_mashin
        self.cena_soldata = cena_soldata
        self.price_limit = price_limit

    def buy_soldiers(self):
        Buy = int(input("Сколько солдатиков хотите приобрести?"))
        total_price = Buy * self.cena_soldata

        if Buy <= 0:
            print("Количество должно быть больше нуля.")
                    

        elif self.balans < total_price:
            print("Недостаточно средств для найма войск.")

        elif self.pexota + Buy > self.max_pexot:
            print (f"Превышен лимит пехоты! | лимит  пехоты {self.max_pexot}")
            
        else:
            self.balans -= total_price
            self.pexota += Buy
            print(f"Списано из казны | {total_price}")
            print(f"Войска успешно куплены. | {self.pexota}")


    def Buy_max_pexot(self):
        Max_Army = int(input("На сколько едениц вы хотите увеличить лимит пехоты?"))
        total_limit_price = Max_Army * self.price_limit

        if Max_Army <= 0:
            print("Количество должно быть больше нуля.")
        
        elif self.balans < total_limit_price:
            print("Недостаточно средств для увелечение лимита пехоты.")

        else:
            self.balans -= total_limit_price
            self.max_pexot += Max_Army
            print(f"Списано из казны | {total_limit_price}")
            print(f"Вы увеличили лимит пехоты! | лимит {self.max_pexot}")




Rassia = Country("Россия", 8700, 1300, 2338, 8700, 1300, 20, 35)
China = Country("Китай", 1352, 3012, 15232, 1352, 3012, 10, 30)
Japan = Country("Япония", 783, 1532, 5432, 783, 1532, 22, 55)
Ukraine = Country("Украина", 2531, 1432, 3523, 2531, 1432, 10, 30)


countries_dict = {
    "Россия": Rassia,
    "Китай": China,
    "Япония": Japan,
    "Украина": Ukraine
}




