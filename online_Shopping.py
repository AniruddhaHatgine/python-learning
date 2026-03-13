product = {
  "product_id": "P101",
  "name": "Wireless Headphones",
  "price": 2999,
  "brand": "Sony",
  "stock": 50,
  "specifications": {
    "color": "Black",
    "battery": "20 hours",
    "warranty": "1 year"
  }
}

print(product["price"])

print(product["specifications"]["battery"])

product["stock"] = 40

product["color"]= "Blue"

product["Discount"]= "20%"

product["update"]= "3 years"

del product["specifications"]["warranty"]

print(product)