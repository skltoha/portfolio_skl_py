from django import template

register = template.Library()

@register.simple_tag
def is_active(request, url_pattern):
    if request.path == url_pattern:
        return 'active'
    return ''
