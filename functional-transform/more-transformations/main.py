def doc_format_checker_and_converter(conversion_function, valid_formats):
    
    def is_file_ext_valid(filename, content):
        if filename.split(".")[1] in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError("Invalid file format")
    
    return is_file_ext_valid


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]