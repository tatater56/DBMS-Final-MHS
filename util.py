from datetime import datetime

def is_empty_string(param):
    return not (param and isinstance(param, str) and not param.isspace())

def validate_date(input_date):
    try:
        datetime.strptime(input_date, '%Y-%m-%d')
        return input_date
    except (ValueError, TypeError):
        return None

def validate_datetime(input_datetime):
    try:
        dt = datetime.strptime(input_datetime, '%Y-%m-%dT%H:%M')
        return dt
    except (ValueError, TypeError):
        return None

def validate_int(input_int):
    if is_empty_string(input_int):
        return None
    elif input_int.isdigit():
        return int(input_int)
    else:
        return None

def validate_str(input_str):
    if is_empty_string(input_str):
        return None
    else:
        return input_str

def validate_form_input(input_dict):
    print(f"validate_form_input before: {input_dict=}")
    for k in input_dict:
        input_dict[k] = validate_str(input_dict[k])
    
    print(f"validate_form_input after: {input_dict=}")
    return input_dict

if __name__ == '__main__':
    print('Testing is_empty_string')
    for x in [is_empty_string(None),
                is_empty_string(''),
                is_empty_string('foobar'),
                is_empty_string('false')]:
        print(x)
    
    print('Testing validate_date')
    for x in [validate_date(None),
                validate_date(''),
                validate_date('2020-01-01'),
                validate_date('foobar')]:
        print(x)
