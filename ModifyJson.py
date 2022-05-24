import json


def updatejson(element):
    data = json.load(open("input_files/test_payload.json"))
    for key in data:
        print(key)
        if element == key:
            del data[key]
            break
        if element in data[key]:
            del data[key][element]
            break

    # Output the updated file with pretty JSON
    open("output_files/test_payload_modified.json", "w").write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))


updatejson("appdate")
#updatejson("outParams")
