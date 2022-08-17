from datetime import datetime


# TODO
# add more delaying initialization if needed
def init_delays():
    with open(f'../YABL00_DATABASE/activity_time', 'w') as output_file:
        output_file.write(str(datetime.now()))


def update_activity_ltime():
    with open(f'../YABL00_DATABASE/activity_time', 'w') as output_file:
        output_file.write(str(datetime.now()))


def get_delta_activity_time():
    with open(f'../YABL00_DATABASE/activity_time') as input_file:
        ltime_str = input_file.read()
    ltime = datetime.strptime(ltime_str, '%Y-%m-%d %H:%M:%S.%f')
    delta = datetime.now() - ltime
    return delta
