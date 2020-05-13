from django import template
from django.conf import settings

register = template.Library()

HOME_MENU_ITEM = 'home'

@register.simple_tag(takes_context=True)
def get_active_menu(context):
    return HOME_MENU_ITEM
