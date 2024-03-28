% Database of students, teachers, and subjects with codes
entity(student(john), 'S101').
entity(student(lisa), 'S102').
entity(teacher(mary), 'T201').
entity(teacher(david), 'T202').
entity(subject(math), 'M301').
entity(subject(english), 'E302').
entity(subject(history), 'H303').

% Predicate to retrieve subjects taught by a teacher
subjects_taught_by_teacher(TeacherName, Subjects) :-
    entity(teacher(TeacherName), TeacherCode),
    findall(Subject, (entity(subject(Subject), Code), teaches(Code, TeacherCode)), Subjects).

% Predicate to check if a teacher teaches a specific subject
teaches(SubjectCode, TeacherCode) :-
    entity(subject(Subject), SubjectCode),
    entity(teacher(Teacher), TeacherCode),
    teaches_relation(Teacher, Subject).

% Relationships between teachers and subjects
teaches_relation(mary, math).
teaches_relation(david, english).
teaches_relation(david, history).
