#!/usr/bin/env python3

"""
Magic Number File Type Identifier
Identifies file types by reading file headers
"""
# Dictionary of magic numbers
# Fortmat: 'File Type': (offset, signature_bytes)
MAGIC_NUMBERS = {                       # This creates a dictionary (like a lookup table)
    'PNG': (0, b'\x89PNG\r\n\x1a\n'),
    'JPEG': (0, b'\xFF\xD8\xFF'),
    'GIF': (0, b'GIF89a'),
    'PDF': (0, b'%PDF'),
    'ZIP': (0, b'PK\x03\x04'),
}

# 'PNG': - The key is the file type name (what we'll display to the user)
# (0, b'...') - A tuple with two parts:
# Part 1) 0 = offset (where in the file to look, 0 means start of file)
# Part 2) b'...' = the actual bytes we're looking for

# Byte Notation:
# b'PNG' - Regular ASCII text as bytes
# \x89 - Hexadecimal byte (hex 89)
# \r\n - Carriage return and newline characters
# \x03\x04 - Two hex bytes

def identify_file(filepath):     # Defines a function that takes a file path as input
    """
    Read file header and identify file type
    
    Args:
        filepath: Path to the file to identify
    
    Returns:
        String with file type or 'Unknown'
    """
    try:                        # Starts a try-except block to catch errors gracefully
        with open(filepath, 'rb') as f:            # Opens the file in read binary mode
            header = f.read(512)                   # Reads first 512 bytes from the file
            
            for file_type, (offset, signature) in MAGIC_NUMBERS.items():  # Loops through our directory
                end = offset + len(signature)      # Calculate where the signature ends
                if header[offset:end] == signature:   # Slice the header and compares to known signature
                    return file_type              # If a match is found, return the type
            
            return 'Unknown'      # On no match
    # The bellow blocked known errors
    except FileNotFoundError:
        return f"Error: File '{filepath}' not found"
    except PermissionError:
        return f"Error: Permission denied for '{filepath}'"
    except Exception as e:
        return f"Error: {str(e)}"
        
def main():
    """Main function to handle command-line arguments"""
    import argparse       # Imports Python's argument parsing library

    
    parser = argparse.ArgumentParser(         # Creates an argument parser
        description='Identify file types using magic numbers'
    )
    parser.add_argument(
        'files',        # name of the argument
        nargs='+',      # means "accept one or more files"
        help='File(s) to identify'   # Description
    )
    
    args = parser.parse_args()   # Actually parses the command-line arguments into usable data
    
    for filepath in args.files:    # Loop
        result = identify_file(filepath)   # Call our function from Step 4
        print(f"{filepath}: {result}")    # Result


if __name__ == '__main__':     # only run this if script is executed directly
    main()
        
