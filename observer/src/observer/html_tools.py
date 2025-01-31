import httpx
from lxml import html


async def get_element_by_xpath_from_url(url: str, xpath: str) -> str:
    html = await get_site_html(url=url)
    element = get_element_by_xpath_from_html(html=html, xpath=xpath)

    return element


async def get_text_by_xpath_from_url(url: str, xpath: str) -> str:
    html = await get_site_html(url=url)
    text = get_text_by_xpath_from_html(html=html, xpath=xpath)

    return text


async def get_site_html(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)

    return response.text


def get_element_by_xpath_from_html(html_text: str, xpath: str) -> str:
    tree = html.fromstring(html=html_text)
    element = tree.xpath(xpath)

    return element


def get_text_by_xpath_from_html(html_text: str, xpath: str) -> str:
    element = get_element_by_xpath_from_html(html_text=html_text, xpath=xpath)
    
    return element.text_content().strip()
