"""Запросить у пользователя возраст. Если возраст меньше 0 - вывести Wrong input,
если меньше 18 - вывести CocaCola, иначе - вывести Beer"""

def drink(age:int):
    if age < 0:
        return (f"Вы ввели неверный возраст")
    elif age < 18:
        return(f"CocaCola")
    else:
        return(f'Beer')

 




