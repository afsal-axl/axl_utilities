#!/usr/bin/env python3

from __future__ import print_function
import sys
from datetime import datetime
import json  # Import the json module

def print_today_date():
    today_date = datetime.now().date()
    today_day = today_date.strftime("%A")
    d = {
        "Date": str(today_date),
        "Day" : today_day
    }
    return d

if __name__ == "__main__":
    # Call the print_today_date function
    result_dict = print_today_date()

    # Convert the dictionary to JSON format
    json_result = json.dumps(result_dict, indent=2)

    # Print the JSON result
    print(json_result)
