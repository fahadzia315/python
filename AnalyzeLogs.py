import csv
from datetime import datetime
import pytz

def parselogfiles(filename):
    output_file = open("output_files/log_analysis.txt", "w")
    result_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open(filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for line in csv_reader:
            if line_count == 0:
                line_count += 1
                result_writer.writerow(["timeStamp", "label", "responseCode", "responseMessage", "failureMessage"])
            if line["responseCode"] != '200':
                time_stamp = int(line["timeStamp"])
                date_obj = datetime.fromtimestamp(time_stamp / 1e3)
                date_obj = date_obj.astimezone(pytz.timezone("US/Pacific"))
                date_format = '%Y-%m-%d %H:%M:%S %Z'
                date_obj = datetime.strftime(date_obj, date_format)
                result_writer.writerow(
                     [date_obj, line["label"], line["responseCode"], line["responseMessage"], line["failureMessage"]])

parselogfiles('input_files/Jmeter_log1.jtl')
#parselogfiles('input_files/Jmeter_log2.jtl')

