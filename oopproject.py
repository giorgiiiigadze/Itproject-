class Person:
    def __init__(self, name):
        self.__name = name  # პირადი ცვლადი სახელისთვის

    @property
    def name(self):
        return self.__name  # გეთერი

    @name.setter
    def name(self, new_name):
        self.__name = new_name  # სეთერი


class Student(Person):
    students = []  # სტუდენტების საერთო სია

    def __init__(self, name, roll_number, grade):
        super().__init__(name)
        self.__roll_number = roll_number
        self.__grade = grade
        Student.students.append(self)  # სიაში დამატება

    def __str__(self):
        return f'Name: {self.name}, Roll Number : {self.__roll_number}, Student Grade : {self.__grade}'
    
    # სტუდენტის დამატება
    @classmethod
    def add_new_student(cls, name, roll_number, grade):
        Student(name, roll_number, grade)
        print(f'{name} has been added to the list!')

    # ვამოწმებთ არის თუ არა სტუდენტი მსგავსი სიის რიცხვით
    @classmethod
    def is_roll_number_valid(cls, roll_number):
        for student in cls.students:
            if roll_number == student.__roll_number:
                return False
        return True
    
    # ვამოწმებთ არის თუ არა სახელი ვალიდური
    @staticmethod
    def is_name_valid(name):
        return not name.isdigit()
    
    # ვამოწმებთ არის თუ არა ქულა ვალიდური
    @staticmethod
    def grade_is_valid(grade):
        return 0 <= grade <= 100

    @classmethod
    def show_every_students(cls):
        if not cls.students:
            print("No student inside list")
        return cls.students  # აბრუნებს ყველა სტუდენტს

    @classmethod
    def find_student_wit_roll_number(cls, roll_number):
        # ვეძენთ სტუდენტს სიის ნომრით
        if not cls.students:
            print("No student inside list")
        for student in cls.students:
            if student.__roll_number == roll_number:
                return f"Student with roll number : {roll_number} is {student.name}, their grade is {student.__grade}"
        return f'No student found with roll number {roll_number}'
    
    @classmethod
    def find_student_with_name(cls, name):
        # ვეძენთ სტუდენტს სახელით
 
        for student in cls.students:
            if student.name == name:
                  return f"Student named {student.name}'s roll number is {student.__roll_number}, their grade is {student.__grade}"
        return f'No student found with name {name}'


    @classmethod
    def change_student_grade(cls, roll_number, new_grade):
        # სტუდენტის შეფასების განახლება
        for student in cls.students:
            if student.__roll_number == roll_number:
                student.__grade = new_grade
                return f'Succesfully updated grade, students current grade is {new_grade}'       
        return 'No student found with that roll number'

    @classmethod
    def remove_student(cls, name):
        # სტუდენტის წაშლა სახელის მიხედვით
        if not cls.students:
            return "No student inside library"
        for student in cls.students:
            if student.name == name:
                cls.students.remove(student)
                return "Student has been succesfully removed"
        return "No student found with that information"



def main():
    # მენიუს ვარიანტები
    operations_list = ['1. Add student',
                       '2. Check all students',
                       '3. Find student with roll number',
                       '4. Find student with name',
                       '5. Change student grade',
                       '6. Remove Student',
                       '7. Exit']

    for i in operations_list:
        print(i)

    try:
        while True:
            # ოპერაციის არჩევა
            try:
                operation = int(input("Enter operation(enter integers):"))
            except ValueError:
                print("Please enter valid input")
                continue
            if operation == 1:
                # სტუდენტის დამატება
                try:
                    while True:
                        try:
                            student_name = input("Enter students name:").lower().strip()
                            if Student.is_name_valid(student_name):
                                break
                            print("Name must only include letters")

                        except ValueError:
                            print("Please enter valid information")
                    while True:
                        try:
                            student_roll_number = int(input("Enter students roll number:").strip())
                            if Student.is_roll_number_valid(student_roll_number):
                                break
                            print('Student with same information is already in the list')

                        except ValueError:
                            print("Please enter valid information")
                    while True:
                        try:
                            student_grade = int(input("Enter students grade:").strip())
                            if Student.grade_is_valid(student_grade):
                                break
                            print("Grade must be greater than 0 and lower than 100")
                        except ValueError:
                            print("Please enter valid information")
                    
                    Student.add_new_student(student_name, student_roll_number, student_grade)
                except ValueError:
                    print("Please enter valid input")

            elif operation == 2:
                # ყველა სტუდენტის ნახვა
                try:
                    all_students =  Student.show_every_students()
                    for student in all_students:
                        print(f"{student}")
                except Exception as e:
                    print(e)
            elif operation == 3:
                # სტუდენტის პოვნა სიის ნომრით
                try:
                    find_student_roll_number = int(input("Enter students roll number to find that student:").strip())
                    result = Student.find_student_wit_roll_number(find_student_roll_number)
                    print(result)
                except ValueError:
                    print("Please enter valid input")
                except Exception as e:
                    print(e)

            elif operation == 4:
                # სტუდენტის პოვნა სახელით
                try:
                    find_student_name = input("Enter students Name to find that student:").strip()
                    result = Student.find_student_with_name(find_student_name)
                    print(result)
                except ValueError:
                    print("Please enter valid input")
                except Exception as e:
                    print(e)

            elif operation == 5:
                # შეფასების განახლება
                try:
                    student_roll_number = int(input("Enter students roll number:").strip())
                    while True:
                        try:
                            new_grade = int(input("Enter students updated grade:").strip())
                            if Student.grade_is_valid(new_grade):
                                break
                            print("Grade must be between 0 and 100")
                        except ValueError:
                            print("Please enter valid numeric grade")
                    result = Student.change_student_grade(student_roll_number, new_grade)
                    print(result)
                except ValueError:
                    print("Please enter valid input")
                except Exception as e:
                    print(e)

            elif operation == 6:
                # სტუდენტის წაშლა
                try:
                    student_name = input("Enter students name to remove:").strip()
                    result = Student.remove_student(student_name)
                    print(result)
                except ValueError:
                    print("Please enter valid input")
                except Exception as e:
                    print(e)

            elif operation == 7:
                print("Exiting the code")
                break
            else:
                print("Please Enter valid information!")
    except KeyboardInterrupt:
        print("Input cancelled during code")

# პროგრამის გაშვების წერტილი
if __name__ == '__main__':
    main()