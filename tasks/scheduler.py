from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.triggers.cron import CronTrigger
from .jobs import exchangeDateNow


def initialize():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # tarea que guarda los precios de comopraventa del dolar
    scheduler.add_job(
        exchangeDateNow,
        trigger=CronTrigger(hour=8),
        id="exchanges",
        replace_existing=True,
    )

    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()
