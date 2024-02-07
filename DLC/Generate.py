import os
import json

def generate_json(base_dir):
    json_data = []  # Initialize an empty list to store JSON objects

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
            json_data.append(json_object)

    return json_data

def main():
    base_directory = '.'  # Set the base directory to the current directory
    json_data = generate_json(base_directory)

    # Write the JSON data to a file
    with open('file_mapping.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("JSON object containing URL and target folder mappings has been generated successfully.")

if __name__ == "__main__":
    main()
