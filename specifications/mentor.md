# Mentor

## Description
This class contains information about the beloved mentors @ Codecool, mainly nicknames and them as a list.

## Parent class
Person

## Attributes

* ```nickname```
  * data type: string
  * description: The nickname of a specific mentor

## Class methods

### ```create_by_csv```
Gets a csv file path as an argument (the csv contains all the data needed to instantiate a mentor object) and gives back a list of mentors.

#### Arguments
File path to the csv file of the mentors.
  
#### Return value
None

## Instance methods

### ```__init__```
The constructor of the object. The class also has a constructor, which calls the Person's constructor, but also set's the nickname attribute (should raise an error, if empty).

#### Arguments

All of the arguments of the class itself.

#### Return value
None
