from lxml.etree import XPath, XPathSyntaxError


def validate_xpath(xpath):
    try:
        XPath(v)
        return v
    except XPathSyntaxError:
        raise ValueError("Incorrect xpath")