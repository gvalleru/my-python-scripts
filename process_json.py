'''
Script to parse employees json data and creates json data which groups managers and reportees
'''

import json

json_data = '''{
	"employees": [{
			"Id": "1",
			"ParentId": "",
			"Name": "Stephen Curry",
			"Title": "Vice President",
			"Phone": "(408) 111 1111"
		},
		{
			"Id": "2",
			"ParentId": "1",
			"Name": "Kevin Durant",
			"Title": "Director of Operations",
			"Phone": "(408) 111 1112"
		},
		{
			"Id": "3",
			"ParentId": "1",
			"Name": "Klay Thompson",
			"Title": "Director of Network Operations",
			"Phone": "(408) 111 1113"
		},
		{
			"Id": "4",
			"ParentId": "2",
			"Name": "Jordan Bell",
			"Title": "Cloud Architect",
			"Phone": "(408) 111 1116"
		},
		{
			"Id": "5",
			"ParentId": "1",
			"Name": "Draymond Green",
			"Title": "Director of Dev ops",
			"Phone": "(408) 111 1114"
		},
		{
			"Id": "6",
			"ParentId": "2",
			"Name": "Andre Iguodala",
			"Title": "Manager of Operations",
			"Phone": "(408) 111 1115"
		}
	]
}'''

data = json.loads(json_data)
parsed_data_list = []
parentid_list=[]
for i in range(0, len(data["employees"])):
    parentid_list.append(data["employees"][i]["ParentId"])

parentid_list = sorted(set(parentid_list))

for parentid in parentid_list:
    if parentid != '':
        for employee in data["employees"]:
            if employee["Id"] ==  parentid:
                parent_employee = employee
                parsed_data = {}
                parsed_data["Name"] = parent_employee["Name"]
                reports =[]
                for employee in data["employees"]:
                    if parent_employee["Id"] == employee["ParentId"]:
                        reports.append(employee["Name"])
                parsed_data["reports"] = reports
                parsed_data_list.append(parsed_data)
parsed_data_json = json.dumps(parsed_data_list)
print parsed_data_json