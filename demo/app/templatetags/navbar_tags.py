from django.template import Library
from app.models import Category
register = Library()
@register.inclusion_tag("navbar_component/navbarcomponent.html")
def navbar_tags():
    categories = Category.objects.order_by("id")
    return {"categories":categories}