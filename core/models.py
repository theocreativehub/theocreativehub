from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=20, unique=True)

    client_name = models.CharField(max_length=100)
    customer_email = models.EmailField(blank=True, null=True)

    project_name = models.CharField(max_length=200)

    momo_reference = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    STATUS_CHOICES = [
        ('Pending Payment', 'Pending Payment'),
        ('In Progress', 'In Progress'),
        ('Ready For Download', 'Ready For Download'),
        ('Completed', 'Completed'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending Payment'
    )

    progress = models.IntegerField(default=0)

    delivery_date = models.DateField()

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