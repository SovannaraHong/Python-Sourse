import calendar
from rich.console import Console
from rich.table import Table

def colorful_calendar(year):
    console = Console()
    month=[calendar.monthcalendar((year,m) for m in range(1,13))]

    for month in range(12):
        month_name =calendar.month_name[month+1]