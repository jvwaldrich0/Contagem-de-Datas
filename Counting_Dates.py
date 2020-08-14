#----------------- Importações ---------------------------#
from datetime import date
#-------------- Método da Escolha 2 ----------------------#
def Calculate(syear, smonth, sday):
    import self
    self.sday = sday
    self.smonth = smonth
    self.syear = syear

    fday = self.sday
    fmonth = self.smonth
    fyear = self.syear
    final_day2 = date(fyear, fmonth, fday)

    year = int(final_day2.year)
    month = int(final_day2.month)
    day = int(final_day2.day)

    max = int(input('Dia máximo: '))

    try:
        for x in range(max):
            try:
                print(final_day2.replace(year=year, month=month, day=day))
            except ValueError:
                if month == 1 or 3 or 5 or 7 or 8 or 10:
                    day = 1
                    month += 1
                elif month == 4 or 6 or 9 or 11:
                    day = 1
                    month += 1
                elif month == 2:
                    day = 1
                    month += 1
            else:
                day += 1
                if (month >= 12) and (day > 31):
                    day = 1
                    month = 1
                    year += 1
    except ValueError:
        print('Deu merda')
    else:
        final_day = date(year, month, day)
        eday = int(final_day.day)
        emonth = int(final_day.month)
        eyear = int(final_day.year)
        return final_day
#-------------------- Datas ------------------------------#
#Data de início -------------------------------------------
print('Qual data você deseja começar a contagem?:')
sday = int(input('Dia: '))
smonth = int(input('Mês: '))
syear = int(input('Ano: '))
start_date = date(syear,smonth,sday)
year = int(start_date.year)
month = int(start_date.month)
day = int(start_date.day)
#Data Fim -------------------------------------------------
choice = int(input('''
Qual data você deseja terminar a contagem?:

1 -------------------------- Data especifica;
2 -------------------------- Ditar numero max. de dias
Qualquer outro numero ------ Dia de hoje;

Resposta: '''))
while choice == 1:
    print('Qual data você deseja terminar a contagem então?:')
    fday = int(input('Dia: '))
    fmonth = int(input('Mês: '))
    fyear = int(input('Ano: '))
    if date(fyear,fmonth,fday) >= date(syear,smonth,sday):
        final_day = date(fyear, fmonth, fday)
        break
    else:
        print('Você digitou uma data menor do que a de início\n')
if choice == 2:
    dayspass = Calculate(syear=syear,smonth=smonth,sday=sday)
    fday = dayspass.day
    fmonth = dayspass.month
    fyear = dayspass.year
    final_day = dayspass
elif choice != 1 or 2:
    final_day = date.today()
    fday = final_day.today().day
    fmonth = final_day.today().month
    fyear = final_day.today().year
#-----------------------Loop------------------------------#
while True:
    try:
        print(start_date.replace(year=year, month=month, day=day))
        if start_date.replace(year=year, month=month, day=day) == final_day.replace(year=fyear, month=fmonth, day=fday):
            if choice != 2:
                print('Contagem de dias = ', str(final_day - start_date)[0:9])
                break
            else:
                break
    except ValueError:
        if month == 1 or 3 or 5 or 7 or 8 or 10:
            day = 1
            month += 1
        elif month == 4 or 6 or 9 or 11:
            day = 1
            month += 1
        elif month == 2:
            day = 1
            month += 1
    else:
        day += 1
        if (month >= 12) and (day > 31):
            day = 1
            month = 1
            year += 1
#---------------------------------------------------------#