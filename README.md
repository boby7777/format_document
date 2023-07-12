# 移除文章中不適當的斷行及空白

This script removes inappropriate newlines from text.

## Usage

1. Make sure you have Python installed.
2. Clone this repository.
3. Open a terminal and navigate to the cloned repository directory.
4. Run the following command:

```shell
python remove_inappropriate_newlines.py
```

## Description

The `remove_inappropriate_newlines` function takes in a text as input and removes inappropriate newlines from it. It performs the following actions:

- Splits the text into lines.
- Iterates through each line and checks for specific conditions:
  - If a line ends with '。', '”', '？', '?', '！', or '!', it removes extra spaces and appends a newline character '\n' at the end.
  - If a line starts with 'Table', '导读', '#', or '第' followed by a digit, it adds newline characters '\n' at the beginning and end.
  - For all other lines, it removes extra spaces.
- Reassembles the cleaned lines into a single cleaned text.

The `remove_extra_spaces` function is a helper function that removes extra spaces from a line, considering specific conditions.

## Example

You can run the script with your own text file by modifying the `file_path` and `output_file_path` variables in the script. Ensure that the input file is encoded in UTF-8.

```python
# Example usage

file_path = 'your_input_file.md'
output_file_path = 'your_output_file.md'

with open(file_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

output_text = remove_inappropriate_newlines(input_text)

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(output_text)
```

## License

This project is licensed under the [MIT License](LICENSE).
