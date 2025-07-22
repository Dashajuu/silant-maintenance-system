from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag
def dynamic_url(view_name_prefix, item_name, pk):
    view_name = f"{view_name_prefix}_{item_name}"
    try:
        return reverse(view_name, args=[pk])
    except NoReverseMatch:
        return "#"


@register.simple_tag(takes_context=True)
def has_model_perm(context, permission_type, model_name):
    request = context['request']
    perm_codename = f"{permission_type}_{model_name}"
    return request.user.has_perm(f"machines.{perm_codename}")