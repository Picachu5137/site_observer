from abc import ABC, abstractmethod
from typing import Callable, Awaitable

from hashlib import sha256
from loguru import logger
from tortoise.queryset import QuerySetSingle

from observer.html_tools import get_element_by_xpath_from_url, get_text_by_xpath_from_url
from models.tasks_models import Task
from grpc_service.grpc_client import telegram_bot_client


class PageObserver:
    CHECK_METHOD = {
        "TEXT": get_text_by_xpath_from_url,
        "HTML": get_element_by_xpath_from_url,
    }

    @staticmethod
    def calculate_hash(data: str) -> str:
        return sha256(data.encode()).hexdigest()

    def __init__(self, task: Task):
        self.task = task

    async def detect_page_changes(self):
        check_method = self.task.check_method
        if check_method in self.CHECK_METHOD:
            fetch_method = self.CHECK_METHOD[check_method]
            is_updated = await self.check_update(fetch_method)

            if is_updated:
                await self.handle_page_changes()

    async def handle_page_changes(self):
        logger.debug(f"Page on task {self.task.id} changes detected")

    async def check_update(self, fetch_method: Callable[[str, str], Awaitable]) -> bool:
        """
        Check for text update on page
        """
        url, xpath, prev_check_hash = self.task.url, self.task.xpath, self.task.element_hash
        data = await fetch_method(url, xpath)
        data_hash = PageObserver.calculate_hash(data)

        return data_hash == prev_check_hash

