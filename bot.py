import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

BOT_TOKEN = "8420735171:AAFkw_N3O7Tp4cMKy8OEFZDDkcHlIb4I3Yk"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class TestStates(StatesGroup):
    waiting_for_answer_1 = State()
    waiting_for_answer_2 = State()
    waiting_for_answer_3 = State()
    waiting_for_answer_4 = State()
    waiting_for_answer_5 = State()
    waiting_for_answer_6 = State()
    waiting_for_answer_7 = State()
    waiting_for_answer_8 = State()
    waiting_for_answer_9 = State()
    waiting_for_answer_10 = State()

button_test = KeyboardButton(text="🧩 Пройти тест")
button_professions = KeyboardButton(text="📚 Каталог профессий")
button_ege = KeyboardButton(text="📅 Даты ЕГЭ")
button_faq = KeyboardButton(text="❔ FAQ")
button_help = KeyboardButton(text="❓ Помощь")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_test],
        [button_professions],
        [button_ege],
        [button_faq],
        [button_help],
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "Привет, выпускник! 🎓\n"
        "Я твой помощник в выборе профессии.\n\n"
        "Выбери действие:"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

@dp.message(lambda message: message.text == "📚 Каталог профессий")
async def show_professions(message: types.Message):
    categories_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💻 IT и технологии")],
            [KeyboardButton(text="🏥 Медицина и биология")],
            [KeyboardButton(text="📊 Экономика и бизнес")],
            [KeyboardButton(text="🎨 Творчество и дизайн")],
            [KeyboardButton(text="🔙 Назад в меню")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        "Выбери категорию профессий, чтобы узнать подробнее:",
        reply_markup=categories_keyboard
    )

@dp.message(lambda message: message.text == "💻 IT и технологии")
async def show_it_professions(message: types.Message):
    professions_text = (
        "💻 **IT и технологии:**\n\n"
        "• **Программист** - создает программы и приложения\n"
        "• **Data Scientist** - анализирует большие данные\n"
        "• **Веб-разработчик** - создает сайты\n"
        "• **Кибербезопасность** - защищает данные\n"
        "• **Геймдев** - разрабатывает игры\n\n"
        "📚 **Нужные предметы ЕГЭ:**\n"
        "Информатика, Математика, Физика/Русский язык"
    )
    await message.answer(professions_text)

@dp.message(lambda message: message.text == "🏥 Медицина и биология")
async def show_medical_professions(message: types.Message):
    professions_text = (
        "🏥 **Медицина и биология:**\n\n"
        "• **Врач** - лечит людей\n"
        "• **Биотехнолог** - создает новые препараты\n"
        "• **Фармацевт** - разрабатывает лекарства\n"
        "• **Ветеринар** - лечит животных\n\n"
        "📚 **Нужные предметы ЕГЭ:**\n"
        "Биология, Химия, Русский язык"
    )
    await message.answer(professions_text)

@dp.message(lambda message: message.text == "📊 Экономика и бизнес")
async def show_business_professions(message: types.Message):
    professions_text = (
        "📊 **Экономика и бизнес:**\n\n"
        "• **Маркетолог** - продвигает товары\n"
        "• **Менеджер** - управляет проектами\n"
        "• **Финансист** - работает с деньгами\n"
        "• **Аналитик** - исследует рынки\n\n"
        "📚 **Нужные предметы ЕГЭ:**\n"
        "Математика, Обществознание, Русский язык"
    )
    await message.answer(professions_text)

@dp.message(lambda message: message.text == "🎨 Творчество и дизайн")
async def show_creative_professions(message: types.Message):
    professions_text = (
        "🎨 **Творчество и дизайн:**\n\n"
        "• **Дизайнер** - создает визуальный контент\n"
        "• **Архитектор** - проектирует здания\n"
        "• **Копирайтер** - пишет тексты\n"
        "• **Фотограф/Видеограф** - создает контент\n\n"
        "📚 **Нужные предметы ЕГЭ:**\n"
        "Литература, Обществознание, Русский язык\n"
        "⚠️ *Часто требуют творческий конкурс*"
    )
    await message.answer(professions_text)

