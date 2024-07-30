import logging
from datetime import datetime, timedelta


logging.basicConfig(filename="parts.log", filemode='w',
                    level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


def validate_max_service_hours():
    service_hours = input(
        "What is the max service hours?")

    if service_hours.isnumeric():
        return service_hours
    else:
        logging.error("User input for max hours is not numeric")
        print("Please enter a number")


def validate_part_id():
    part_id = input(
        "What is the part number?")

    if part_id.isnumeric():
        return part_id
    else:
        print("part number is not numeric")


# def install_date():
#     install_date = input("What is the service date?")
#     if install_date
validate_max_service_hours()
validate_part_id()
