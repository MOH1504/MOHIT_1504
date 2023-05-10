#What relationship is appropriate for Student and Person?


"""In object-oriented programming, the appropriate relationship between the Student and Person classes/entities 
    is an inheritance relationship, where the Student class inherits from the Person class.

This means that a Student is a type of Person and shares all the properties and methods of a Person, as well
as having additional properties and methods specific to a Student.

For example, a Person class might have properties such as "name", "age", and "address", while a Student class 
might have additional properties such as "student ID", "major", and "GPA". By inheriting from the Person class,
the Student class can reuse the properties and methods of the Person class, while also adding its own properties
and methods.

In terms of the database design, a common approach is to have a single "Persons" table that stores information
about all individuals, including students, faculty, and staff, with a unique identifier for each person. Then, 
there would be a separate "Students" table that stores information specific to students, including a foreign key
reference to the corresponding person in the "Persons" table. This allows for efficient querying and updating of
both the shared and specific information for students.
"""