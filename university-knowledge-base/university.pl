% --- University Knowledge Base ---

% --- Students and Staff Information ---

% Gender and Age
gender(john, male).
gender(susan, female).
gender(michael, male).
gender(linda, female).
gender(alex, male).
gender(emily, female).
gender(brandon, male).
gender(nina, female).

age(john, 22).
age(susan, 21).
age(michael, 35).
age(linda, 30).
age(alex, 24).
age(emily, 23).
age(brandon, 29).
age(nina, 20).

% Major and Year (only students)
major(john, computer_science).
major(susan, computer_science).
major(alex, mathematics).
major(emily, computer_science).
major(nina, economics).

year(john, 3).
year(susan, 2).
year(alex, 4).
year(emily, 3).
year(nina, 1).

% Courses and Enrollment
teaches(michael, cs101).
teaches(michael, ai301).
teaches(linda, math201).
teaches(brandon, econ101).

enrolled_in(john, cs101).
enrolled_in(susan, cs101).
enrolled_in(alex, math201).
enrolled_in(emily, ai301).
enrolled_in(nina, econ101).
enrolled_in(john, ai301).
enrolled_in(emily, cs101).

% Advisor Relationship
advisor_of(michael, john).
advisor_of(michael, susan).
advisor_of(linda, alex).
advisor_of(michael, emily).
advisor_of(brandon, nina).

% Favorite Subjects
favorite_subject(john, ai).
favorite_subject(susan, data_science).
favorite_subject(alex, algebra).
favorite_subject(emily, robotics).
favorite_subject(nina, microeconomics).

% --- Rules ---

% A person is a student if they have a major
student(X) :-
    major(X, _).

% A person is a staff member if they teach a course
staff(X) :-
    teaches(X, _).

% Two students are classmates if enrolled in the same course
classmate(X, Y) :-
    enrolled_in(X, Course),
    enrolled_in(Y, Course),
    X \= Y.

% A person X is older than Y if X's age is greater
older_than(X, Y) :-
    age(X, AX),
    age(Y, AY),
    AX > AY.

% Two students have the same major
same_major(X, Y) :-
    major(X, M),
    major(Y, M),
    X \= Y.

% Find all students enrolled in a particular course
students_in_course(Course, Student) :-
    enrolled_in(Student, Course),
    student(Student).

% Find the advisor of a student
advisor(Student, Advisor) :-
    advisor_of(Advisor, Student).

% Find all courses taught by a professor
courses_taught_by(Professor, Course) :-
    teaches(Professor, Course).

% Check if a student is in their final year (4th year)
final_year_student(Student) :-
    year(Student, 4),
    student(Student).

% Find students who like a certain subject
likes_subject(Student, Subject) :-
    favorite_subject(Student, Subject).

% Check if two students share at least one course
share_course(Student1, Student2) :-
    enrolled_in(Student1, Course),
    enrolled_in(Student2, Course),
    Student1 \= Student2.

% --- Additional Queries ---

% 1. Find all students
all_students :-
    student(X),
    write(X), nl,
    fail.  % Forces backtracking to get all solutions

% 2. Find all staff (professors and teachers)
all_staff :-
    staff(X),
    write(X), nl,
    fail.  % Forces backtracking to get all solutions

% 3. Find all advisors
all_advisors :-
    advisor_of(Advisor, _),
    write(Advisor), nl,
    fail.  % Forces backtracking to get all solutions

% 4. Find all professors and the courses they teach
all_professors_and_courses :-
    teaches(Professor, Course),
    write(Professor), write(' teaches '), write(Course), nl,
    fail.  % Forces backtracking to get all solutions

% 5. Find all students and the courses they are enrolled in
all_students_and_courses :-
    enrolled_in(Student, Course),
    write(Student), write(' is enrolled in '), write(Course), nl,
    fail.  % Forces backtracking to get all solutions

% 6. Find all classmates
all_classmates :-
    classmate(X, Y),
    write(X), write(' and '), write(Y), write(' are classmates'), nl,
    fail.  % Forces backtracking to get all solutions

% 7. Find all students with the same major
all_students_with_same_major :-
    same_major(X, Y),
    write(X), write(' and '), write(Y), write(' have the same major'), nl,
    fail.  % Forces backtracking to get all solutions

% 8. Find all students who are in the final year (4th year)
all_final_year_students :-
    final_year_student(Student),
    write(Student), nl,
    fail.  % Forces backtracking to get all solutions

% 9. Find all students who like a certain subject
all_students_who_like_subject(Subject) :-
    likes_subject(Student, Subject),
    write(Student), write(' likes '), write(Subject), nl,
    fail.  % Forces backtracking to get all solutions

% 10. Find all students who share at least one course
all_students_sharing_courses :-
    share_course(Student1, Student2),
    write(Student1), write(' shares a course with '), write(Student2), nl,
    fail.  % Forces backtracking to get all solutions

