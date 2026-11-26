from darabase_Stran import Country
from darabase_Stran import countries_dict
from time import time, sleep
from random import uniform
from razvegka import sdelat_razvedky

# Кд для разведки йопта
CD_recon = 0

while True:
    Select_country = input("\nВведите название страны за которую хотите сражатся.").strip().capitalize()
    if Select_country in countries_dict:
        stats = countries_dict[Select_country]
        print(f"\nВы выбрали {Select_country}")
        print(f"Армия {stats.pexota} чел. | Военная техника {stats.Boenie_mashin} ед. | Баланс {stats.balans}$ | ")
        break
    else:
        print("\nТакой страны нету")

while True:
    print(f"""\nглавное меню
    1. купить пехоту ("ПРИМЕЧАНИЕ: покупаются только солдаты техника в счёт не входит)
    2. разведка (Узнать данные о соседних стран)
    3. Выйти из игры""")

    menu_choice = int(input(f"\nЖдём приказа генерал!"))
    if menu_choice == 1:
        nested_input = int(input("""1. Купить пехоту
2. Увеличить лимит пехоты"""))

        if nested_input == 1:
            stats.buy_soldiers()

        else:
            stats.Buy_max_pexot()

    elif menu_choice == 2:
        # Бачим текующие время епт
        current_time = time()
        past_tence = current_time - CD_recon # паст_тенсе эта прошедшее время а тута мы узнаем згога прошло
        if past_tence < 60:
            time_left_CD = int(60 - past_tence) # времичко до конца кд пон же
            print(f"\nНаданный момент разведка не доступна повторите попытку через {time_left_CD} сек")
            continue # тепаемся обратно потомушто кд еще не прошло

        print("--- РАЗВЕДКА --- (Получить данные о соседях)")
        scout_country = input("О какой стране хотите получить данные?").strip().capitalize() # Получаем какую страну ввел пользователь

        CD_recon = past_tence # обновляем время отправки

        # ПРовиряяяяяет какую страну пользовател ввел и есть эта страна в словаре а так же не ввел ли он свою
        if scout_country in countries_dict:
            if scout_country == Select_country:
                print(f"Это ваша страна. Данные о ней можно посмотреть в статистике")

            

            else:

                original_armia = countries_dict[scout_country].pexota
                original_balans = countries_dict[scout_country].balans
                original_BoenieMashin = countries_dict[scout_country].Boenie_mashin


                fakava_armia, fakava_balans, fakava_Boenie_mashin = sdelat_razvedky(original_armia, original_balans, original_BoenieMashin)

                
                print(f"""\n--- ИТОГИ РАЗВЕДКИ ---
                1. пехота {fakava_armia}
    2 Военная техника {fakava_Boenie_mashin}
    3. Казна {fakava_balans}""")
                


        



