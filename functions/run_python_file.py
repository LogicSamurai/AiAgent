import subprocess
import sys
import os
from google.genai import types


def run_python_file(working_directory,file_path,args=[]):
    try:
        full_path = os.path.abspath(os.path.join(working_directory,file_path))
        file_abs_path = os.path.abspath(full_path)

        if not file_abs_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(file_abs_path):
            return f'Error: File "{file_path}" not found.'

        if not os.path.basename(file_path).lower().endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.' 

        try:
            commands = ["python", file_abs_path]
            if args:
                commands.extend(args)
            completed_process = subprocess.run(commands, capture_output=True, text=True, timeout=30)
        except Exception as e:
            return f"Error: executing Python file: {e}"

        result_str = f"STDOUT: {completed_process.stdout}, STDERR: {completed_process.stderr}"
        if not completed_process.returncode == 0:
            result_str += f" Process exited with code {completed_process.returncode}"

        if not completed_process.stdout:
            return "No output produced"

        return result_str
    except Exception as e:
        return f"Error: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)