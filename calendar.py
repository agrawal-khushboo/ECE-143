import calendar
def number_of_days(year,month):
    """
    Write a function that returns the number of calendar days in a given year and month. 
    """
    assert year>0
    assert type(year)==int
    assert type(month)==int
    assert 1<=month<=12
    days=calendar.monthrange(year,month)[1]
    return days

def number_of_leap_years(year1,year2):
    """
    Write a function to find the number of leap-years between (including both endpoints) two given years. 
    """
    assert year1>0
    assert year2>0
    assert type(year1)==int
    assert type(year2)==int
    assert year2>=year1
    c=0
    for y in range(year1,year2+1):
        d=number_of_days(y,2)
        if d==29:
            c+=1
    return c
def get_day_of_week(year,month,day):
    """
    Write a function to find the string name (e.g., Monday, Tuesday) 
    of the day of the week on a given month,day, and year.
    """
    assert type(year)==int
    assert year>0
    assert type(month)==int
    assert 1<=month<=12
    assert type(day)==int
    days=number_of_days(year,month)
    assert day<=days
    d=calendar.weekday(year,month,day)
    if d==0:
        return 'Monday'
    elif d==1:
        return 'Tuesday'
    elif d==2:
        return 'Wednesday'
    elif d==3:
        return 'Thursday'
    elif d==4:
        return 'Friday'
    elif d==5:
        return 'Saturday'
    elif d==6:
        return 'Sunday'
