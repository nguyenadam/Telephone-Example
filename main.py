import adam
import emma
import johnny

students = [adam, emma, johnny]

phrase = "The cat in the hat."
print("Original Phrase: " + phrase)

for student in students:
  phrase = student.telephone(phrase)
  print(student.__name__ + " - " + phrase)