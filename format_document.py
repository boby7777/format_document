def remove_inappropriate_newlines(text):
    # 按行拆分文本
    lines = text.splitlines()
    cleaned_text = ""

    # 逐行处理文本
    for line in lines:
        if line.endswith(('。', '”', '？', '?', '！', '!')):
            cleaned_line = remove_extra_spaces(line) + '\n'
        elif line.startswith('Table') or line.startswith('导读') or line.startswith('#') or (line.startswith('第') and line[1].isdigit()):
            cleaned_line = '\n' + line + '\n'
        else:
            cleaned_line = remove_extra_spaces(line)
        cleaned_text += cleaned_line
    return cleaned_text

def remove_extra_spaces(line):
    cleaned_line = ''
    prev_char = ''
    for char in line:
        if char.isspace() and prev_char.isspace():
            cleaned_line += char
        elif char.isspace():
            if is_ascii(prev_char) or is_ascii(line[line.index(char) + 1:]):
                cleaned_line += char
        else:
            cleaned_line += char
        prev_char = char
    return cleaned_line

def is_ascii(text):
    return all(ord(char) < 128 for char in text)

# 示例用法
file_path = 'test.md'  # 外部文件路径

with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

output_text = remove_inappropriate_newlines(input_text)

output_file_path = 'out.md'  # 输出文件路径

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(output_text)
