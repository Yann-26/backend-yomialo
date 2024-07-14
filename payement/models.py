from django.db import models

class Payment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]

    transaction_id = models.CharField(max_length=100, unique=True)
    site_id = models.CharField(max_length=100)
    trans_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    signature = models.CharField(max_length=256)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    cel_phone_num = models.CharField(max_length=20, null=True, blank=True)
    phone_prefix = models.CharField(max_length=10, null=True, blank=True)
    language = models.CharField(max_length=10, null=True, blank=True)
    version = models.CharField(max_length=10, null=True, blank=True)
    payment_config = models.CharField(max_length=50, null=True, blank=True)
    page_action = models.CharField(max_length=50, null=True, blank=True)
    custom = models.CharField(max_length=256, null=True, blank=True)
    designation = models.CharField(max_length=256, null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.transaction_id} - {self.amount} {self.currency} - {self.get_status_display()}"
