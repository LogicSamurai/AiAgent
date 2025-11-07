import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path = os.path.abspath(os.path.join(working_directory,file_path))
    abs_path = os.path.abspath(full_path)
    working_dir_abs_path = os.path.abspath(working_directory)

    if not abs_path.startswith(working_dir_abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    dirname = os.path.dirname(file_path)
    dir_path = os.path.abspath(os.path.dirname(full_path))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    try:
        with open(full_path,"w") as f:
            content_len = f.write(content)
            return f'Successfully wrote to "{file_path}" ({content_len} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)