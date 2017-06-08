from django import template


register = template.Library()


@register.inclusion_tag('form/field.html')
def email_field(field):
    return {'field': field, 'type': 'email'}


@register.inclusion_tag('form/field.html')
def text_field(field):
    return {'field': field, 'type': 'text'}


@register.inclusion_tag('form/field.html')
def number_field(field):
    return {'field': field, 'type': 'number'}


@register.inclusion_tag('form/field.html')
def password_field(field):
    return {'field': field, 'type': 'password'}


@register.inclusion_tag('form/field.html')
def url_field(field):
    return {'field': field, 'type': 'url'}
