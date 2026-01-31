<h1>File Type Identifier</h1>

<h2>Description</h2>

A tool that reads file headers (magic numbers) to identify the actual file type, regardless of the extension. This functionality will be ran using the command line. This is useful for:

 - Detecting file type mismatches (e.g., a .txt file that's actually a .exe).
 - Analysing suspicious files in CTFs or malware analysis.
 - Verifying file uploads.
   
<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>argparse</b>
- <b>pathlib</b>
- <b>Notpad++</b>

<h2>Environment Used </h2>

- <b>Windows</b>

<h2>Walk-Through</h2>

<p align="center">
Create a project folder somewhere sensible <br/>
<img src="https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/9bcc5f53fcd2c8c8124b87c8e86af3af9fb3ff76/Screenshot%202026-01-31%20150216.png" height="80%" width="80%" alt="File-Type-Identifier"/>
<br />
<br />
Optional but recommended: Set up a virtual environment (This keeps the project deployment separate)  <br/>
<img src="https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/84ac215f390e6b839c58998fd1e43ac9a156fcda/Screenshot%202026-01-31%20152255.png" height="80%" width="80%" alt="File-Type-Identifier"/>
 <br />
<img src="https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/84ac215f390e6b839c58998fd1e43ac9a156fcda/Screenshot%202026-01-31%20152337.png" height="80%" width="80%" alt="File-Type-Identifier"/>
<br />
<br />
<p align="left">
<hr>
<h2>Create the main .py file</h2>

- Open your text editor (Notepad, VS Code, whatever you've got/prefer).
- Create a new empty file.
- Save it as magic_identifier.py in your magic-number-identifier folder.

<hr>
<br />
<p align="center">
Add the shebang and docstring <br/>

<img src="https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/4b1648d99967eefba7a0e7df366ded939383f9db/Screenshot%202026-01-31%20160742.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<p align="center">
 
- This is called a "shebang". On Linux/Mac it tells the system to run this with Python. On Windows it doesn't do much, good practice and makes your code portable.
<p align="center">
<br />
<br />
Create the magic numbers dictionary  <br/>
<img src="https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/3cc80a07f70e664b868be2da914953b684a674b6/Screenshot%202026-01-31%20162752.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Write the file identification function <br/>
<img src="https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/180ca69b31fbdc5766e00cfa17965f81d04e7c1c/Screenshot%202026-01-31%20164344.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br/>
<br/>
Add the command-line interface  <br/>
<img src="https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/3a2f3ed7bd76fb56e5ea79aec1d96c9866c4ea04/Screenshot%202026-01-31%20165312.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
<p align="left">
<hr>

<h2>Testing the code</h2                 
<h3>Option 1: Download some test files from the internet:</h3>

- A PNG image (any image from Google Images, right-click > Save)
- A PDF (any PDF)
- A JPEG photo
- Save them in your magic-number-identifier folder

<h4>Option 2: Use files you already have</h4>

- Copy some existing files (images, PDFs, etc.) into your project folder.

<h5>Option 3: Rename a file with the wrong extension</h5>

- Take a PNG file
- Rename it to fake.txt or fake.jpg
- Hopefully it will still identify it as PNG!

<p align="center">
 
<img src="https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/49cb1bbdef31193fac70278eb012dfe70036d111/Screenshot%202026-01-31%20171935.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<hr>
<br />
<p align="center">
Running the tool - (make sure you're in the magic-number-identifier folder with venv activated) <br/>
<img src="https://github.com/Dylan-W-Clark/File-Type-Identifier/blob/a4256a270ec735f389b2d93f17af0d3b84ca7e11/Screenshot%202026-01-31%20172530.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>

<p align="left">

- As we can see the tool correctly identified the file types and was not fooled by the renaming of the fiile!
</p>
