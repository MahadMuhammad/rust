import os
import re

def check_file_for_sentence(file_path, sentence):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return sentence not in content

def find_files_without_sentence(directory, sentence):
    non_matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".md"):
                file_path = os.path.join(root, file)
                if check_file_for_sentence(file_path, sentence):
                    non_matching_files.append(file_path)
    return non_matching_files

def find_files_with_sentence(directory, sentence):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".md"):
                file_path = os.path.join(root, file)
                if not check_file_for_sentence(file_path, sentence):
                    matching_files.append(file_path)
    return matching_files



def create_url(error_code):
    # return "https://doc.rust-lang.org/error-index.html#%s" % error_code
    # returning file with this format: [`E0139`](https://doc.rust-lang.org/error_codes/E0139.html)
    # str = "https://doc.rust-lang.org/error_codes/%s.html" % error_code
    # return "[`%s`](%s)" % (error_code, str)
    return "[`%s`](https://doc.rust-lang.org/error_codes/%s.html)" % (error_code, error_code)
    # return f"[`{error_code}`](https://doc.rust-lang.org/error_codes/{error_code}.html)"

if __name__ == "__main__":
    target_directory = "/home/mahad/Desktop/rust/compiler/rustc_error_codes/src/error_codes/"
    sentence_to_check = "#### Note: this error code is no longer emitted by the compiler."

    non_matching_files = find_files_without_sentence(target_directory, sentence_to_check)
    matching_files = find_files_with_sentence(target_directory, sentence_to_check)

    

    output_all_files = open("output_all_files.txt", "w")
    
    # if not non_matching_files:
    # if non_matching_files:
    print("All files contain the sentence.")
    for file_path in matching_files:
        # print(file_path)
        print(re.sub(target_directory, "", file_path).replace(".md", ""))
    else:
        print("Files without the sentence:")
        for file_path in non_matching_files:
            # print(file_path)
            # printing name of file without extension like E0001
            print(re.sub(target_directory, "", file_path).replace(".md", ""))
            # print(re.sub(target_directory, "", file_path))
            # print(re.sub(target_directory, "", file_path))
        output_all_files.write(re.sub(target_directory, "", file_path).replace(".md", "") + "\n")
    print("Files without the sentence:")
    for file_path in non_matching_files:
        # print(file_path)
        # printing name of file without extension like E0001
        print(re.sub(target_directory, "", file_path).replace(".md", ""))
        output_all_files.write(re.sub(target_directory, "", file_path).replace(".md", "") + "\n")
        # print(re.sub(target_directory, "", file_path))
        # print(re.sub(target_directory, "", file_path))


    print("Total files:", len(non_matching_files) + len(matching_files))
    print("Files without the sentence:", len(non_matching_files))
    print("Files with the sentence:", len(matching_files))

    # Sorting output files
    output_all_files = open("output_all_files.txt", "r")
    lines = output_all_files.readlines()
    lines.sort()
    output_all_files = open("output_all_files.txt", "w")
    output_all_files.writelines(lines)
    

    # storing this output in a file in sorted order
    output_file_with_sentence = open("output_file_with_sentence.txt", "w")
    output_file_without_sentence = open("output_file_without_sentence.txt", "w")

    for file_path in matching_files:
        output_file_with_sentence.write(re.sub(target_directory, "", file_path).replace(".md", "") + "\n")
    for file_path in non_matching_files:
        output_file_without_sentence.write(re.sub(target_directory, "", file_path).replace(".md", "") + "\n")

    # Sorting the files
    output_file_with_sentence = open("output_file_with_sentence.txt", "r")
    output_file_without_sentence = open("output_file_without_sentence.txt", "r")

    lines = output_file_with_sentence.readlines()
    lines.sort()
    output_file_with_sentence = open("output_file_with_sentence.txt", "w")
    output_file_with_sentence.writelines(lines)

    lines = output_file_without_sentence.readlines()
    lines.sort()
    output_file_without_sentence = open("output_file_without_sentence.txt", "w")
    output_file_without_sentence.writelines(lines)


    # Add comment to error code output_all_files, if the error code is in output_file_with_sentence
    output_all_files = open("output_all_files.txt", "r")
    output_file_with_sentence = open("output_file_with_sentence.txt", "r")
    # output_file_without_sentence = open("output_file_without_sentence.txt", "r")

    lines = output_all_files.readlines()
    lines_with_sentence = output_file_with_sentence.readlines()
    # lines_without_sentence = output_file_without_sentence.readlines()

    output_all_files = open("output_all_files.txt", "w")
    # output_file_with_sentence = open("output_file_with_sentence.txt", "w")
    # output_file_without_sentence = open("output_file_without_sentence.txt", "w")

    for line in lines:
        if line in lines_with_sentence:
            output_all_files.write(line.replace("\n", "") + ", // this error code is no longer emitted by the compiler\n")
        else:
            output_all_files.write(line.replace("\n", "") + ",\n")
    # for line in lines_with_sentence:
    #     output_file_with_sentence.write(line)
    # for line in lines_without_sentence:
    #     output_file_without_sentence.write(line)




    



    output_all_files.close()
    output_file_with_sentence.close()
    output_file_without_sentence.close()

    output_file_with_sentence_markdown = open("output_file_with_sentence_markdown.md", "w")
    output_file_without_sentence_markdown = open("output_file_without_sentence_markdown.md", "w")

    for file_path in matching_files:
        output_file_with_sentence_markdown.write(create_url(re.sub(target_directory, "", file_path).replace(".md", "")) + "\n")
    for file_path in non_matching_files:
        output_file_without_sentence_markdown.write(create_url(re.sub(target_directory, "", file_path).replace(".md", "")) + "\n")

    # sorting the files and converting them to url
    output_file_with_sentence_markdown = open("output_file_with_sentence_markdown.md", "r")
    output_file_without_sentence_markdown = open("output_file_without_sentence_markdown.md", "r")

    lines = output_file_with_sentence_markdown.readlines()
    
    # convering each code to url
    # for i in range(len(lines)):
    #     lines[i] = create_url(lines[i].replace("\n", "")) + "\n"
    lines.sort()
    output_file_with_sentence_markdown = open("output_file_with_sentence_markdown.md", "w")
    output_file_with_sentence_markdown.writelines(lines)

    lines = output_file_without_sentence_markdown.readlines()
    # for i in range(len(lines)):
    #     lines[i] = create_url(lines[i].replace("\n", "")) + "\n"
    lines.sort()
    output_file_without_sentence_markdown = open("output_file_without_sentence_markdown.md", "w")
    output_file_without_sentence_markdown.writelines(lines)

    output_file_with_sentence_markdown.close()
    output_file_without_sentence_markdown.close()

