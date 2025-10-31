import os
from config import MAX_CHARS

def get_file_content(working_directory,file_path):
    try:
        full_path = os.path.abspath(os.path.join(working_directory,file_path))
        file_abs_path = os.path.abspath(full_path)

        if not file_abs_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read: "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file_content = ""
        # MAX_CHARS = config.MAX_CHARS
        with open(file_abs_path,"r") as f:
            file_content = f.read()
            if len(file_content) > MAX_CHARS:
                truncated_content = file_content[:MAX_CHARS]
                messaged_content  = truncated_content + f' [...File "{file_path}" truncated at 10000 characters]'

        # print(file_content,"=======file content")
        return messaged_content
    except Exception as e:
        return f"Error: {e}"