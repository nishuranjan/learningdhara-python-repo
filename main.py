"""
Generate the customer profile and store into output folder

"""
from src.customer import get_customer, add_customer


FILE_PATH = "data/customer.json"
new_customer = [{
            "name": "Prashant",
            "age": "50",
            "sex": "Male",
            "organization": "TCS",
            "department": "RnD",
            "isActive": "true"
        },]
customer_all = add_customer(FILE_PATH, data=new_customer)
print(customer_all)
print("###################")
# print(id(FILE_PATH))
# print(hex(id(FILE_PATH)))

# Home Work
# swapping of 2 variable different values
