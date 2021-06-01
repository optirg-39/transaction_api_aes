from rest_framework import serializers
from . models import *

class InventorySerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField(many=False, read_only=True)
    color = serializers.StringRelatedField(many=False, read_only=True)
    company = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = InventoryItem
        fields =['unique_id','article', 'color', 'company', 'gross_quan','net_quan', 'unit']

class ItemSerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField(many=False, read_only=True)
    color = serializers.StringRelatedField(many=False, read_only=True)
    inventory = InventorySerializer(many=True)
    class Meta:
        model = TransactionLineItemDetails
        fields = ["unique_id",'article', 'color', 'date', 'quantity','rate_per_unit', 'unit','inventory']

class TransactionSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(read_only=True, many=False)
    branch = serializers.StringRelatedField(read_only=True, many=False)
    department = serializers.StringRelatedField(read_only=True, many=False)
    items = ItemSerializer(many=True)
    class Meta:
        model = Transaction
        fields = ["unique_id",'company', 'branch', 'department', 'trans_number','trans_status', 'remarks','items']


class transSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["unique_id",'company', 'branch', 'department', 'trans_number','trans_status', 'remarks','items']




