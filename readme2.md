1.	Add a transaction with its line items.

POST http://localhost:8000/transaction/

   This API creates a transaction with line items data.

RequestPayload:
{
    "company" : {"name":"Ace"},
    "branch" : {"short_name":"SUN"},
    "department" : {"name":"DPV"},
    "trans_status" : "CLOSE",
    'remarks' : "First Transaction",
    "line_items" :
        [
            {
"article" : {"name" : "YarnArticle2"},
    "color" : {"name" : "Yellow"},
    "quantity" : 123.45,
    "rate_per_unit" : 18,
    "unit" : "KG"
    },
    {
"article" : {"name" : "YarnArticle2"},
    "color" : {"name" : "Yellow"},
    "quantity" : 123.45,
    "rate_per_unit" : 18,
    "unit" : "KG"
    }
        ]
}


2.  Add line items once a transaction is created.

Post http://127.0.0.1:8000/transaction/items/
{
    "trans_number" : "TRN/0000/2021",

"line_items" :[

    {
    "article" : {"name" : "YarnArticle2"},
    "color" : {"name" : "Yellow"},
    "quantity" : 123.45,
    "rate_per_unit" : 18,
    "unit" : "KG"

     },

{
    "article" : {"name" : "YarnArticle2"},
    "color" : {"name" : "Black"},
    "quantity" : 123.45,
    "rate_per_unit" : 18,
    "unit" : "KG"

     },

	. . . . . .
]
}

2.	Add multiple inventory items to line items.

POST http://127.0.0.1:8000/transaction/inventory/


{

  "items_unique_id": 1,


  "inventory": [
    {
      "article": {
        "name": "YarnArticle2"
      },
      "color": {
        "name": "Yellow"
      },
      "company": {
        "name": "Ace"
      },
      "gross_quan": 28,
      "net_quan": 18,
      "unit": "KG"
    },

    {
      "article": {
        "name": "YarnArticle1"
      },
      "color": {
        "name": "Black"
      },
      "company": {
        "name": "Ace"
      },
      "gross_quan": 30,
      "net_quan": 19,
      "unit": "KG"
    }
  ]
}

4.  Delete a transaction, cant be deleted if inventory is created.

DELETE : http://localhost:8000/transaction/<trans_number>/

Example: http://127.0.0.1:8000/transaction/TRN/0001/2021/
Response:{
"message": "Transaction with trans_number TRN/0000/2021 contains    inventory"
"status": 401}

5.  View a transaction with all its line items and their inventory items.

GET : http://127.0.0.1:8000/transaction/<trans_number>/

http://127.0.0.1:8000/transaction/TRN/0001/2021/
HTTP 200 OK
Allow: GET, POST, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "unique_id": 2,
    "company": "Ace",
    "branch": "SUN",
    "department": "DPV",
    "trans_number": "TRN/0001/2021",
    "trans_status": "CLOSE",
    "remarks": "First Transaction",
    "items": [
        {
            "unique_id": 2,
            "article": "YarnArticle2",
            "color": "Yellow",
            "date": "2021-05-31T21:12:07.945194Z",
            "quantity": "123.45",
            "rate_per_unit": 18,
            "unit": "KG",
            "inventory": []
        },
        {
            "unique_id": 3,
            "article": "YarnArticle2",
            "color": "Yellow",
            "date": "2021-05-31T21:12:08.429454Z",
            "quantity": "123.45",
            "rate_per_unit": 18,
            "unit": "KG",
            "inventory": []
        }
    ]
}


