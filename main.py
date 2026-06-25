


import re
import os

DATA = {
    "about": {
        "name": "Есен Динмухамед",
        "age": 16,
        "description": "Мне 16 лет, я начинающий Python-разработчик. Увлекаюсь технологиями, хоккеем и английским языком. Стремлюсь создавать полезные проекты и развиваться в сфере IT."
    },
    "goal": "Я пришёл в программирование, потому что мне интересно создавать полезные проекты и решать сложные задачи с помощью технологий. В будущем я хочу развиваться в сфере IT, совмещая знания в области технологий и бизнеса, участвовать в крупных проектах и строить успешную карьеру.",
    "how_i_got_here": "Мой интерес к IT появился благодаря любопытству к современным технологиям и желанию понимать, как работают программы и цифровые сервисы. Я хотел не просто пользоваться технологиями, но и создавать их — и это привело меня к программированию.",
    "mentor": {
        "name": "Каракат тичер",
        "description": "Мне помогает и вдохновляет Каракат тичер. Она поддерживает меня на пути в IT и помогает разобраться в сложных темах программирования."
    },
    "progress": {
        "point_a": "Когда я только начал изучать программирование, у меня были лишь базовые знания и небольшой опыт. Многие концепции казались сложными и непонятными.",
        "point_b": "Со временем я освоил основы языков программирования, научился писать простые программы и лучше понимать принципы разработки. Сейчас я продолжаю развиваться, изучаю новые технологии и уверенно двигаюсь к своим профессиональным целям."
    },
    "hobbies": [
        "Хоккей — занимаюсь на протяжении 10 лет, стал чемпионом Казахстана 🏒🏆",
        "Английский язык — изучаю углублённо",
        "Люблю узнавать новое и ставить перед собой новые цели"
    ],
    "works": [
        {
            "title": "Игра «Бумага, камень, ножницы»",
            "description": "Консольная игра на Python. Пользователь играет против компьютера, который случайным образом выбирает ход. Освоил условные операторы, генерацию случайных чисел и логику игры.",
            "link": "GitHub (скоро)"
        }
    ],
    "github": "https://github.com/"
}


class Portfolio:
    def __init__(self, data: dict):
        self.data = data

    @staticmethod
    def _header(title: str):
        width = 54
        print("\n" + "═" * width)
        print(f"  ✦  {title}")
        print("═" * width)

    @staticmethod
    def _footer():
        print("─" * 54)

    def show_about(self):
        d = self.data["about"]
        self._header("О СЕБЕ")
        print(f"  Имя:     {d['name']}")
        print(f"  Возраст: {d['age']} лет")
        print()
        print(f"  {d['description']}")
        self._footer()

    def show_goal(self):
        self._header("МОЯ ЦЕЛЬ")
        print(f"  {self.data['goal']}")
        self._footer()

    def show_how_i_got_here(self):
        self._header("КАК Я ПРИШЁЛ В IT")
        print(f"  {self.data['how_i_got_here']}")
        self._footer()

    def show_mentor(self):
        m = self.data["mentor"]
        self._header("МОЙ МЕНТОР")
        print(f"  Ментор: {m['name']}")
        print()
        print(f"  {m['description']}")
        self._footer()

    def show_progress(self):
        p = self.data["progress"]
        self._header("ТОЧКА А → ТОЧКА Б")
        print("  📍 Точка А (начало):")
        print(f"     {p['point_a']}")
        print()
        print("  🚀 Точка Б (сейчас):")
        print(f"     {p['point_b']}")
        self._footer()

    def show_hobbies(self):
        self._header("ХОББИ И ИНТЕРЕСЫ")
        for hobby in self.data["hobbies"]:
            print(f"  •  {hobby}")
        self._footer()

    def show_works(self):
        self._header("МОИ ЛУЧШИЕ РАБОТЫ")
        for i, work in enumerate(self.data["works"], 1):
            print(f"  [{i}] {work['title']}")
            print(f"      {work['description']}")
            print(f"      🔗 {work['link']}")
            print()
        self._footer()

    def show_github(self):
        self._header("МОЙ GITHUB")
        print(f"  🔗 {self.data['github']}")
        print()
        print("  Все проекты и исходный код — в репозитории.")
        self._footer()


MENU_ITEMS = [
    ("1", "О себе"),
    ("2", "Моя цель"),
    ("3", "Как я пришёл в IT"),
    ("4", "Мой ментор"),
    ("5", "Точка А → Точка Б"),
    ("6", "Хобби и интересы"),
    ("7", "Мои лучшие работы"),
    ("8", "Ссылка на GitHub"),
    ("0", "Выход"),
]

VALID_CHOICES = re.compile(r"^[0-8]$")


def show_menu():
    width = 54
    print("\n" + "╔" + "═" * (width - 2) + "╗")
    title = "ПОРТФОЛИО — ЕСЕН ДИНМУХАМЕД"
    padding = (width - 2 - len(title)) // 2
    print("║" + " " * padding + title + " " * (width - 2 - padding - len(title)) + "║")
    print("╠" + "═" * (width - 2) + "╣")
    for key, label in MENU_ITEMS:
        line = f"  {key}.  {label}"
        print("║" + line + " " * (width - 2 - len(line)) + "║")
    print("╚" + "═" * (width - 2) + "╝")


def get_choice() -> str:
    while True:
        raw = input("\n  Введите номер раздела: ").strip()
        if VALID_CHOICES.match(raw):
            return raw
        print("  ⚠️  Введите цифру от 0 до 8.")


def main():
    os.system("cls" if os.name == "nt" else "clear")

    print("""
  ██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ ██╗      ██╗ ██████╗
  ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗██║      ██║██╔═══██╗
  ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██║   ██║██║      ██║██║   ██║
  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██║   ██║██║      ██║██║   ██║
  ██║     ╚██████╔╝██║  ██║   ██║   ██║     ╚██████╔╝███████╗ ██║╚██████╔╝
  ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚═╝ ╚═════╝
    """)

    portfolio = Portfolio(DATA)

    actions = {
        "1": portfolio.show_about,
        "2": portfolio.show_goal,
        "3": portfolio.show_how_i_got_here,
        "4": portfolio.show_mentor,
        "5": portfolio.show_progress,
        "6": portfolio.show_hobbies,
        "7": portfolio.show_works,
        "8": portfolio.show_github,
    }

    while True:
        show_menu()
        choice = get_choice()

        if choice == "0":
            print("\n  👋  До встречи! Удачи в обучении, Есен!\n")
            break

        actions[choice]()
        input("\n  [Нажмите Enter, чтобы вернуться в меню]")


if __name__ == "__main__":
    main()