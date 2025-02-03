import atexit

import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from fast_grpc import FastGRPC

from schedules.observer_jobs import check_sites
from grpc_service.grpc_client import telegram_bot_client


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
    telegram_bot_client.start()


async def on_shutdown():
    telegram_bot_client.stop()
    pass


async def main():
    await on_startup


if __name__ == "__main__":
    asyncio.run(main)