import re

log_file = '/var/log/app.log'
error_keyword = 'ERROR'

def analyze_logs():
    with open(log_file, 'r') as file:
        for line in file:
            if re.search(error_keyword, line):
                print(line)

analyze_logs()
