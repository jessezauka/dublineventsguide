from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ('d', 'Draft'),
    ('h', 'Highlight'),
    ('a', 'Active'),
    ('i', 'Inactive')
]


class Original(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(editable=True)
    model = models.CharField(max_length=300, blank=True)
    image_main = models.ImageField(upload_to="original_images", blank=True)
    image_two = models.ImageField(upload_to="original_images", blank=True)
    image_three = models.ImageField(upload_to="original_images", blank=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='a'
    )
    votes = models.PositiveIntegerField(default=0)
    price_min = models.DecimalField(
        max_digits=16, decimal_places=2, default=0, blank=True
    )
    price_max = models.DecimalField(
        max_digits=16, decimal_places=2, default=0, blank=True
    )


    def __str__(self):
        return self.model


PRODUCT_STATUS_CHOICES = [
    ('p', 'Promotion'),
    ('s', 'Soldout'),
    ('o', 'Out of stock'),
    ('n', 'Not on sales'),
    ('y', 'On sales')
]

class Product(models.Model):
    title = models.CharField(max_length=300, default='')
    description = models.TextField()
    model = models.CharField(max_length=300, blank=True)
    place = models.CharField(max_length=200, default='')
    date = models.DateTimeField(editable=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0
    )
    old_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, default=0
    )
    image_main = models.ImageField(upload_to="product_images")
    image_sec = models.ImageField(upload_to="product_images", blank=True)
    status = models.CharField(
        max_length=1, choices=PRODUCT_STATUS_CHOICES, default='y'
    )
    in_stock = models.PositiveIntegerField(default=0)
    original_key = models.ForeignKey(
        Original, null=True,
        related_name='products',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.model

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    highlight = models.ForeignKey(
        Original, on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'highlight'], name='up_vote'
            )
        ]

    def __str__(self):
        return self.highlight.model
