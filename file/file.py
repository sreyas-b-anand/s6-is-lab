import os
BUFFER_SIZE = 1024
def copy_file(source, destination):

    try:
        src_fd = os.open(source, os.O_RDONLY)
        dest_fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
        while True:
            data = os.read(src_fd, BUFFER_SIZE)
            if not data:
                break
            os.write(dest_fd, data)

        os.close(src_fd)
        os.close(dest_fd)
        print("File copied successfully.")
    except OSError as e:
        print("Error:", e)
        
        
source_file = input("Enter source file: ")
destination_file = input("Enter destination file: ")
copy_file(source_file, destination_file)