@dp.message(lambda message: message.text == "🔙 Назад в меню")
async def back_to_menu(message: types.Message):
    await message.answer(
        "Возвращаю в главное меню:",
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text == "📅 Даты ЕГЭ")
async def show_ege_dates(message: types.Message):
    dates_text = (
        "📅 **Основные даты ЕГЭ 2025:**\n\n"
        "• Русский язык - 29 мая\n"
        "• Математика - 26-27 мая\n"
        "• Информатика - 10-11 июня\n"
        "• Обществознание - 2 июня\n"
        
        "• Физика - 2 июня\n"
        "• Химия - 23 мая\n"
        "• Биология - 5 июня\n"
        "• История - 23 мая\n"
        "• Литература - 23 мая\n"
        "• Английский язык - 10-11 июня\n\n"
        "*Даты предварительные, уточняйте на официальном сайте*"
    )
    await message.answer(dates_text)

@dp.message(lambda message: message.text == "❔ FAQ")
async def show_faq(message: types.Message):
    faq_text = (
        "❔ **Частые вопросы:**\n\n"
        "• *Как выбрать вуз?* - Пройди тест и посмотри рекомендации\n"
        "• *Какие ЕГЭ сдавать?* - Зависит от направления, смотри в каталоге профессий\n"
        "• *Когда подавать документы?* - Обычно с 20 июня по 25 июля\n"
        "• *Можно ли изменить выбор?* - Да, до подачи оригиналов документов"
    )
    await message.answer(faq_text)

@dp.message(lambda message: message.text == "❓ Помощь")
async def show_help(message: types.Message):
    help_text = (
        "Я помогу тебе:\n"
        "• Определить подходящие профессии\n"  
        "• Узнать о современных направлениях\n"
        "• Понять, какие предметы ЕГЭ сдавать\n\n"
        "Просто нажимай на кнопки в меню!"
    )
    await message.answer(help_text)

@dp.message(lambda message: message.text == "🧩 Пройти тест")
async def start_test(message: types.Message, state: FSMContext):
    await ask_question_1(message, state)

async def ask_question_1(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 1/10:\n\n"
        "Какой вид деятельности тебе больше нравится?\n\n"
        "а) Работа с техникой и компьютерами\n"
        "б) Общение и помощь людям\n"
        "в) Анализ данных и расчеты\n"
        "г) Творчество и искусство"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) Техника")],
            [KeyboardButton(text="б) Общение")],
            [KeyboardButton(text="в) Анализ")],
            [KeyboardButton(text="г) Творчество")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_1)

@dp.message(TestStates.waiting_for_answer_1)
async def handle_answer_1(message: types.Message, state: FSMContext):
    await state.update_data(answer_1=message.text)
    await ask_question_2(message, state)

async def ask_question_2(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 2/10:\n\n"
        "Что тебе интереснее?\n\n"
        "а) Создавать программы и приложения\n"
        "б) Организовывать мероприятия\n"
        "в) Исследовать научные проблемы\n"
        "г) Рисовать или создавать дизайн"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) Программы")],
            [KeyboardButton(text="б) Мероприятия")],
            [KeyboardButton(text="в) Исследования")],
            [KeyboardButton(text="г) Дизайн")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_2)

@dp.message(TestStates.waiting_for_answer_2)
async def handle_answer_2(message: types.Message, state: FSMContext):
    await state.update_data(answer_2=message.text)
    await ask_question_3(message, state)

async def ask_question_3(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 3/10:\n\n"
        "Какой школьный предмет тебе нравится больше?\n\n"
        "а) Информатика\n"
        "б) Обществознание\n"
        "в) Математика\n"
        "г) Литература/Искусство"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) Информатика")],
            [KeyboardButton(text="б) Обществознание")],
            [KeyboardButton(text="в) Математика")],
            [KeyboardButton(text="г) Искусство")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_3)

@dp.message(TestStates.waiting_for_answer_3)
async def handle_answer_3(message: types.Message, state: FSMContext):
    await state.update_data(answer_3=message.text)
    await ask_question_4(message, state)

async def ask_question_4(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 4/10:\n\n"
        "Как ты предпочитаешь работать?\n\n"
        "а) Самостоятельно за компьютером\n"
        "б) В команде с другими людьми\n"
        "в) С цифрами и формулами\n"
        "г) Создавая что-то новое"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) Компьютер")],
            [KeyboardButton(text="б) Команда")],
            [KeyboardButton(text="в) Цифры")],
            [KeyboardButton(text="г) Создавать")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_4)

