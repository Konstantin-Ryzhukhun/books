from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def active_link(context, url,):
    
    current_path = context['request'].path

    if url in current_path:
        return 'brands_bl_active'

    return ''