#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
# Объект бота
bot = Bot(token="5698707049:AAFY30CaL-vL8-LIJMvI58VZKJ9jq_kMTxE")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
@dp.message_handler(commands="start")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Какие документы нужны для утверждения \nнаучных консультантов докторантов?", callback_data="V12"))
    keyboard.add(types.InlineKeyboardButton(text="Я получил приглашение на стажировку, какие документы мне необходимо собрать?", callback_data="V2"))
    await message.answer("Выберите вопрос:", reply_markup=keyboard)

@dp.callback_query_handler(text="V12")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(text="1. Форма №1. "
                                   "\n2. Резюме отечественного и зарубежного консультантов. "
                                   "\n3. Письмо согласие отечественного и зарубежного консультантов. "
                                   "\n4. Информация по цитируемости и публикациям предполагаемых научных консультантов из баз данных Clarivate Analytics (Web of Science Core Collection) и Scopus."
                                   "\n5. Список наиболее значимых публикаций (в РК, странах ближнего и дальнего зарубежья) предполагаемых научных консультантов по теме исследования докторанта за последние 5 лет.")
@dp.callback_query_handler(text="V2")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(text='- Заявление на имя ректора о командировании обучающегося за границу (пишется в печатном виде), важно писать ФИО по удостоверению;'
                                   '\n- Копия приглашения с нотариально заверенным переводом на государственный или русский языки с указанием периода пребывания, цели поездки '
                                   '\n(нотариально заверяется оригинал перевода); если приглашение на русском языке, нужно поставить печать факультета и подпись декана факультета.'
                                   '\n- Программу стажировки и понедельный план, утвержденные Университетом и принимающей организацией.'
                                   '\n- Выписка из заседания кафедры о разрешении на выезд обучающегося'
                                   '\n- Выписка из заседания Ученого совета факультета о разрешении на выезд обучающегося;'
                                   '\n- Смета расходов на командировку'
                                   '\n- Языковой сертификат (при прохождении стажировки на иностранном языке) английский язык: Test of English as a Foreign Language Institutional Testing'
                                   '\n- Programm (TOEFL ITP) пороговый балл – не менее 163баллов, Test of English as a Foreign Language Institutional Testing Programm Internet-based Test (TOEFL IBT), '
                                   '\nпороговый балл – не менее 60, Test of English as a Foreign Language Paper-based testing (TOEFL PBT), '
                                   '\nпороговый балл – не менее 498, Test of English as a Foreign Language Paper-delivered testing (TOEFL PDT), '
                                   '\nпороговый балл – не менее 65, International English Language Tests System (IELTS) пороговый балл – не менее 6.0. '
                                   '\nИ/или немецкий язык: Deutsche Sprachpruеfung fuеr den Hochschulzugang (DSH, Niveau С1/уровень C1), '
                                   '\nTestDaF-Prufung (тестдаф-прюфун) (Niveau C1/уровень C1). И/или французский язык: Test de Franзais International™ – (TFI) – '
                                   '\nне ниже уровня В1 по секциям чтения и аудирования), Diplome d’Etudes en Langue franзaise (DELF), уровень B2), '
                                   '\nDiplome Approfondi de Langue franзaise – (DALF (ДАЛФ), уровень C1), Test de connaissance du franзais – (TCF) – не менее 50 баллов).')
@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
