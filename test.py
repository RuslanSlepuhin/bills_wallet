import re

from variables import variables

a = "УНЛ 291313486 РЕГ# 219004067 \ —ЧЕК ПРОДАЖИ » шЕ и ПЛАТЕЖНЫЙ ДОКУМЕНТ ° — НОМЕР ЧЕКА 31801.320.86  ‚  КАССИР 4 Евсейчик ВВ, ' 4810319018179 Творог Минская мерка 5% 180 г ! 1.69 * .3.000, бонус 0.03 5.07 ' 4810319018162 Творог Минская марка 2% 180 г ° " \
    "1.61 * 1.000, бонус 0.01 1.61 ! \n4811036044700 Хлеб темный Багач 400 г упак ( !° ' 1.68 * 1.000, бонуб .0.01 2268 4810223018616. Молоко Свежие новости ультрапе ; 2.10 * 2.000,: бонуе 002 4.2С . ‚ 55027 Окунь морской атл ВИТАЛЮР золотист г/к : " \
    "19.59 * 0.394, бонус 0.04 7.72 ; 4810268046872 Сыр полутвердый Брест-Литовск 9.99 * 1.000, бонуе 0.04 . 9.95 58062 Хурма сорт Рохо Вриллианте свеж вес 1 ^ 6.49 * 1.382, бонус 0.04 й 8.97 116895 Багет Классический 220 г 1.69 * 1.000, бонус 0.01 1.65 " \
    "Бонусная карта; х*х*ххх*8908 _ ' ='==========г_п=::::збонусы=========за:№= ‚ — Нечальный баланс бонусоВ, . у.лаалаьнае к «О.Е \ 1Ы ооа тниь в ииконнааиень мАча лИ Г. ЧЕ ОТЫН НЫ "

expr = variables.code
match = re.findall(expr, a)

pass