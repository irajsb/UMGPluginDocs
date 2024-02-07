import os
import json

def generate_json(base_dir, array_field_name):
    json_data = {array_field_name: []}  # Initialize a dictionary with the array field name as key

    # Iterate through directories and files recursively
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            # Ignore specified files
            if file in ['file_mapping.json', 'Generate.py']:
                continue
            
            # Construct the URL using the base URL and relative file path
            url = f"https://irajsb.github.io/UMGPluginDocs/DLC/{os.path.relpath(os.path.join(root, file), base_dir)}"
            # Replace backslashes with forward slashes in the URL
            url = url.replace('\\', '/')
            # Construct the target folder using the /FontIcons/ prefix and relative file path
            target_folder = f"/FontIcons/{os.path.relpath(os.path.join(root, file), base_dir)}"
            # Replace backslashes with forward slashes in the target folder path
            target_folder = target_folder.replace('\\', '/')
            # Create a dictionary representing the JSON object
            json_object = {"URL": url, "TargetFolder": target_folder}
            # Append the JSON object to the list
            json_data[array_field_name].append(json_object)

    return json_data

def main():
    base_directory = '.'  # Set the base directory to the current directory
    array_field_name = 'Files'  # Name of the array field
    json_data = generate_json(base_directory, array_field_name)

    # Write the JSON data to a file
    with open('file_mapping.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("JSON object containing URL and target folder mappings has been generated successfully.")

if __name__ == "__main__":
    main()