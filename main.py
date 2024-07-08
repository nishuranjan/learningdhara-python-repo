"""
Generate the customer profile and store into output folder

"""
from src.customer import get_customer


FILE_PATH = "data/customer.json"
customer_all = get_customer(FILE_PATH)
print(customer_all)
print("###################")
print(id(FILE_PATH))
print(hex(id(FILE_PATH)))

# Home Work
# swapping of 2 variable different values
