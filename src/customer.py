"""
Fetch (Select) the customer details
Add (Insert) new customer details
.
.
"""

import json


def get_customer(file_path):
    """
    Get all the customers
    """
    # Write the business logic to retrive the customer details
    if file_path:
        with open(file_path, 'r') as f:
            customer_data = json.load(f)

    return customer_data if customer_data else None


def add_customer(file_path, **new_customer):
    """
    Adding new customer
    """

    if file_path:
        # Load the original data
        load_data = get_customer(file_path)
        # Add the new customer to original data
        for item in new_customer["data"]:
            load_data["data"].append(item)

        with open(file_path, "w") as outfile:
            json.dump(load_data, outfile)

        # Load the original data
        load_data = get_customer(file_path)
    
    return load_data if load_data else None
