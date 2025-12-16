# 1. MODEL

class Actor:
    def __init__(self, full_name, role):
        self.full_name = full_name
        self.role = role

class FilmModel:
    def __init__(self, title, genre, director, year, duration, studio):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = []

    def add_actor(self, actor_obj):
        self.actors.append(actor_obj)


# 2. TEMPLATE

class FilmTemplate:
    @staticmethod
    def render(film_model):
        """Создает 'страницу' (текстовый блок) с информацией о фильме"""
        output = []
        output.append("=" * 40)
        output.append(f"ФИЛЬМ: {film_model.title.upper()}")
        output.append("=" * 40)
        output.append(f"Жанр:      {film_model.genre}")
        output.append(f"Режиссер:  {film_model.director}")
        output.append(f"Год:       {film_model.year}")
        output.append(f"Длительность: {film_model.duration} мин")
        output.append(f"Студия:    {film_model.studio}")
        output.append("-" * 40)
        output.append("АКТЕРСКИЙ СОСТАВ:")
        
        if not film_model.actors:
            output.append("   (Нет информации об актерах)")
        else:
            for i, actor in enumerate(film_model.actors, 1):
                output.append(f"   {i}. {actor.full_name} ... {actor.role}")
        
        output.append("=" * 40)
        return "\n".join(output)


# 3. VIEW

class FilmView:
    def create_film_interactive(self):
        """Логика получения данных (симуляция ввода от пользователя)"""
        print("\n--- СОЗДАНИЕ НОВОГО ФИЛЬМА ---")
        title = input("Название фильма: ")
        genre = input("Жанр: ")
        director = input("Режиссер: ")
        year = input("Год выпуска: ")
        duration = input("Длительность (мин): ")
        studio = input("Студия: ")

        film = FilmModel(title, genre, director, year, duration, studio)

        while True:
            choice = input("Добавить актера? (д/н): ").lower()
            if choice != 'д':
                break
            name = input("  -> ФИО актера: ")
            role = input("  -> Роль: ")
            actor = Actor(name, role)
            film.add_actor(actor)
        
        return film

    def show_film_page(self, film_model):
        """Логика отображения: берет Модель, скармливает её Шаблону и выводит результат"""
        page_content = FilmTemplate.render(film_model)
        
        print("\n\nПредпросмотр страницы фильма:")
        print(page_content)


if __name__ == "__main__":
    app_view = FilmView()

    my_film_model = app_view.create_film_interactive()

    app_view.show_film_page(my_film_model)