import functools

def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            splited_doc = doc.split("\n")
            # count = 0
            # for line in splited_doc:
            #     if sequence in line:
            #         count += 1
            # return count

            return functools.reduce(
                lambda x, y: x + 1 if sequence in y else x,
                splited_doc,
                0
            )
        
        return with_length

    return with_char