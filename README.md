# Telephone Coding Project
## Objective:
Reinforce student understanding of methods/functions and string manipulation through a fun interactive project.

SWBAT:
- Effectively write methods in x language
- Alter and manipulate strings in x language

## Overview:
Each student writes their own method that takes in a phrase and modifies it in some way. Some potential ideas include, changing one character, removing or adding a word, or even trying to fix the previous person's mistake.

```javascript
function telephone(input) {
  /* make changes here */
  return new_input
}
```

There is significant potential here for ambitious students to explore a lot, and it's also a good way to help bring struggling students up to par on the concepts.

## Example:
Say a student, Adam, just wants to change one part of the phrase. Maybe he wants to "increment" the first letter, so A -> B, B -> C, etc.

Shown below is an example of how he could do this in python. Notice that while this example seems simple in concept, actually implementing it involves a significant understanding of coding. 

```python
def telephone(phrase):

  # making small modification to the input
  phrase = list(phrase)
  phrase[0] = chr(ord(phrase[0]) + 1)
  return "".join(phrase)
```

After the class has finished writing their individual functions, they should all be submitted to the teacher. The teacher can then load all of the files and run the functions consecutively. Shown below is an example of how that can be acomplished:

```python
import adam
import emma
import johnny

students = [adam, emma, johnny]

phrase = "The cat in the hat."
print("Original Phrase: " + phrase)

for student in students:
  phrase = student.telephone(phrase)
  print(student.__name__ + " - " + phrase)
```

*adam*, *emma*, and *johnny* are all other files created by the students. They should each contain a method called telephone() that takes in a string and returns a new string. 

The output produced by this code block is as follows:

```plaintext
Original Phrase: The cat in the hat.
adam - Uhe cat in the hat.
emma - Uhe cat in the
johnny - the cat in the
```

As you can see, Adam altered one letter in the phrase, Emma removed a whole word, and Johnny attempted to fix the phrase. 