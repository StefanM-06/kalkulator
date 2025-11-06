from math import pi


def menu():
    print("=============================")
    print("   КАЛКУЛАТОР   ")
    print("=============================")
    print("1.Калкулатор на геометрични фигури")
    print("2Калкулатор на геометрични тела")
    print("3.Изход")
    print("=============================")

def menu_tela():
    print("=============================")
    print("   КАЛКУЛАТОР НА ГЕОМЕТРИЧНИ ТЕЛА")
    print("=============================")
    print("1.Обем на кълбо")
    print("2.Обем на паралелепипед")
    print("3.Назад")
    print("=============================")

def menu_figuri():
    print("=============================")
    print("   КАЛКУЛАТОР НА ГЕОМЕТРИЧНИ ФИГУРИ")
    print("=============================")
    print("1.Лице на трапец")
    print("2.Лице на кръг")
    print("3.Назад")
    print("=============================")

def lice_trapec():
    print("Лице на трапец")
    try:
        a = float(input("Въведи голяма основа (a): "))
        b = float(input("Въведи малка основа (b): "))
        h = float(input("Въведи височина (h): "))
        area = ((a + b) / 2) * h
        print(f"Лицето на трапеца е: {area:.2f}")
    except ValueError:
        print("Грешка! Моля въведи числа.")

def lice_krug():
    print("Лице на кръг")
    try:
        r = float(input("Въведи радиус (r): "))
        area = pi * (r *r)
        print(f"Лицето на кръга е: {area:.2f}")
    except ValueError:
        print("Грешка! Моля въведи число.")

def obem_kulbo():
    print("Обем на кълбо")
    try:
        r = float(input("Въведи радиус (r): "))
        volume = (4/3) * pi * (r *r * r)
        print(f"Обемът на кълбото е: {volume:.2f}")
    except ValueError:
        print("Грешка! Моля въведи число.")

def obem_paralel():
    print("Обем на паралелепипед")
    try:
        a = float(input("Въведете страната a: "))
        b = float(input("Въведете страната b: "))
        c = float(input("Въведете страната c: "))
        volume = a * b * c
        print(f"Обемът на паралелепипеда е: {volume:.2f}")
    except ValueError:
        print("Грешка! Опитайте отново.")

def main():
    while True:
        menu()
        choice = input("Избери опция (1-3): ")

        
        if choice == "1":
            while True:
                menu_figuri()
                fig = input("Избери фигура (1-3): ")
                if fig == "1": lice_trapec()
                elif fig == "2": lice_krug()
                elif fig == "3": break
                else: print("Невалиден избор!")
                input("Натисни Enter за продължение...")

      
        elif choice == "2":
            while True:
                menu_tela()
                telo = input("Избери тяло (1-3): ")
                if telo == "1": obem_kulbo()
                elif telo == "2": obem_paralel()
                elif telo == "3": break
                else: print("Невалиден избор!")
                input("Натисни Enter за продължение...")

        elif choice == "3":
            print("Изход от програмата. Довиждане!")
            break

        else:
            print("Невалиден избор! Опитай пак.")


if __name__ == "__main__":
    main()
    input("Натисни Enter за изход...")



