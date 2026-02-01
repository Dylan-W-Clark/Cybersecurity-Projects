# File Type Identifier

A command-line tool that reads file headers (magic numbers) to identify the actual file type, regardless of the extension.

## Use Cases

- **Detect file type mismatches** - Identify files with incorrect extensions (e.g., a `.txt` file that's actually an `.exe`)
- **Security analysis** - Analyse suspicious files in CTFs or malware analysis
- **File upload verification** - Verify that uploaded files match their claimed type

## Technologies Used

- **Python**
- **argparse** - Command-line argument parsing
- **pathlib** - File path handling
- **Notepad++** - Code editor

## Environment

- **Windows**

---

## Project Setup

### 1. Create Project Folder

Create a project folder in a sensible location:

```bash
mkdir magic-number-identifier
cd magic-number-identifier
```

![Project Folder](https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/9bcc5f53fcd2c8c8124b87c8e86af3af9fb3ff76/Screenshot%202026-01-31%20150216.png)

### 2. Set Up Virtual Environment (Recommended)

This keeps the project dependencies separate from your system Python:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac
```

![Virtual Environment Setup](https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/84ac215f390e6b839c58998fd1e43ac9a156fcda/Screenshot%202026-01-31%20152255.png)

![Virtual Environment Activated](https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/84ac215f390e6b839c58998fd1e43ac9a156fcda/Screenshot%202026-01-31%20152337.png)

---

## Implementation

### 1. Create the Main Python File

- Open your text editor (Notepad++, VS Code, or your preferred editor)
- Create a new file named `magic_number.py` in your `magic-number-identifier` folder

### 2. Add the Shebang and Docstring

```python
#!/usr/bin/env python3
"""
File Type Identifier using Magic Numbers
"""
```

> **Note:** The shebang (`#!/usr/bin/env python3`) tells Linux/Mac systems to run this file with Python. While it doesn't affect Windows execution, it's good practice for portability.

![Shebang and Docstring](https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/4b1648d99967eefba7a0e7df366ded939383f9db/Screenshot%202026-01-31%20160742.png)

### 3. Create the Magic Numbers Dictionary

This dictionary maps file signatures (magic numbers) to their corresponding file types:

![Magic Numbers Dictionary](https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/3cc80a07f70e664b868be2da914953b684a674b6/Screenshot%202026-01-31%20162752.png)

### 4. Write the File Identification Function

This function reads the file header and matches it against known magic numbers:

![Identification Function](https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/180ca69b31fbdc5766e00cfa17965f81d04e7c1c/Screenshot%202026-01-31%20164344.png)

### 5. Add the Command-Line Interface

Implement the CLI using argparse to accept file paths as arguments:

![Command-Line Interface](https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/3a2f3ed7bd76fb56e5ea79aec1d96c9866c4ea04/Screenshot%202026-01-31%20165312.png)

---

## Testing

### Prepare Test Files

You can use any of these methods:

**Option 1: Download test files from the internet**
- Download a PNG image from Google Images (right-click > Save)
- Download any PDF file
- Download a JPEG photo
- Save them in your `magic-number-identifier` folder

**Option 2: Use existing files**
- Copy some files you already have (images, PDFs, etc.) into your project folder

**Option 3: Create a mismatch test (Recommended)**
- Take a JPEG file
- Rename it with a different extension (e.g., `image.jpg` → `download.ps1`)
- The tool should still correctly identify it as a JPEG!

![Test Files](https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/49cb1bbdef31193fac70278eb012dfe70036d111/Screenshot%202026-01-31%20171935.png)

### Running the Tool

Make sure you're in the `magic-number-identifier` folder with your virtual environment activated:

```bash
python magic_number.py <filename>
```

**Example:**
```bash
python magic_number.py download.ps1
python magic_number.py sample.py
python magic_number.py document.pdf
```

![Running the Tool](https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/a4256a270ec735f389b2d93f17af0d3b84ca7e11/Screenshot%202026-01-31%20172530.png)

### Results

As demonstrated in the screenshot above, the tool correctly identifies file types based on their magic numbers, regardless of their file extension. It successfully detects when files have been renamed with incorrect extensions!

---

## How It Works

The tool works by:

1. **Reading the file header** - Opens the file in binary mode and reads the first few bytes
2. **Comparing magic numbers** - Matches the header bytes against a dictionary of known file signatures
3. **Identifying the type** - Returns the actual file type based on the magic number match
4. **Reporting results** - Displays the identified file type to the user

This method is more reliable than checking file extensions, which can be easily changed or spoofed.

---

## Author

Dylan W. Clark
