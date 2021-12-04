day = {1 : 'Monday',
       2 : 'Tuesday',
       3 : 'Wednesday',
       4 : 'Thursday',
       5 : 'Friday',
       6 : 'Saturday',
       7 : 'Sunday',
}
choise_day = int(input())
print(day.get(choise_day, 'Ошибка'))