@dp.message(TestStates.waiting_for_answer_4)
async def handle_answer_4(message: types.Message, state: FSMContext):
    await state.update_data(answer_4=message.text)
    await ask_question_5(message, state)

async def ask_question_5(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 5/10:\n\n"
        "Что для тебя важнее в работе?\n\n"
        "а) Высокая зарплата\n"
        "б) Помощь людям\n"
        "в) Карьерный рост\n"
        "г) Творческая реализация"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) Зарплата")],
            [KeyboardButton(text="б) Помощь")],
            [KeyboardButton(text="в) Карьера")],
            [KeyboardButton(text="г) Творчество")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_5)

@dp.message(TestStates.waiting_for_answer_5)
async def handle_answer_5(message: types.Message, state: FSMContext):
    await state.update_data(answer_5=message.text)
    await ask_question_6(message, state)

async def ask_question_6(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 6/10:\n\n"
        "Какой проект тебе интереснее?\n\n"
        "а) Разработка сайта или приложения\n"
        "б) Социальная акция\n"
        "в) Аналитическое исследование\n"
        "г) Художественная выставка"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) Сайт")],
            [KeyboardButton(text="б) Акция")],
            [KeyboardButton(text="в) Исследование")],
            [KeyboardButton(text="г) Выставка")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_6)

@dp.message(TestStates.waiting_for_answer_6)
async def handle_answer_6(message: types.Message, state: FSMContext):
    await state.update_data(answer_6=message.text)
    await ask_question_7(message, state)

async def ask_question_7(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 7/10:\n\n"
        "Что тебе лучше удается?\n\n"
        "а) Логически мыслить\n"
        "б) Договариваться с людьми\n"
        "в) Решать сложные задачи\n"
        "г) Придумывать идеи"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) Логика")],
            [KeyboardButton(text="б) Договариваться")],
            [KeyboardButton(text="в) Решать задачи")],
            [KeyboardButton(text="г) Идеи")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_7)

@dp.message(TestStates.waiting_for_answer_7)
async def handle_answer_7(message: types.Message, state: FSMContext):
    await state.update_data(answer_7=message.text)
    await ask_question_8(message, state)

async def ask_question_8(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 8/10:\n\n"
        "Какую книгу ты выберешь?\n\n"
        "а) Про технологии будущего\n"
        "б) Про выдающихся лидеров\n"
        "в) Научное исследование\n"
        "г) Художественный роман"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) Технологии")],
            [KeyboardButton(text="б) Лидеры")],
            [KeyboardButton(text="в) Наука")],
            [KeyboardButton(text="г) Роман")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_8)

@dp.message(TestStates.waiting_for_answer_8)
async def handle_answer_8(message: types.Message, state: FSMContext):
    await state.update_data(answer_8=message.text)
    await ask_question_9(message, state)

async def ask_question_9(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 9/10:\n\n"
        "Кем ты видишь себя через 5 лет?\n\n"
        "а) IT-специалистом\n"
        "б) Руководителем\n"
        "в) Ученым/аналитиком\n"
        "г) Дизайнером/художником"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) IT")],
            [KeyboardButton(text="б) Руководитель")],
            [KeyboardButton(text="в) Ученый")],
            [KeyboardButton(text="г) Дизайнер")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_9)

@dp.message(TestStates.waiting_for_answer_9)
async def handle_answer_9(message: types.Message, state: FSMContext):
    await state.update_data(answer_9=message.text)
    await ask_question_10(message, state)

