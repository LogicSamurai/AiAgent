import os

def get_files_info(working_directory,directory="."):
    try:
        is_directory = os.path.isdir(directory) 
        if not is_directory:
            print(f'Error: "{directory}" is not a directory')

        full_path = os.path.join(working_directory,directory)
        directory_abs_path = os.path.abspath(directory)

        if not directory_abs_path.startswith(full_path):
            print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory') 

        file_name = os.path.basename(working_directory) 
        file_size = os.path.getsize(working_directory)
        directory_content = os.listdir(directory)
        print(directory_content,"directory content==========")

        for i in directory_content:
            print(os.path.isfile(i),"path===========")

        return f"{file_name}: file_size={file_size} bytes, is_dir={is_directory}"
    
    except Exception as e:
        print(f"Error: {e}")