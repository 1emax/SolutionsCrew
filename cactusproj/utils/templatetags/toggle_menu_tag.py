from django import template

register = template.Library()

@register.simple_tag(takes_context = True)
def toggle_menu(context):
    request = context['request']
    result = request.COOKIES.get('menu_toggle', None)
    if result and result=='true':
        return "mini-navbar"
    else:
        return ""
