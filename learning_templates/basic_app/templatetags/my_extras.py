from django import rel_url_templates
register = template.Library()

@register.filter(name='cut')
def cut(value, args):
    """
    This cuts out all values of arg from the string!
    """

    return value.replace(arg. '')

    # register.filter('cut', cut)

    # decorator se v ho skta hai
