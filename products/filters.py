import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    place = django_filters.AllValuesFilter(
        field_name="place"
    )
    title = django_filters.AllValuesFilter(
        field_name="title"
    )

    o = django_filters.OrderingFilter(
        fields={
            ('date', 'date'),
            ('price', 'price')
        }
    )

    class Meta:
        fields = ['place', 'title']
