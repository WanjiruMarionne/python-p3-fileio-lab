def write_file(file_name, file_content):
    file_name = str(file_name) + ".txt"
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name = str(file_name) + ".txt"
    with open(file_name, 'a') as file:
        if file.tell() != 0:
            append_content = append_content.lstrip("\n")  
            append_content = "\n" + append_content
        file.write(append_content)

def read_file(file_name):
    file_name = str(file_name) + ".txt"
    with open(file_name, 'r') as file:
        content = file.read()
    return content

