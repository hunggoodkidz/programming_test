def file_reader_demo():
    filename = "./utils/Q4_file.txt" 
    
    with open(filename, "r", encoding="utf-8") as f:
        # Read and print every line in the file
        for line in f:
            print(line, end="")  # 'end=""' avoids adding extra newlines

if __name__ == "__main__":
    file_reader_demo()
