import datetime
from .models import *
from django.db.models import Q


def trans_number_custom():
    last_tn=Transaction.objects.all().order_by("unique_id").last()
    if not last_tn:return "TRN/" + '0000/' + str(datetime.date.today().year)
    trans_number = last_tn.trans_number
    last_count = int(trans_number[4:8])
    last_year = int(trans_number[9:13])
    new_year = datetime.date.today().year
    if new_year == last_year:new_count = last_count+1
    else:new_count=0
    return "TRN/" + str(new_count).zfill(4) + "/"+ str(new_year)

def CreateLineItem(trans_number, **item):
    article_data = item.pop('article')
    color_data = item.pop('color')
    article_inst = ArticleMaster.objects.get(name=article_data['name'])

    # """Colour chosen should have a link with chosen article."""
    # check_color=ColorMaster.objects.filter(Q(article=article_inst) & Q(name=color_data['name'])).exist()
    # if check_color:color_inst = ColorMaster.objects.get(article=article_inst, name=color_data['name'])

    color_inst=ColorMaster.objects.get(article=article_inst, name=color_data['name'])
    transaction = Transaction.objects.get(trans_number=trans_number)

    """Two line items in a transaction cant have same combination of article and colour"""
    check = TransactionLineItemDetails.objects.filter(Q(article=article_inst) & Q(color=color_inst) & Q(transaction__trans_number = trans_number)).exist()
    if not check:
        item_created = TransactionLineItemDetails.objects.create(transaction=transaction, article=article_inst,
                                                         color=color_inst, **item)


def CreateInventory(item_unique_id, **inventory):
    article_data = inventory.pop('article')
    color_data = inventory.pop('color')
    company_data = inventory.pop('company')
    item_inst = TransactionLineItemDetails.objects.get(unique_id=item_unique_id)
    article_inst = ArticleMaster.objects.get(name=article_data['name'])
    color_inst = ColorMaster.objects.get(name=color_data['name'])
    company_inst = CompanyLedgerMaster.objects.get(name=company_data['name'])
    invantory = InventoryItem.objects.create(item=item_inst, article=article_inst, color=color_inst,
                                             company=company_inst, **inventory)