from django.contrib import admin
from .models import ArticleMaster, BranchMaster, DepartmentMaster,ColorMaster,CompanyLedgerMaster, Transaction, \
    TransactionLineItemDetails, InventoryItem

# Register your models here.
@admin.register(ArticleMaster)
class AdminArticleMaster(admin.ModelAdmin):
    list_display = ['name', 'short_name','blend_pct', 'twists', 'remarks']

@admin.register(BranchMaster)
class AdminBranchMaster(admin.ModelAdmin):
    list_display = ['short_name', 'contact_person_name', 'gst_number', 'address1', 'pin_code', 'mobile']

@admin.register(DepartmentMaster)
class AdminDepartmentMaster(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ColorMaster)
class AdminColorMaster(admin.ModelAdmin):
    list_display = ['article', 'name', 'short_name']

@admin.register(CompanyLedgerMaster)
class AdminCompanyLedgerMaster(admin.ModelAdmin):
    list_display = ['name', 'gst_number' , 'supplier_status', 'address1', 'pin_code', 'mobile' , 'remarks']


@admin.register(Transaction)
class AdminTransaction(admin.ModelAdmin):
    list_display = ['unique_id', 'company','branch', 'department', 'trans_number','trans_status', 'remarks']

@admin.register(TransactionLineItemDetails)
class AdminTransactionLineItemDetails(admin.ModelAdmin):
    list_display = ['transaction', 'unique_id','article', 'color', 'date', 'quantity','rate_per_unit', 'unit']

@admin.register(InventoryItem)
class AdminInventoryItem(admin.ModelAdmin):
    list_display = ['item', 'unique_id','article', 'color', 'company', 'gross_quan','net_quan', 'unit']