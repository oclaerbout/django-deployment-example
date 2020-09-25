from django import template

register = template.Library()

@register.filter(name='knip')
def knip(value,arg):
    """
    Dit knipt alle "arg" waarden van de string!
    """
    return value.replace(arg,'')

# register.filter('knip',knip)
# De eerste knip is hoe we de filter willen noemen, de tweede knip is de naam van de functie hierboven

# cfr python level 2 - decorators: hier kan je ook met decorators werken. om dit te doen:
# register.filter('knip',knip) (regel 12 hier) wordt in commentaar gezet
# en @register.filter(name='cut') (regel 5) wordt toegevoegd.

