import json
import sys

tests_path = sys.argv[1]
values_path = sys.argv[2]
reports_path = sys.argv[3]

with open(values_path, 'r', encoding='utf-8') as f:
    values_data = json.load(f)
id_to_value = {item['id']: item['value'] for item in values_data['values']}

with open(tests_path, 'r', encoding='utf-8') as f:
    tests_data = json.load(f)

def fill_values(test_list):
    for test in test_list:
        test_id = test.get('id')
        if test_id in id_to_value:
            test['value'] = id_to_value[test_id]
        if 'values' in test:
            fill_values(test['values'])

fill_values(tests_data['tests'])

with open(reports_path, 'w', encoding='utf-8') as f:
    json.dump(tests_data, f, indent=2, ensure_ascii=False)



