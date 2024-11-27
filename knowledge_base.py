import json as js

def load_knowledge_base(file_path):
    """加载知识库文件"""
    try:
        with open(file_path, 'r') as file:
            return js.load(file)
    except FileNotFoundError:
        print(f"错误: 无法找到文件 {file_path}")
        return []
    except js.JSONDecodeError:
        print(f"错误: 文件 {file_path} 格式错误")
        return []