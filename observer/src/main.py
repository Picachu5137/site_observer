import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from fast_grpc import FastGRPC

from observer.src.schedules.observer_jobs import check_sites

app = FastGRPC(
        service_name="ObserverService",
        proto="proto/observe.proto",
        auto_gen_proto=True
    )

scheduler = AsyncIOScheduler()


async def on_startup():
    scheduler.add_job(
        check_sites,
        "interval",
        hours=1,
    )

    scheduler.start()

    app.run()


async def on_shutdown():
    pass

