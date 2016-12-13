# Student

## Description
This class represents a real class @ Codecool, containing mentors and students working at the class.

## Parent class
None

## Attributes

* ```knowledge_level```
  * data type: string
  * description: stores the knowledge level of the students
* ```energy```
  * data type: string
  * description: stores the energy value of the students personally 


## Class methods

### ```generate_local```

Creates a ```Student class``` object having some real-life data from the implementer persons class.


## Instance methods

### ```__init__```
The constructor of the object. 
Calls the Person's constructor, but also set's the attributes above (should raise an error, if any is empty).

#### Arguments

None

#### Return value
None

### ```find_student_by_full_name```

Gives back a student with the same full name as the argument from ```students```
