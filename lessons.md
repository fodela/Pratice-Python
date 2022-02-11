# Everything new thing I learnt Practicing Python

## String Validators

- Documentation: https://docs.python.org/3/library/stdtypes.html

Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum() => checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha() => checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
str.islower()
str.isupper()

see documentation for more

## Reading inputs

.split() => splits strings into list
.strip() => removes leading and trailing whitespaces
.lstrip() => removes trailing whitespace
.rstrip() => removes leading whitespace

## Count element that satisfy a condition

- Create a dictionary
- Set the default to zero
- Increase the value of the element(key) by one per every occurrence of the element
- Use key as count of element

See 'Word order' for a sample
