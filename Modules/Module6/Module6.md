<div style="text-align:center">
        <img    src="https://www.nylas.com/wp-content/uploads/JSON_Blog_Hero.png"
                title="JSON" 
                width="70%" 
                height="70%" />
</div>
<br>

# [Module 6: Objects and the JSON Format](https://www.geeksforgeeks.org/convert-class-object-to-json-in-python)

<br>

## [What is JSON](https://www.w3schools.com/whatis/whatis_json.asp).
JSON is a format that encodes objects into a string.
* https://realpython.com/python-json/
  
<br>

## [How to define an object](https://www.geeksforgeeks.org/convert-class-object-to-json-in-python/).
* ### [What is an object constructor](https://www.geeksforgeeks.org/constructors-in-python)
  * An object constructor is like a function. It's function is included by default in all classes. it is used by writing a function called `__init__`.You define how many parameters it includes. You also define what variables are stored into your object by assigning them to `self`.

```python

class Student:
  def __init__(self,  id:str, name:str):
    self.id = id
    self.name = name

s = Student("14-146", "Carlos Cobian")

```

<br>

## [Serialization and Deserialization](https://medium.com/swlh/object-serialization-and-deserialization-in-python-5fad3c2970a4)
 Serialization means to convert an object into a string representing an object, and deserialization is its inverse operation (convert string -> object). 
 * [Search winklerrr](https://stackoverflow.com/questions/3316762/what-is-deserialize-and-serialize-in-json)

### json.dump() vs. json.dumps()
* <u>json.dump</u> serializes an object into a file. It takes 2 parameters, the object and the destination file.
* <u>json.dumps</u> or *dump string* serializes an object into a string, that may then be stored into a variable for future use. It's only parameter is the object.

### Serialization of an object into a file
This file will be placed in the same directory as the script being executed.
See the below example. It will not run until our class labeled `ObjectDataType` is defined.

```python
# List of Students
students = [
  Student("14-146", "Carlos Cobian"),
  Student("98-007", "Jose Quintana")
]

# Determine output Directory
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'students.json')

# Serialization
with open(myOutputFilePath, 'w') as outfile:
  # For a single student seen above use: json.dump(s.__dict__, outfile)
  # For loop will include all students in list.
  json.dump([data.__dict__ for data in myDataSet], outfile)

```

### Deserializing using a class
```python
file = open('ExperimentData.json',)
experimentJson = json.load(file)

myObject = ExperimentData(**experimentJson)
```

<br>

# Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module6`</u> directory (Module6.md)`(20pts)`
<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

What does JSON Stand for?

 - Answer: JavaScript Object Notation

Why are JSON formats important?

 - Answer: JSON file format helps in transmit and serialize all types of structured data. Allows you to perform asynchronous data calls without the need to do a page refresh. Helps you to transmit data between a server and web applications.

 Reference : "https://www.guru99.com/json-tutorial-example.html#:~:text=Application%20of%20JSON,-Here%20are%20some&text=Helps%20you%20to%20transfer%20data,a%20server%20and%20web%20applications".

Create an example of a JSON object with at least 4 values. It may represent anything but it must be original.

 - Answer:
experimentFacts = {
   "animal" : "zebra",
   "food" : "grass",
   "velocity" : 40,
   "habitat" : "savanna woodlands"
 }

What is the difference between serialization and deserialization?

 - Answer: Serialization converts the state of an object into a byte stream. Deserialization uses the byte stream to recreate the object.
 
 Reference :"https://www.geeksforgeeks.org/serialization-in-java/#:~:text=Serialization%20is%20a%20mechanism%20of,used%20to%20persist%20the%20object."

Research data persistance. What did you find?

 - Answer: Data Persistence is a means for an application to persist and retrieve information from a non-volatile storage system.

 Reference : "https://www.ibm.com/docs/en/was-liberty/nd?topic=overview-java-persistence-api-jpa" 

Type down any class notes below this sentence:



Lackluster responses may result in point deductions.
-->

<br>

## [Next Module ->](/../../tree/main/Modules/Module7/Module7.md)