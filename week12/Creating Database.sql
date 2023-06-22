


CREATE TABLE students (
    student_id INT PRIMARY KEY NOT NULL,
    student_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    is_deleted BOOLEAN);

CREATE TABLE departments (
    department_id INT PRIMARY KEY NOT NULL,
    department_name VARCHAR(100) NOT NULL,
    is_deleted BOOLEAN);

CREATE TABLE instructors(
        instructor_id INT PRIMARY KEY NOT NULL,
        instructor_name VARCHAR(50) NOT NULL,
        specialization VARCHAR(100) NOT NULL,
        department_id BIGINT NOT NULL,
        is_deleted BOOLEAN,
        FOREIGN KEY (department_id) REFERENCES departments(department_id));


CREATE TABLE courses (
    course_id INT PRIMARY KEY NOT NULL,
    title VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
    prerequisites_of_id BIGINT,
    is_prerequisites BOOLEAN,
    instructor_id bigint NOT NULL,
    is_deleted BOOLEAN,
    FOREIGN KEY (prerequisites_of_id) REFERENCES courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id));


CREATE TABLE StudentRegistration(
       registration_id INT PRIMARY KEY NOT NULL,
       student_id INT NOT NULL,
       course_id INT NOT NULL,
       FOREIGN KEY (student_id) REFERENCES students(student_id),
       FOREIGN KEY (course_id) REFERENCES courses(course_id));

INSERT INTO departments (department_id,department_name,is_deleted)
VALUES (1, 'Mathematics',false),
        (2,'Computer Science',false);

INSERT INTO students (student_id,student_name,date_of_birth,is_deleted)
VALUES (1, 'Farzam', '1992-08-14', false),
        (2,'Mohammad','1999-07-30',false),
        (3, 'Hossein','2001-04-16',false),
        (4,'Mehdi','1997-10-15',false);

INSERT INTO instructors(instructor_id, instructor_name, specialization, department_id, is_deleted)
VALUES (1, 'Ali','mathematics',1,false),
        (2,'Reza','physics',1,false),
        (3,'Akbar','python',2,false),
        (4,'Asqar','ML',2,false),
        (5,'Rostam','AI',2,false);

INSERT INTO courses (course_id,title,credits,prerequisites_of_id,is_prerequisites,instructor_id, is_deleted)
VALUES (1, 'Python',3,3,true,3, false),
        (2,'ML',3,3,true,4,false),
        (3, 'AI',3,null,false,5,false),
        (4,'Math',3,2,true,1,false);

INSERT INTO StudentRegistration (registration_id,student_id,course_id)
VALUES (1,1,3),
        (2,2,4),
        (3,3,1),
        (4,4,2),
        (5,1,2);

DELETE FROM StudentRegistration
WHERE registration_id =5;

INSERT INTO StudentRegistration (registration_id,student_id,course_id)
VALUES (5,1,2);

DELETE FROM students
WHERE student_name = 'Mohammad';

INSERT INTO students (student_id,student_name,date_of_birth,is_deleted)
VALUES (2,'Mohammad','1999-07-30',false);

UPDATE students
SET student_name = 'Feri'
WHERE student_name = 'Farzam';

UPDATE students
SET student_name = 'Farzam'
WHERE student_name = 'Feri';

ALTER TABLE students
ADD Phone INT;

ALTER TABLE students
DROP Phone;

--DROP TABLE students

ALTER TABLE students
RENAME TO fake_students;

ALTER TABLE fake_students
RENAME TO students;



CREATE VIEW ourse_num_students AS
SELECT title, count(students.student_id)
FROM courses
INNER JOIN StudentRegistration ON StudentRegistration.course_id=courses.course_id
INNER JOIN students ON StudentRegistration.student_id=students.student_id
GROUP BY title;
