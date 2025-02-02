from abc import ABC, abstractmethod
from typing import Callable, Awaitable

from hashlib import sha256
from tortoise.queryset import QuerySetSingle

from observer.html_tools import get_element_by_xpath_from_url, get_text_by_xpath_from_url
from models.tasks_models import Task
from grpc.grpc_stub import


class Page:
    CHECK_METHOD = {
        "TEXT": get_text_by_xpath_from_url,
        "HTML": get_element_by_xpath_from_url,
    }

    @staticmethod
    def calculate_hash(data: str) -> str:
        return sha256(data.encode()).hexdigest()

    def __init__(self, task: QuerySetSingle[Task]):
        self.task = task

    async def detect_page_changes(self):
        check_method = await self.task.values_list("check_method", flat=True)
        if check_method in self.CHECK_METHOD:
            fetch_method = self.CHECK_METHOD[check_method]
            is_updated = await self.check_update(fetch_method)

            if is_updated:
                await self.handle_page_changes()

    async def handle_page_changes(self):


    async def check_update(self, fetch_method: Callable[[str, str], Awaitable]) -> bool:
        """
        Check for text update on page
        """
        url, xpath, prev_check_hash = await self.task.values_list("url", "xpath", "element_hash")
        data = await fetch_method(url, xpath)
        data_hash = Page.calculate_hash(data)

        return data_hash == prev_check_hash

    @staticmethod
    async def check_element_update(task: QuerySetSingle[Task]) -> bool:
        """
        Check for html update on page
        """
        url, xpath, prev_check_hash = await task.values_list("url", "xpath", "element_hash")
        data = await get_text_by_xpath_from_url(url=url, xpath=xpath)
        data_hash = sha256(data.encode()).hexdigest()

        return data_hash == prev_check_hash
