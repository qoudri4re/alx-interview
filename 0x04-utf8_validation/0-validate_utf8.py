#!/usr/bin/python3

def validUTF8(data):
    num_of_bytes_to_process = 0
    for num in data:
        # get the binary representation of the current byte
        binary_num = format(num, '#010b')[-8:]
        if num_of_bytes_to_process == 0:
            # if the first bit is 1, it's a continuation byte
            if binary_num[0] == '1':
                return False
            # if the first bit is 0, it's a single-byte character
            elif binary_num[0] == '0':
                continue
            # if the first three bits are 110, it's the start of a two-byte character
            elif binary_num[:3] == '110':
                num_of_bytes_to_process = 1
            # if the first four bits are 1110, it's the start of a three-byte character
            elif binary_num[:4] == '1110':
                num_of_bytes_to_process = 2
            # if the first five bits are 11110, it's the start of a four-byte character
            elif binary_num[:5] == '11110':
                num_of_bytes_to_process = 3
            # if none of the above, it's not a valid UTF-8 character
            else:
                return False
        else:
            # if the first two bits are not 10, it's not a valid continuation byte
            if binary_num[:2] != '10':
                return False
            num_of_bytes_to_process -= 1
    # if we've processed all bytes and there are no remaining bytes to process, it's a valid UTF-8 string
    if num_of_bytes_to_process == 0:
        return True
    else:
        return False
