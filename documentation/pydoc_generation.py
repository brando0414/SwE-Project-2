import os
import subprocess

def generate_pydoc_for_files(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a Python file
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)
            
            # Use subprocess to run pydoc for each Python file
            print(f"Generating pydoc for {filename}...")
            try:
                subprocess.run(['python', '-m', 'pydoc','-w', filepath], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error generating pydoc for {filename}: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
    
    print("Finished generating pydocs.")
    subprocess.run(['python', '-m', 'pydoc','-p', '8080'], check=True)

# Usage
directory = "../Scripts"
generate_pydoc_for_files(directory)
