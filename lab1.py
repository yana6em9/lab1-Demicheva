
import os
import time

# Escape-последовательности для цветов
CSI = "\033["
RESET = f"{CSI}0m"

RED = f"{CSI}41m"
YELLOW = f"{CSI}43m"
BLUE = f"{CSI}44m"
PURPLE = f"{CSI}45m"
WHITE = f"{CSI}47m"
BLACK = f"{CSI}40m"


# Очистка экрана
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# 1. Флаг Швейцарии
def draw_flag(color=RED):
    clear()
    print("Флаг Швейцарии:\n")

    for i in range(15):
        line = ""

        for j in range(21):
            # Горизонтальная и вертикальная части креста
            if (5 <= i <= 9 and 7 <= j <= 13) or \
               (3 <= i <= 11 and 9 <= j <= 11):
                line += WHITE + "  " + RESET
            else:
                line += color + "  " + RESET

        print(line)


# 2. Два больших кольца, как в образце j
def draw_pattern():
    clear()
    print("Узор из двух колец:\n")

    # 7 строк и 15 столбцов
    # 3 и 11 — центры двух окружностей
    for y in range(7):
        line = ""

        for x in range(15):
            ring = False
            inside = False

            for center in [3, 11]:
                dx = x - center
                dy = y - 3

                # Внешний контур окружности
                if dx * dx + dy * dy <= 10:
                    ring = True

                # Белая середина кольца
                if dx * dx + dy * dy <= 3:
                    inside = True

            # Белый фон, чёрный контур, белая середина
            if ring and not inside:
                line += BLACK + "  " + RESET
            else:
                line += WHITE + "  " + RESET

        print(line)

    time.sleep(2)


# 3. Анимация из четырёх кадров
def animate():
    colors = [RED, YELLOW, BLUE, PURPLE]

    for color in colors:
        draw_flag(color)
        time.sleep(1)


# Запуск программы
if __name__ == "__main__":
    animate()







