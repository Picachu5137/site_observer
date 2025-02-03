from typing import Optional, Any, Dict

from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader("templates", "messages"),
    autoescape=select_autoescape(["html"])
)

def render_template(template_name: str, values: Optional[Dict[str, Any]]=None, **kwargs):
    """
    Render template
    """

    template = env.get_template(template_name)

    if values:
        rendered_template = template.render(values, **kwargs)
    else:
        rendered_template = template.render(**kwargs)

    return rendered_template
