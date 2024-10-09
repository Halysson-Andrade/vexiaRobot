import os
import json

def create_directory_structure(data):
    branches_infos = []

    for branch_id, branch_info in data['1']['branches'].items():
        branch_name = branch_info['branchDetails']['brc_name'].replace(" ", "_").lower()
        os.makedirs(branch_name, exist_ok=True)

        # Iterate through borrowers
        borrower =  branch_info['borrowers']['1']['borrowerDetails']
        borrower_name = borrower['brr_name'].replace(" ", "_").lower()

        os.makedirs(f'{branch_name}/{borrower_name}', exist_ok=True)

        for employee in branch_info['borrowers']['1']['employees']:
            employee_name = employee['empl_name'].replace(" ", "_").lower() + '.txt'
            employee_file_path = os.path.join(f'{branch_name}/{borrower_name}', employee_name)

            with open(employee_file_path, 'w') as f:
                f.write('Hello, World!')

with open('json.example.json') as f:
    json_data = json.load(f)

create_directory_structure(json_data['data'])
