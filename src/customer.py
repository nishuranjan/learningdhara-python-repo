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
    else:
        customer_data = None
        # write_log_txt(f"Failed to Fetch the
        # customer detais on {datetime.datetime}")

        # Improvise this section
        raise Exception(f"No path found. Path = {file_path}")

    # write_log_txt(f"Fetched customer detais on {datetime.datetime}")

    return customer_data