async def ask_question_10(message: types.Message, state: FSMContext):
    question_text = (
        "Вопрос 10/10:\n\n"
        "Что для тебя главное в профессии?\n\n"
        "а) Востребованность на рынке\n"
        "б) Возможность помогать\n"
        "в) Интеллектуальный вызов\n"
        "г) Свобода самовыражения"
    )
    
    test_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="а) Востребованность")],
            [KeyboardButton(text="б) Помощь")],
            [KeyboardButton(text="в) Вызов")],
            [KeyboardButton(text="г) Свобода")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(question_text, reply_markup=test_keyboard)
    await state.set_state(TestStates.waiting_for_answer_10)

@dp.message(TestStates.waiting_for_answer_10)
async def handle_answer_10(message: types.Message, state: FSMContext):
    await state.update_data(answer_10=message.text)
    await calculate_and_show_results(message, state)

async def calculate_and_show_results(message: types.Message, state: FSMContext):
    data = await state.get_data()
    
    scores = {"technical": 0, "social": 0, "analytical": 0, "creative": 0}
    
    for i in range(1, 11):
        answer = data.get(f'answer_{i}', '')
        if any(word in answer for word in ["а)", "Техника", "Информатика", "Зарплата", "Технологии", "IT", "Программы", "Компьютер", "Сайт", "Логика"]):
            scores["technical"] += 1
        elif any(word in answer for word in ["б)", "Общение", "Обществознание", "Помощь", "Лидеры", "Руководителем", "Мероприятия", "Команда", "Акция", "Договариваться"]):
            scores["social"] += 1
        elif any(word in answer for word in ["в)", "Анализ", "Математика", "Карьера", "Наука", "Ученым", "Исследования", "Цифры", "Исследование", "Решать задачи"]):
            scores["analytical"] += 1
        elif any(word in answer for word in ["г)", "Творчество", "Искусство", "Свобода", "Роман", "Дизайнером", "Дизайн", "Создавать", "Выставка", "Идеи"]):
            scores["creative"] += 1
    

    main_direction = max(scores, key=scores.get)
    
    directions = []
    universities = []
    
    if main_direction == "technical":
        directions = ["IT-разработка", "Инженерное дело", "Кибербезопасность", "Робототехника"]
        universities = [
            "🎓 **Технические вузы:**",
            "• МГТУ им. Баумана - лучший технический вуз",
            "• МИФИ - ядерная физика, IT, кибербезопасность", 
            "• МИСиС - материаловедение, IT, нанотехнологии",
            "• МАИ - авиация, ракетостроение, IT",
            "• МЭИ - энергетика, электроника"
        ]
    elif main_direction == "social":
        directions = ["Менеджмент", "Психология", "Маркетинг", "HR-специалист"]
        universities = [
            "🎓 **Социально-гуманитарные вузы:**",
            "• НИУ ВШЭ - экономика, менеджмент, социология",
            "• МГУ (факультет психологии) - психология",
            "• РАНХиГС - госуправление, менеджмент",
            "• МГИМО - международные отношения",
            "• РГГУ - гуманитарные науки"
        ]
    elif main_direction == "analytical":
        directions = ["Финансы", "Data Science", "Бизнес-аналитика", "Научный сотрудник"]
        universities = [
            "🎓 **Аналитические и научные вузы:**", 
            "• МГУ (мехмат, ВМК) - математика, IT, аналитика",
            "• НИУ ВШЭ - экономика, data science, аналитика",
            "• Финакадемия - финансы, банковское дело",
            "• МФТИ - фундаментальная наука, аналитика",
            "• РЭУ им. Плеханова - экономика, аналитика"
        ]
    else:  
        directions = ["Дизайн", "Геймдев", "Медиаиндустрия", "Архитектура"]
        universities = [
            "🎓 **Творческие вузы:**",
            "• МАРХИ - архитектура, дизайн",
            "• ВГИК - кино, медиаискусство",
            "• Строгановка - промышленный дизайн",
            "• МГХПА - художественные промыслы",
            "• Институт кино и телевидения - медиа"
        ]
    
    if main_direction != "technical":
        universities.extend([
            "",
            "💻 **IT-направление (рекомендуем):**",
            "• МГТУ им. Баумана - программирование",
            "• НИУ ВШЭ - computer science", 
            "• МИСиС - IT, data science"
        ])
    
    result_text = (
        "🎯 **Результаты теста:**\n\n"
        f"Технические навыки: {scores['technical']}/10\n"
        f"Социальные навыки: {scores['social']}/10\n"
        f"Аналитические навыки: {scores['analytical']}/10\n"
        f"Творческие навыки: {scores['creative']}/10\n\n"
        "**Тебе подходят:**\n" + "\n".join(f"• {d}" for d in directions) +
        "\n\n" + "\n".join(universities)
    )
    
    await message.answer(result_text, reply_markup=keyboard)
    await state.clear()

if __name__ == "__main__":
    print("Бот запущен!")
    dp.run_polling(bot)