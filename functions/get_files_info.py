import os

def get_files_info(working_directory,directory="."):
    try:
        result = []
        full = os.path.abspath(os.path.join(working_directory, directory))
        directory_abs_path = os.path.abspath(full)

        if not directory_abs_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        is_directory = os.path.isdir(directory_abs_path) 
        if not is_directory:
            return f'Error: "{directory}" is not a directory'

        for entry in  os.listdir(directory_abs_path):
            if entry.startswith("."):
                continue

            path = os.path.join(directory_abs_path,entry) 
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)

            result.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")

        return result    
    except Exception as e:
        print(f"Error: {e}")