from abc import ABC, abstractmethod

from hashlib import sha256
from tortoise.queryset import QuerySetSingle

from observer.html_tools import get_element_by_xpath_from_url, get_text_by_xpath_from_url
from models.tasks_models import Task


class PageObserver(ABC):
    """
    Interface for page observer
    """

    @abstractmethod
    async def check_update(task: QuerySetSingle[Task]) -> bool:
        pass


class ElementObserver(PageObserver):
    """
    Page observer with check_method == HTML
    """

    async def check_update(self, task: QuerySetSingle[Task]) -> bool:
        """
        Check for page update
        """
        url, xpath, prev_check_hash = await task.values_list("url", "xpath", "element_hash")
        data = await get_element_by_xpath_from_url(url=url, xpath=xpath)
        data_hash = sha256(data.encode()).hexdigest()

        return data_hash == prev_check_hash


class TextObserver(PageObserver):
    """
    Page observer with check_method == TEXT
    """

    async def check_update(self, task: QuerySetSingle[Task]) -> bool:
        """
        Check for page update
        """
        url, xpath, prev_check_hash = await task.values_list("url", "xpath", "element_hash")
        data = await get_text_by_xpath_from_url(url=url, xpath=xpath)
        data_hash = sha256(data.encode()).hexdigest()

        return data_hash == prev_check_hash
