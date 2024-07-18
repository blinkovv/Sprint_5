input_name = "//label[text()='Имя']/parent::div/input"  # Регистрация. Поле Имя
input_email = "//label[text()='Email']/parent::div/input"  # Регистрация. Поле Email
input_password = "//label[text()='Пароль']/parent::div/input"  # Регистрация. Поле Пароль
button_register = '//button[text()="Зарегистрироваться"]'  # Регистрация. Кнопка "Зарегистрироваться"
error_password = '//p[text()="Некорректный пароль"]'  # Регистрация. Некорректный пароль ошибка текст


button_login = '//button[text()="Войти в аккаунт"]'  # Кнопка "Войти" на главной странице
button_login_in_chapter = '//button[text()="Войти"]'  # Кнопка "Войти" в разделе ВХОД
button_reset_password = 'a[href="/forgot-password"]'  # Кнопка "Восстановить пароль" на странице Логин
input_password_in_enter_page = "//label[text()='Пароль']/parent::div/input"  # Поле "Пароль" на странице ВХОДА
button_personal_account = '//p[text()="Личный Кабинет"]'  # Кнопка "Личный Кабинет" на главной странице
button_login_from_register = '//a[text()="Войти"]'  # Кнопка "Войти" в форме регистрации и Восстановить пароль
text_entrance_on_the_login_page = '//h2[text()="Вход"]'  # Текст "Вход" на странице Login
text_assemble_burger_main_page = '//h1[text()="Соберите бургер"]'  # Тескст "Собери бургер" на главной странице
place_an_order_button = '//button[text()="Оформить заказ"]'  # Кнопка Оформить заказ для авторизованного пользователя


button_constructor = '//p[text()="Конструктор"]'  # Кнопка "Конструктор" переход в его вкладку
button_logotype = '//a[@class="active"]' # Переход по Stellar Burger
button_log_out =  '//button[text()="Выход"]' # Кнопка "Выход" из личного аккаунта


link_buns = '//span[text()="Булки"]'  # Раздел Булки
link_sauces = '//span[text()="Соусы"]'  # Раздел Соусы
link_fillings = '//span[text()="Начинки"]'  # Раздел Начинки
text_buns = '//h2[text()="Булки"]'  # Текст-Заголовок в разделе Булки
text_sauces = '//h2[text()="Соусы"]'  # Текс-Заголовок в разделе Соусы
text_fillings = '//h2[text()="Начинки"]'  # Текст-Заголовок в разделе Начинки