from django.db import models


class BranchMaster(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    contact_person_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.short_name

    class Meta:
        db_table = 'BranchMaster'

class DepartmentMaster(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'DepartmentMaster'

class CompanyLedgerMaster(models.Model):
    name = models.CharField(max_length=32, unique=True)
    gst_number = models.CharField(max_length=20, unique=True)
    supplier_status = models.BooleanField(default=False)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CompanyLedgerMaster'

class ArticleMaster(models.Model):
    name = models.CharField(max_length=80, unique=True)
    short_name = models.CharField(max_length=50, unique=True)
    blend_pct = models.CharField(max_length=50)
    twists = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ArticleMaster'



class ColorMaster(models.Model):
    article = models.ForeignKey(ArticleMaster, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=20)
    remarks = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ColorMaster'
# Create your models here.


# specifying Teansactin status choices

TRANS_CHOICES = (
    ("PENDING", "PENDING"),
    ("COMPLETED", "COMPLETED"),
    ("CLOSE", "CLOSE"),
)

# specifying Unit choices
UNIT_CHOICES = (
    ("KG", "KG"),
    ("METER", "METER")
    )



class Transaction(models.Model):
    unique_id=models.AutoField(primary_key = True)
    company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE)
    branch = models.ForeignKey(BranchMaster, on_delete=models.CASCADE)
    department = models.ForeignKey(DepartmentMaster, on_delete=models.CASCADE)
    trans_number = models.CharField(max_length = 20, default =None, editable=False, unique=True)
    trans_status =models.CharField(
            max_length=20,
            choices=TRANS_CHOICES,
            default='1')
    remarks = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.trans_status

    class Meta:
        db_table = 'Transaction'




class TransactionLineItemDetails(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="items")
    unique_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(ArticleMaster, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorMaster, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    rate_per_unit = models.IntegerField()
    unit = models.CharField(max_length=35, choices = UNIT_CHOICES, default='1')


    class Meta:
        db_table = 'TransactionLineItemDetails'


class InventoryItem(models.Model):
    item=models.ForeignKey(TransactionLineItemDetails, on_delete=models.CASCADE, related_name="inventory")
    unique_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(ArticleMaster, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorMaster, on_delete=models.CASCADE)
    company=models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE)
    gross_quan = models.DecimalField(max_digits=5, decimal_places=2)
    net_quan = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=35, choices=UNIT_CHOICES, default="1")


    class Meta:
        db_table = 'InventoryItem'
