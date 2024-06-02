
count_of_holiday = int(input())
year = int(input())
holidays = [input().lower().split() for i in range(count_of_holiday)]
beginning_day = input().lower()


months = {
    'january' : 31,
    'february' : 28,
    'march' : 31,
    'april' : 30,
    'may' : 31,
    'june' : 30,
    'july' : 31,
    'august' : 31,
    'september' : 30,
    'october' : 31,
    'november' : 30,
    'december' : 31
}

if(year % 400 == 0 or (year % 4 == 0 and year % 100 !=0)):
    months['february'] = 29

week_days = [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'
]

holiday_months = {}
for month in months.keys():
    holiday_months[month.lower()] = []

# print(holidays)

for holiday in holidays:
    # print(int(holiday[0]))
    # print(months[holiday[1]])
    # if(int(holiday[0]) >= months[holiday[1]]):
    #     continue
    holiday_months[holiday[1]] += [int(holiday[0])]

# print(holiday_months)
key_day = week_days.index(beginning_day)

week_count = [0, 0, 0, 0, 0, 0, 0]

for month in months.keys():
    for day in range(1,int(months[month])+1):
        week_count[key_day] += 1
        # print(month, day, week_days[key_day])
        if day in holiday_months[month]:
            
            for i in range(7):
                if(i == key_day):
                    continue
                week_count[i] += 1


        key_day = (key_day+1) % 7

# print(week_days(week_count.index(week_count.minzzzz))))
# print(week_days(week_count.index(max(week_count))))
# print(week_count)
week_day_min = 400
week_day_max = -1

for i in range(len(week_count)):
    if(week_count[i] < week_day_min):
        week_day_min = week_count[i]
        min_res = week_days[i]

    if(week_count[i] > week_day_max):
        week_day_max = week_count[i]
        max_res = week_days[i]

print(max_res.capitalize() + ' ' +min_res.capitalize())