from forex_python.bitcoin import BtcConverter
from tkinter import *
from datetime import date, datetime, time
import calendar
import math

"""
Function Code
"""
def year_initialize():
    year = []
    for i in range(5):
        year.append(2021-i)
    return year

def month_initialize():
    month = []
    for i in range(12):
        month.append(i+1)
    return month

def date_initialize(selected_year=date.today().year, selected_month=date.today().month):
    day = []
    if date.today().year == selected_year:
        for avalable_day in calendar_obj.itermonthdays(selected_year, selected_month):
            if avalable_day == date.today().day and selected_month == date.today().month:
                day.append(avalable_day)
                break
            elif avalable_day != 0:
                day.append(avalable_day)
    else:
        for avalable_day in calendar_obj.itermonthdays(selected_year, selected_month):
            if avalable_day != 0:
                day.append(avalable_day)
    return day

def get_current_bitcoin_rate(*args):
    output_result = str(bitcoin_obj.get_latest_price(choice_var.get())) + " " + choice_var.get()
    today_bitcoin_rate_label.configure(text=output_result)

def average_bitcoin_rate(event):
    if (int(start_year_choice_var.get()) == int(end_year_choice_var.get()) and
        (int(start_month_choice_var.get()) == int(end_month_choice_var.get()) and
        int(start_day_choice_var.get()) >= int(end_day_choice_var.get())) or
        int(start_month_choice_var.get()) > int(end_month_choice_var.get()) or
        int(start_year_choice_var.get()) > int(end_year_choice_var.get())):
        # in case invalid input
        start_day_choice_var.set(date.today().day)
        end_day_choice_var.set(date.today().day)
        start_month_choice_var.set(date.today().month)
        end_month_choice_var.set(date.today().month)
        start_year_choice_var.set(date.today().year)
        end_year_choice_var.set(date.today().year)
        average_label.configure(text='Invalid input')
    else:
        mintime = time.min
        maxtime = time.max
        start_date_str = [start_day_choice_var.get(), start_month_choice_var.get(), start_year_choice_var.get()]
        start_date_str = "-".join(start_date_str)
        end_date_str = [end_day_choice_var.get(), end_month_choice_var.get(), end_year_choice_var.get()]
        end_date_str = "-".join(end_date_str)
        start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
        start_date = start_date.combine(start_date, mintime)
        end_date = datetime.strptime(end_date_str, '%d-%m-%Y')
        end_date = end_date.combine(end_date, maxtime)
        average_label.configure(text=cal_average_bitcoin_rate(start_date,end_date))

def cal_average_bitcoin_rate(start_date, end_date):
    avg = 0
    data_result = bitcoin_obj.get_previous_price_list(choice_var.get(), start_date, end_date)
    if data_result == {}:
        return "No data from your period"
    else:
        for key in data_result:
            avg = avg + data_result.get(key)
        avg = avg/len(data_result)
        return f"Average of Bitcoin price is {avg} {choice_var.get()}"

def recalculation(*args):
    average_label.configure(text="Currentcy is changed. Press Average for re-calculation")

"""
Parameter Declaration Code
"""
bitcoin_obj = BtcConverter()
calendar_obj = calendar.Calendar()
available_year = year_initialize()
available_month = month_initialize()
avalilable_date = date_initialize()
"""
GUI Code
"""
main_page = Tk()
day_label = Label(main_page, text='Date')
day_label.grid(row=1, column=0)
start_day_choice_var = StringVar(main_page)
start_day_choice_var.set(date.today().day)
start_day_entry = OptionMenu(main_page, start_day_choice_var, *avalilable_date)
start_day_entry.grid(row=2, column=0)
end_day_choice_var = StringVar(main_page)
end_day_choice_var.set(date.today().day)
end_day_entry = OptionMenu(main_page, end_day_choice_var, *avalilable_date)
end_day_entry.grid(row=3, column=0)
month_label = Label(main_page, text='Month')
month_label.grid(row=1, column=1)
start_month_choice_var = StringVar(main_page)
start_month_choice_var.set(date.today().month)
start_month_entry = OptionMenu(main_page, start_month_choice_var, *available_month)
start_month_entry.grid(row=2, column=1)
end_month_choice_var = StringVar(main_page)
end_month_choice_var.set(date.today().month)
end_month_entry = OptionMenu(main_page, end_month_choice_var, *available_month)
end_month_entry.grid(row=3, column=1)
year_label = Label(main_page, text='Year')
year_label.grid(row=1, column=2)
start_year_choice_var = StringVar(main_page)
start_year_choice_var.set(date.today().year)
start_year_entry = OptionMenu(main_page, start_year_choice_var, *available_year)
start_year_entry.grid(row=2, column=2)
end_year_choice_var = StringVar(main_page)
end_year_choice_var.set(date.today().year)
end_year_entry = OptionMenu(main_page, end_year_choice_var, *available_year)
end_year_entry.grid(row=3, column=2)
average_button = Button(main_page, text='Average')
average_button.bind('<Button-1>', average_bitcoin_rate)
average_button.grid(row=4, column=0)
average_label = Label(main_page, text='Average Result')
average_label.grid(row=4, column=1)
choice_var = StringVar(main_page)
choice_var.set('THB')
currentcy = ['USD','THB']
currentcy_option_menu = OptionMenu(main_page, choice_var, *currentcy)
currentcy_option_menu.grid(row=0, column=0)
today_bitcoin_rate_label = Label(main_page, text='Today Bitcoin Rate')
today_bitcoin_rate_label.grid(row=0, column=1)
main_page.after(1000, get_current_bitcoin_rate)
choice_var.trace('w', get_current_bitcoin_rate)
choice_var.trace('w', recalculation)
main_page.mainloop()