# Person
## Description
This class represents a Person in real life, but we only use it to inherit it's features in Student and Mentor classes
## Parent class
None

## Attributes

* ```first name```
  * data type: list
  * description: stores the the first name of the persons
* ```last name```
  * data type: list
  * description: stores the the last name of the persons
* ```year of birth```
   * data type: list 
   * description: stores the persons year of birth
* ```gender```
  * data type: string
  * description: assumes(triggered) the gender of the person

## Class methods

### ```generate_local```

Creates a ```Person``` object having some real-life data from the implementer students and mentors
#### Arguments
None

#### Return value

```Person``` object

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
It should raise an error, if any of the attributes is empty, and also if the provide gender is not valid
