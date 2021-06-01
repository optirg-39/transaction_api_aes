from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .functions import *
import io
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.response import Response
from rest_framework import status



class TransectionAPI(APIView):

    """View a transaction with all its line items and their inventory items."""
    def get(self, request, str_1, num_1, num_2):
        num = str(num_1).zfill(4)
        trans_number=f"{str_1}/{num}/{num_2}"
        transaction =Transaction.objects.get(trans_number=trans_number)
        serializer = TransactionSerializer(transaction)
        return Response({"data" : serializer.data, "message": "data of transaction with all its line items and their "
                                                              "inventory items"}, status=status.HTTP_200_OK)

    """Add a transaction with its line items."""
    def post(self, request, format=None):
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        items_data = python_data.pop('line_items')
        company_data = python_data.pop('company')
        branch_data = python_data.pop('branch')
        department_data = python_data.pop('department')
        company_inst = CompanyLedgerMaster.objects.get(name = company_data['name'])
        branch_inst = BranchMaster.objects.get(short_name=branch_data['short_name'])
        department_inst = DepartmentMaster.objects.get(name = department_data['name'])
        transaction = Transaction.objects.create(company=company_inst, branch=branch_inst, department =
        department_inst, trans_number= trans_number_custom(), **python_data)
        serializer = transSerializer(transaction)
        print(serializer.data)
        trans_number = serializer.data['trans_number']

        for item in items_data:
            CreateLineItem(trans_number, **item)

        return Response({"data":"", "message": "add transaction with its line items"}, status=status.HTTP_200_OK)

    """Delete a transaction, cant be deleted if inventory is created."""
    def delete(self ,request ,str_1, num_1, num_2):
        num = str(num_1).zfill(4)
        trans_number = f"{str_1}/{num}/{num_2}"
        check = InventoryItem.objects.filter(item__transaction__trans_number=trans_number).exists()
        if not check:
            transation = Transaction.objects.get(trans_number = trans_number)
            transation.delete()
            return Response({"message":f"Transaction with trans_number {trans_number} deleted"}, status=status.HTTP_200_OK)
        return Response({"message":f"Transaction with trans_number {trans_number} contains invetory",
                         "status" :status.HTTP_401_UNAUTHORIZED})



"""Add line items once a transaction is created"""
class ItemsAPI(APIView):
    def post(self, request, format=None):
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        trans_number = python_data.pop("trans_number")
        items_data = python_data.pop("line_items")

        for item in items_data:
            CreateLineItem(trans_number, **item)
        return Response({"data": "", "message": "add line items"}, status=status.HTTP_200_OK)

"""Add multiple inventory items to line items."""
class InventoryAPI(APIView):
    def post(self, request, format=None):
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        item_data = python_data.pop('items_unique_id')
        python_data_1=python_data.pop('inventory')
        for inventory in python_data_1:
            CreateInventory(item_unique_id=item_data, **inventory)
        return Response({"message":"add inventory items"}, status=status.HTTP_200_OK)

