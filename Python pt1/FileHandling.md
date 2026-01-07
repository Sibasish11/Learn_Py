# File Handling

So far we have seen different Python data types. We usually store our data in different file formats. In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section. First, let us get familiar with handling files with common file format(.txt).

File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use _open()_ built-in function.

```py
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
```

- "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
- "a" - Append - Opens a file for appending, creates the file if it does not exist
- "w" - Write - Opens a file for writing, creates the file if it does not exist
- "x" - Create - Creates the specified file, returns an error if the file exists
- "t" - Text - Default value. Text mode
- "b" - Binary - Binary mode (e.g. images)

### Opening Files for Reading

The default mode of _open_ is reading, so we do not have to specify 'r' or 'rt'. I have created and saved a file named reading_file_example.txt in the files directory. Let us see how it is done:

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

As you can see in the example above, I printed the opened file and it gave  some information about it. Opened file has different reading methods: _read()_, _readline_, _readlines_. An opened file has to be closed with _close()_ method.

- _read()_: read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the *read(number)* method.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

Instead of printing all the text, let us print the first 10 characters of the text file.

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# output
<class 'str'>
This is an
```

- _readline()_: read only the first line

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# output
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: read all the text line by line and returns a list of lines

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

Another way to get all the lines as a list is using _splitlines()_:

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

After we open a file, we should close it. There is a high tendency of forgetting to close them. There is a new way of opening files using _with_ - closes the files by itself. Let us rewrite the the previous example with the _with_ method:

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### Opening Files for Writing and Updating

To write to an existing file, we must add a mode as parameter to the _open()_ function:

- "a" - append - will append to the end of the file, if the file does not it creates a new file.
- "w" - write - will overwrite any existing content, if the file does not exist it creates.

Let us append some text to the file we have been reading:

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

The method below creates a new file, if the file does not exist:

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### Deleting Files

We have seen in previous section, how to make and remove a directory using _os_ module. Again now, if we want to remove a file we use _os_ module.

```py
import os
os.remove('./files/example.txt')

```

If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## File Types

### File with txt Extension

File with _txt_ extension is a very common form of data and we have covered it in the previous section. Let us move to the JSON file

### File with json Extension

JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.

_Example:_

```py
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```
