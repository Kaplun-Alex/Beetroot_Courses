#   Проанализируйте прилагаемый лог и найдите сколько байт было потрачено \
#   на трафик для всех ответов с кодом "200" (предпоследнее значение). \
#   Сравните его с общим трафиком.

log = open('access-log', 'r')

ful_traf_gen = (int(line.split()[-1]) for line in log if line.split()[-1] != '-') # Всего по логу
summ_ful_traf_gen = sum(i for i in ful_traf_gen)
print(summ_ful_traf_gen)
log.close()

fog = open('access-log', 'r') #   Оч странно файл вроди никто не закрывал или его занял предыдущий генер, братухе непонятно!!!
dveste_traf_gen = (int(line.split()[-1]) for line in fog if line.split()[-2] == '200' and line.split()[-1] != '-')
summ_dveste_traf_gen = sum(j for j in dveste_traf_gen)
print(summ_dveste_traf_gen)
fog.close()

# 2. Проанализируйте прилагаемый лог и найдите сколько байт было потрачено \
# на трафик для всех ответов с кодом "404" (предпоследнее значение).
jog = open('access-log', 'r')
tchitirista_tchitiri_gen = (int(line.split()[-1]) for line in jog if line.split()[-2] == '404' and line.split()[-1] != '-')
summ_tchitirista_tchitiri_gen = sum(t for t in tchitirista_tchitiri_gen)
print(summ_tchitirista_tchitiri_gen)
jog.close()

#   3. Проанализируйте прилагаемый лог и попробуйте найти общее количество всех запросов без исключения.
# Указание - можно использовать ленивый вариант подсчета, например так:
dog = open('access-log', 'r')
count_gen = (line.split()[-1] for line in dog)
summ_count_gen = sum(1 for c in count_gen)
print(summ_count_gen)
dog.close()

#   4. Проанализируйте прилагаемый лог и найдите количество всех ответов\
#   с кодом "200" (предпоследнее значение).
sog = open('access-log', 'r')
count_dv_gen = (line.split()[-1] for line in sog if line.split()[-2] == '200')
summ_count_dv_gen = sum(1 for c in count_dv_gen)
print(summ_count_dv_gen)
sog.close()


#   5. Проанализируйте прилагаемый лог и найдите количество всех ответов с\
#   кодом "404" (предпоследнее значение).
hog = open('access-log', 'r')
count_tch_gen = (line.split()[-1] for line in hog if line.split()[-2] == '404')
summ_count_tch_gen = sum(1 for c in count_tch_gen)
print(summ_count_tch_gen)
hog.close()

#   6. Найдите сколько в среднем байт тратится на запрос 200 и на запрос 404
tog = open('access-log', 'r')
midle_dv_gen = (line.split()[-1] for line in tog if line.split()[-2] == '200')
summ_midle_dv_gen = summ_dveste_traf_gen/sum(1 for c in midle_dv_gen)
print(summ_midle_dv_gen)
tog.close()

kog = open('access-log', 'r')
midle_tch_gen = (line.split()[-1] for line in kog if line.split()[-2] == '404')
summ_midle_tch_gen = summ_tchitirista_tchitiri_gen/sum(1 for c in midle_tch_gen)
print(summ_midle_tch_gen)
kog.close()
print('*********************************************************************************')
#   7. Получите и отсортируйте список всех уникальных ip-адресов с которых приходили запросы.
iphneg = open('access-log', 'r')
iphneg_gen = (ip.split()[0] for ip in iphneg)
sort_iphneg_gen = set(ip for ip in iphneg_gen) #    через set все вхэрачили!)))
for ip in sort_iphneg_gen:
    print(ip)
iphneg.close()
print('*********************************************************************************')
#   8. Посчитайте сколько было уникальных ip-адресов с которых приходили запросы.
countiphneg = open('access-log', 'r')
count_iphneg_gen = (ip.split()[0] for ip in countiphneg)
count_sort_iphneg_gen = sum(1 for c in set(ip for ip in count_iphneg_gen)) # генератор сгенерил генератор чттобы завести генетарот от генератора%)
print(count_sort_iphneg_gen)
countiphneg.close()

print('*********************************************************************************')
#   9. Выберите только те ip, запросы с которых приходили в первой\
#   половине дня (с 0000 до 1200) по местному времени.
data_time = open('access-log', 'r')
data_time_gen = (d.split()[0] for d in data_time if float((d.split()[-7][-8:][:-3]).replace(':', '.')) <= float(12))  #ААААААА! Зашквар!\
# Отрезал сконца 7го елемента строки так что дата погоды не делает
sort_data_time_gen = set(ip for ip in data_time_gen)
am_count = sum(1 for c in sort_data_time_gen)
for i in sort_data_time_gen:
    print(i)
data_time.close()
print('*********************************************************************************')
#   10. Когда больше людей ходит на сайт - до полудня или после полудня?
pm_data_time = open('access-log', 'r')
pm_data_time_gen = (d.split()[0] for d in pm_data_time if float((d.split()[-7][-8:][:-3]).replace(':', '.')) >= float(12))
sort_pm_data_time_gen = set(ip for ip in pm_data_time_gen)
pm_count = sum(1 for c in sort_pm_data_time_gen)
for i in sort_pm_data_time_gen:
    print(i)
data_time.close()
print('*********************************************************************************')
print('AM - ', am_count, 'PM - ', pm_count) # Уточню, людей, а значит количество отзаSETченных айпишнегов
