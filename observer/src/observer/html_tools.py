import httpx
from lxml import html


async def get_element_by_xpath_from_url(url: str, xpath: str) -> str:
    html_content = await get_site_html(url=url)
    element = get_element_by_xpath_from_html(html_text=html_content, xpath=xpath)

    return element


async def get_text_by_xpath_from_url(url: str, xpath: str) -> str:
    html_content = await get_site_html(url=url)
    text = get_text_by_xpath_from_html(html_text=html_content, xpath=xpath)

    return text


async def get_site_html(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)

    return response.text


# TODO: доделать логику получения элемента/текста из html
def get_element_by_xpath_from_html(html_text: str, xpath: str) -> html.XP:
    tree = html.fromstring(html=html_text)
    element = tree.xpath(xpath)

    return element[0] if element else ""


def get_text_by_xpath_from_html(html_text: str, xpath: str) -> str:
    element = get_element_by_xpath_from_html(html_text=html_text, xpath=xpath)
    
    return element.text_content().strip() if element != "" else ""
