import pendulum
from airflow.timetables.events import EventsTimetable

dates = [
    "2019-01-30",
    "2019-02-24",
    "2019-03-31",
    "2019-05-01",
    "2019-05-31",
    "2019-06-30",
    "2019-07-30",
    "2019-09-01",
    "2019-09-30",
    "2019-10-31",
    "2019-11-30",
    "2019-12-31",
    "2020-01-31",
    "2020-02-29",
    "2020-03-23",
    "2020-04-30",
    "2020-05-31",
    "2020-06-29",
    "2020-10-30",
    "2020-11-30",
    "2020-12-31",
    "2021-01-30",
    "2021-02-27",
    "2021-03-30",
    "2021-04-30",
    "2021-06-29",
    "2021-07-23",
    "2021-08-30",
    "2021-09-30",
    "2021-10-30",
    "2021-11-30",
    "2021-12-30",
    "2022-01-30",
    "2022-02-27",
    "2022-03-31",
    "2022-04-30",
    "2022-05-26",
    "2022-06-29",
    "2022-07-31",
    "2022-08-31",
    "2022-09-28",
    "2022-10-31",
    "2022-11-30",
    "2022-12-31",
    "2023-01-31",
    "2023-02-28",
    "2023-03-31",
    "2023-04-30",
    "2023-05-31",
    "2023-06-30",
    "2023-07-31",
    "2023-08-30",
    "2023-09-25",
    "2023-10-31",
    "2023-11-30",
    "2023-12-31",
    "2024-01-31",
    "2024-02-29",
    "2024-03-31",
    "2024-04-30",
    "2024-05-31",
    "2024-06-30",
    "2024-07-31",
    "2024-08-31",
    "2024-09-30",
    "2024-10-31",
    "2024-11-30",
    "2024-12-31",
]


def get_schedule(start=0):
    event_dates = []
    for ds in dates:
        y, m, d = map(int, tuple(ds.split("-")))
        event_dates.append(pendulum.datetime(y, m, d))

    event_dates = event_dates[start:]
    schedule = EventsTimetable(
        event_dates=event_dates,
        description="Airbnb schedule",
        restrict_to_events=True,
    )
    if len(event_dates) < 10:
        desc = "["
        for d in event_dates[:-1]:
            desc += f"{str(d.date())}, "
        desc += f"{str(event_dates[-1].date())}]"
        schedule.description = desc
    else:
        d = [str(d.date()) for d in event_dates]
        schedule.description = f"[{d[0]}, {d[1]}, {d[2]}, ..., {d[-3]}, {d[-2]}, {d[-1]}]"
    return schedule
