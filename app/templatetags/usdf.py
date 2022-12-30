from django import template

register=template.Library()



def swap(value):
    return value.swapcase()
@register.filter(name='counting')
def count(value,arg):
    return value.count(arg)
@register.filter()
def remove(value,arg):
    return value.replace(arg,'')


register.filter('swaping',swap)
#register.filter('counting',count)

