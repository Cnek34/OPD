define Sasha17yo = Character('Саша', color="#ff00ff")
define Bogdan = Character('Богдан', color="#ff00ff")
define Alina = Character('Алина', color="#ff00ff")
define Mark = Character('Марк', color="#ff00ff")
define Pavel = Character('Павел', color="#ff00ff")
define Team = Character('Команда', color="#ff00ff")
define Stranger = Character('Незнакомец', color="#ff00ff")
define Sasha37yo= Character('Александр', color="#ff00ff")
label start:

    scene start
    with dissolve
    show sasha37yo
    Sasha37yo"Привет! Я Саша и я работаю специалистом информационной безопасности."
    Sasha37yo"Как я докатился до такой жизни? Спокойно, сейчас я все расскажу…"
    Sasha37yo"Эта история началась лет 20 назад. Тогда я был обычным школьником, который совсем не интересовался IT сферой, но очень часто пользовался компьютером."

    scene alleyway
    with dissolve
    show sasha17yo
    Sasha37yo"В тот день я шел от бабушки. На улице было уже достаточно темно, но я все равно решил сократить путь до дома, проложив свой путь через тёмный переулок."

    scene door
    with dissolve
    show bogdan
    "Вдруг меня окликнул мужчина, который стоял в дверном проёме."
    Stranger"Мальчик, не поможешь нам?"

    scene alleyway
    with dissolve
    show sasha17yo
    Sasha17yo"Я прошел мимо не обращая на него внимания."

    scene door
    with dissolve
    show bogdan
    show sasha17yo
    Stranger"Саша стой, нам действительно нужна твоя помощь!"
    "Остановившись, Саша спросил у мужчины."
    Sasha17yo"Откуда вы знаете моё имя?»"
    Stranger"Проходи ко мне в дом и я тебе все расскажу."
    "Хотя мне было страшно, но в итоге интерес переборол страх и я пошел."

    scene room
    with dissolve
    show bogdan
    show sasha17yo
    "Войдя в помещение, я был удивлён от увиденного. Комната была наполнена большим количеством устройств, компьютеров и шпионской аппаратуры."
    Stranger"Ну, давай знакомиться. Меня зовут Богдан, а это моя команда. И все мы специалисты в сфере кибербезопасность. Наблюдая за тобой, мы
     поняли, что у тебя большие перспективы в данной сфере."

    scene table1
    with dissolve
    show bogdan
    show sasha17yo
    show pavel
    Bogdan"Итак, это Павел и он кибербезопасный аналитик."
    Pavel"Хай! Тебе как рассказать в двух словах или поподробнее."
    menu:
        "Я не тороплюсь.":
            Pavel"В мои обязанности входит анализ поведения пользователей. Эта информация касается сайтов, которые посещают, количество проводимого времени в сети,
             используемых приложений пользователем."
            Pavel"Следующее это отслеживание и классификация угроз."
            Pavel"Это могут быть фишинговые сайты, трояны, скрытые майнеры по добыче криптовалюты и ещё масса зловредных программ. Ну и конечно же составление
             моделей исходящих угроз и поиск слабых мест в защите."
        "Давай кратенько.":
            Pavel"Я отслеживаю и анализирую угрозы кибербезопасности, оцениваю уязвимости и разрабатываю стратегии защиты и так далее..."

    scene table2
    with dissolve
    show alina
    show bogdan
    show sasha17yo
    Bogdan"Так, идем дальше. Это Алина."
    Alina"О, привет."
    Bogdan"Она лучший этичный хакер."
    Alina"Ой, не начиная. Я всего-то провожу пентесты , нахожу и устраняю уязвимости в IT-инфраструктуре компании, которые могут привести к потенциальному взлому."

    scene table3
    with dissolve
    Bogdan"И последний наш участник Марк."
    Mark"Приветствую. На меня возлагается обеспечение безопасности информации в ходе ее обработки, передачи, хранения."
    Mark"Я имею прямое отношение обеспечению целостности и постоянства процессов обработки информации, реагированию на инциденты, восстановлению работы сети и компьютерного оборудования."

    scene siren
    with dissolve
    Bogdan"Ооо, нет. Кто-то пытается взломать наше оборудование."
    Bogdan"Так, всем по местам. А ты Саша иди к Павлу, тоже будешь помогать."
    Sasha17yo"Но я ничего не умею."
    Pavel"Ничего, будем учиться на практике."

    scene table1
    with dissolve
    Pavel"Сначала надо определить тип кибератаки. Это может быть фишинг, брутфорс-атака, вредоносное ПО и так далее… В нашем же случае это скорее всего брутфорс-атака."
    Sasha17yo"И как это понимать."
    Pavel"Смотри, в этих атаках хакеры используют ПО для подбора комбинации паролей."
    Pavel"Учитывая сложность инструментов взлома учетных данных, полагаться на комбинацию букв,
     символов и цифр уже недостаточно для обеспечения надежной защиты."
    Pavel"Лучшими мерой защиты от брутфорса является включение двухфакторной аутентификации. Но мы её ДО СИХ ПОР не сделали."

    scene table3
    with dissolve
    Mark"САША СМОТРИ! Для того чтобы остановить хакеров нужно сделать ограничитель частоты обращений."
    Mark"С помощью этого метода можно ограничить продолжительность запросов клиента до определенного времени, независимо от того, что именно он делает."
    Mark"В результате время совершения запроса ограничивается как для реального пользователя, так и для скрипта."

    scene room
    with dissolve
    Bogdan"Ну, вроде все. Теперь брутфорс-атаки нам не помеха."
    Bogdan"Но нужно проверить еще раз работоспособность нашего кода, этим займется Алина."

    scene table2
    with dissolve
    Alina"Я уже пробовала всеми методами взломать нашу защиту, но не выходит. Значит все исправно работает и это больше не повторится."

    scene room
    with dissolve
    Bogdan"Ребята, все молодцы. Кстати, сколько времени на часах."
    Bogdan"Ого, уже 5 часов утра. Мы тут всю ночь просидели. Саша тебе уже давно пара быть дома."
    Sasha17yo"Да, сейчас пойду. Но мне было так интересно провести с вами время. Я поучаствовал во всех этапах борьбы с хакерами."
    Bogdan"Надеемся мы показали тебе насколько интересна наша профессия."

    scene door
    with dissolve
    Sasha17yo"Ладно, я пошел. Всем пока!"
    Team"Пока Саша!"

    scene start
    with dissolve
    "На следующий день Саша точно решил связать свою жизнь с информационной безопасностью."
    Sasha37yo"Так я и стал кибербезопасником. Присоединяйся и ты, будущий студент."

    scene end
    with dissolve
    ""

    return
