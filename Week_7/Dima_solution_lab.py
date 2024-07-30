# import modules
import logging
from datetime import datetime, timedelta
# set variables
# user inputed vars
part_id = None
install_date_string = None
max_service_hours = None

# calculated vars
now = None
hours_remaining = None
install_date = None
hours_in_service = None
percent_hours_remaining = None


# configure our logger
logging.basicConfig(filename='partstracker.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')


# control function for getting user input and validating it

def ask_for_input_and_validate(validation_function, prompt, reprompt):
    while True:
        user_input = input(prompt)
        try:
            validation_function(user_input)
        except:
            print(reprompt)
            continue
        else:
            break
    return user_input


# validation function for part_id
def part_id_validation(user_input):
    if not user_input.isalnum():
        raise ValueError('not alpha numeric')
    if len(user_input) != 4:
        raise ValueError("not 4 chars")

# validation function for install_date (validate string is in the right format)


def validate_install_date_format(user_input):
    try:
        datetime.strptime(user_input, '%Y/%m/%d')
    except ValueError:
        raise ('not in the right format')

# validation function for maxservice hours


def validate_max_hours(user_input):
    try:
        int(user_input)
    except ValueError:
        raise ("not an integer")


part_id = ask_for_input_and_validate(
    part_id_validation, "what is part number?", 'Part id must be 4 alphanumberic characters')
install_date_string = ask_for_input_and_validate(
    validate_install_date_format, "Please enter install date in YYYY/MM/DD format", " install date must be in YY/MM/DD")
max_service_hours = int(ask_for_input_and_validate(
    validate_max_hours, "What is the max service hours", "Max service hours must be an integer"))


print(f"install_date_string {install_date_string}")
print(f"max_service_hours {max_service_hours}")
print(f"part_id: {part_id}")


# calculate the parts hours remaining
install_date = datetime.strftime(install_date_string, '%Y/%m/%d')
now = datetime.now()
hours_in_service = (now - install_date).total_seconds() / 3600

hours_remaining = max_service_hours - hours_in_service
percent_hours_remaining = hours_remaining / max_service_hours * 100


# datetime install object


# log at appropriate level to file (use if/elif/else block)
if percent_hours_remaining > 20:
    logging.info(
        f"Part id: {part_id} is good. It has {hours_remaining} hours of service remaining")
elif percent_hours_remaining > 0:
    logging.warning(
        f"Part id: {part_id} has less then 20% of service time remaining. Replace part")
else:
    logging.critical(
        f"Part id: {part_id} is critical and needs to be changed immdiately")
