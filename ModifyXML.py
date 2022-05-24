from datetime import datetime, timedelta
import xml.etree.ElementTree as ET


def updatexml(x, y):
    tree = ET.parse('input_files/test_payload1.xml')
    root = tree.getroot()
    initial_depart_date = root.find('.//DEPART').text
    initial_return_date = root.find('.//RETURN').text
    modified_depart_date = datetime.strptime(initial_depart_date, '%Y%m%d') + timedelta(x)
    modified_return_date = datetime.strptime(initial_return_date, '%Y%m%d') + timedelta(y)
    root.find('.//DEPART').text = modified_depart_date.strftime("%Y%m%d")
    root.find('.//RETURN').text = modified_return_date.strftime("%Y%m%d")
    tree.write('output_files/test_payload1_modified.xml')


updatexml(20, 20)
