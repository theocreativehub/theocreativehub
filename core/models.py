from django.db import models

from django.db import models
import uuid
from django.db import models


class Order(models.Model):
    order_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    client_name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=200)

    STATUS_CHOICES = [
        ('Pending Payment', 'Pending Payment'),
        ('In Progress', 'In Progress'),
        ('Ready For Download', 'Ready For Download'),
    ]

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending Payment'
    )

    progress = models.IntegerField(default=0)

    delivery_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    preview_image = models.ImageField(
        upload_to='previews/',
        blank=True,
        null=True
    )

    final_file = models.FileField(
        upload_to='deliveries/',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = f"TCH-{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id

class Portfolio(models.Model):
        title = models.CharField(max_length=200)
        image = models.ImageField(upload_to='portfolio/')
        category = models.CharField(max_length=100)

        def __str__(self):
            return self.title
class Comment(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.order_id

class AdminReply(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.order_id