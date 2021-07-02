from django import template
from ..models import Post

register=template.Library()

@register.simple_tag
def get_total_post_count():
    '''
    use in template:
        {% load my_tags %}
        {% get_total_post_count %}
    '''
    return Post.objects.all().count()


def Tags_or_Tag(count):
    '''
    use in template:
        {% load my_tags %}
        {% Tags_or_Tag 10 %}
        {% Tags_or_Tag 1 %}
        {% Tags_or_Tag Post.tags.allc.ount %}
    '''
    if count >1:
        return 'Tags:'
    else:
        return 'Tag:'    
    
