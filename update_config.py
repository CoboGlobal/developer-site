import subprocess
import json
import sys
import traceback
import os
import shutil


def delete_exist_files():
    folders_to_delete = [
        'v2/api-references/developers--webhooks',
        'v2/api-references/transactions',
        'v2/api-references/wallets',
        'v2/api-references/wallets--mpc-wallets',
    ]

    for folder in folders_to_delete:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f'已删除: {folder}')
        else:
            print(f'文件夹不存在: {folder}')


def process_spec_data(original_spec_data):
    processed_spec_data = {}
    for group in json.loads(original_spec_data):
        processed_spec_data[group["group"]] = group["pages"]
    return processed_spec_data


def update():
    try:
        source_file = "v2/cobo_waas2_openapi_spec/dev_openapi.yaml"
        destination_dir = "v2/api-references/"
        mint_file = "mint.json"

        delete_exist_files()

        command = [
            "npx", "@mintlify/scraping@latest", "openapi-file", source_file, "-o", destination_dir
        ]
        original_spec_data = subprocess.run(command, capture_output=True, text=True).stdout.split('\n', 1)[1]

        with open(mint_file, "r") as file:
            original_mint_json = json.load(file)

        processed_spec_data = process_spec_data(original_spec_data)

        navigation_update = {
            ("Wallets", "Version 2.0"): [
                ("Wallets", 0),
                ("Wallets - MPC Wallets", 1)
            ],
            ("Transactions", "Version 2.0"): [
                ("Transactions", 0)
            ],
            ("Webhooks", "Version 2.0"): [
                ("Developers - Webhooks", 0)
            ]
        }

        for group in original_mint_json["navigation"]:
            if "version" in group:
                key = (group["group"], group["version"])
                if key in navigation_update:
                    for sub_group, index in navigation_update[key]:
                        group["pages"][index]["pages"] = processed_spec_data[sub_group]

        with open(mint_file, "w") as file:
            json.dump(original_mint_json, file, indent=2)

    except:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    update()
