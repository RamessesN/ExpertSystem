import json as js

def load_knowledge_base(file_path):
    """Load the knowledge base file"""
    try:
        with open(file_path, 'r') as file:
            return js.load(file)
    except FileNotFoundError:
        print(f"Error: Cannot find file: {file_path}")
        return []
    except js.JSONDecodeError:
        print(f"Error: The format of file {file_path} is wrong")
        return []