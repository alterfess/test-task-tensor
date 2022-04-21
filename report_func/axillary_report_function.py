import datetime


# Additional report function for new test
def update_report_file(path: str):
    report_file = open(path, 'a')
    report_file.write(f'Timestamp:{datetime.datetime.now()}' + '\n')
    report_file.write('Automation test is proceeded' + '\n')
    return report_file


# Additional report function for failed test
def failed_test(report_file, message: str):
    report_file.write(f'Failed: {message}' + '\n')
    report_file.write('FAILED' + '\n')
    report_file.write(50 * '_' + '\n')
    report_file.close()
