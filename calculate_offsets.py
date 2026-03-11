import re

def calculate_offsets(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()

    offsets = []
    pattern = re.compile(rb'(?<!\w)_{1,}(?!\w)')

    for match in pattern.finditer(content):
        offsets.append((match.start(), len(match.group())))

    return offsets

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1] if len(sys.argv) > 1 else "L01/T01/task.py"
    offsets = calculate_offsets(file_path)

    for i, (offset, length) in enumerate(offsets, 1):
        print(f"Placeholder {i}: offset={offset}, length={length}")
