import datetime
# datatime lets you use datetime features


def addStudent():  # defines a function to add a student

    # incident = input, allows the user to enter an incident number
    incident = input("Enter incident number: ")

    # student_id = input, allows the user to enter a student id
    student_id = input("Enter student id: ")

    while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

        # date = input, allows the user to enter a notifcation date in dd/mm/yy format
        date = input("Enter notification date in 'dd/mm/yy' format: ")

        try:  # implements expection handling, means if you have any errors it can handle it and counter it with a different thing

            day, month, year = date.split("/")  # It splits everything a user inputs by its slash/

            # Check if datetime is valid in try loop
            datetime.datetime(int(year), int(month), int(day))

            break  # Break = just ends loop

        except ValueError:
            # Meaning that the value a user is using returns an error if it is incorrect, sees if there is an error in try loop

            print("Invalid date, try again. ")  # It prints an error and makes the user try again

    # Module_code = input, allows the user to enter module code
    module_code = input("Enter module code: ")

    # Module_name = input, allows the user to enter module name
    module_name = input("Enter module name: ")

    while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

        # Student_name = inputs, allows the user to enter a student name
        student_name = input("Enter student name: ")

        if all(x.isalpha() or x.isspace() for x in student_name):
            # Checks every value in student name, you can't have number on student name for example

            break  # Break = just ends loop

        else:  # Body of else is executed

            # It prints an error and makes the user try again
            print("Invalid student name. Try again.")

    while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

        try:  # implements expection handling, means if you have any errors it can handle it and counter it with a different thing

            non_originality_index = int(input("Enter Non Originality index: "))
            # non_originality_index = int, allows the user to enter the Non Originality index

            if (0 <= non_originality_index <= 100):  # This checks that the Non Originality index entered is between 0 to 100

                # Changes the integer value to a string
                non_originality_index = str(non_originality_index)

                break  # Break = just ends loop

            else:  # Body of else is executed

                # It prints an error and makes the user try again
                print("Invalid Non Originality Index. Try again.")

        except ValueError:  # Meaning that the value a user is using returns an error if it is incorrect, sees if there is an error in try loop

            # It prints an error and makes the user try again
            print("Invalid Non Originality Index. Try again.")

    summary = input("Enter summary(if comma is used its replaced with $): ")
    # summary = input, allows the user to replace a comma, if used for a $

    for value in summary:  # Changes comma to a string character in summary

        if value == ",":

            value == "$"

    hearing_code = ['NCA', 'AMWW', 'AMREDC', 'AMREPC',
                    'AMREPU', 'AMFU', 'AMREPS or AMREPY', 'AMTER']
    # These are the list of the Poor Academic Practise which the user can choose from

    while(True):  # keeps looping until it meets end condition. True always evaluates to Boolean "True"

        for value in hearing_code:  # Forloop

            print('{}\n'.format(value))  # Prints all of the hearing codes in the list

        # code_selection = input, allows the user to enter the hearing code
        code_selection = input("Choose hearing code: ")

        if code_selection not in hearing_code:  # Checks if the input was correct

            # It prints an error and makes the user try again
            print("Invalid option, please try again. ")

        else:  # Body of else is executed

            break  # Break = just ends loop

    while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

        # am_hearing = input, allows the user to enter Yes or No for the appeal
        am_hearing = input("Has an appeal been lodged? (Y/N): ")

        if (am_hearing.upper() != ('Y' or 'N')):  # If the entered something other than 'Y' or 'N', then the code will not continue

            # It prints an error and makes the user try again
            print("Option not valid. Please try again. ")

        else:  # Body of else is executed
            am_hearing = am_hearing.upper()  # That is changing what the user inputted in the upper case

            break  # Break = just ends loop

    while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

        if code_selection == 'NCA':  # If the user enters 'NCA' then that part is complete

            ami_complete = 'Y'

            break  # Break = just ends loop

        else:  # Body of else is executed

            ami_complete = input("Is case closed? (Y/N): ")
            # ami_complete = input, allows the user to enter 'Y' or 'N', whether the case is closed

            # If the entered something other than 'Y' or 'N', then the code will not continue
            if (ami_complete.upper() != ('Y' or 'N')):

                # It prints an error and makes the user try again
                print("Option not valid. Please try again. ")

            else:  # Body of else is executed

                ami_complete = ami_complete.capitalize()  # Just changing it to a capital letter

                break  # Break = just ends loop

    # The python file is connected with the Excel CSV file
    file = open("cwksampledata.csv", "a", encoding="utf-8-sig")

    file.write("{},{},{},{},{},{},{},{},{},{},{}\n".format(
        incident, date, module_code, module_name, student_id, student_name, non_originality_index, summary, code_selection, am_hearing, ami_complete))
    # Writes to the file

    file.close()  # Closes the file


def findStudent():  # This option will apear to the user to find students in the Excel file

    file = open("cwksampledata.csv",  "r", encoding='utf-8-sig')
    # This will connect the Excel file to the user in order to find a student

    data = []  # Data is a list

    for row in (file):  # For each role in the file, split the row by a comma, then adds items in role through data list

        terms = row.split(",")  # Split the row by a comma

        data.append(terms)  # Adds each item to the data list

    # student_id = int, allows the user to enter the Student ID
    student_id = int(input("Enter student ID: "))

    print(data)  # Prints the list
    for i in range(0, len(data)):
        print("!" + data[i][4] + "! ")

        if data[i][4] == str(student_id):

            found = data[i]  # If the student ID is found, the process will go ahead

    if (i > len(data)):  # If the length goes beyond the limit then the student will not be found

        print("Student not in database")  # It will print that the student is not in the database

    else:  # Body of else is executed

        print(" | ".join(data[0]))  # Both print found student

        print(" | ".join(found))


def editStudent():  # This option will apear to the user to edit students in the Excel file

    displayStudents()  # This will display all students

    file = open("cwksampledata.csv",  "r", encoding='utf-8-sig')
    # This will connect the Excel file to the user in order to find a student

    data = []  # Data is a list

    for row in (file):  # For each role in the file, split the row by a comma, then adds items in role through data list

        terms = row.split(",")  # Split the row by a comma

        data.append(terms)  # Adds each item to the data list

    # student_id = int, allows the user to enter the Student ID
    student_id = int(input("Enter student ID: "))

    for i in range(0, len(data)):

        if data[i][4] == str(student_id):

            found = data[i]  # If the student ID is found, the process will go ahead

    if (i > len(data)):  # If the length goes beyond the limit then the student will not be found

        print("Student not in database")  # It will print that the student is not in the database

    else:  # Body of else is executed

        temp = found  # Used to store data

        data.remove(found)  # Removes found data

        while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

            try:  # implements expection handling, means if you have any errors it can handle it and counter it with a different thing

                non_originality_index = int(input("Enter Non Originality index: "))
                # non_originality_index = int, allows the user to enter the Non Originality index

                if (0 <= non_originality_index <= 100):  # This checks that the Non Originality index entered is between 0 to 100

                    # Changes the integer value to a string
                    non_originality_index = str(non_originality_index)

                    break  # Break = just ends loop

                else:  # Body of else is executed

                    # It prints an error and makes the user try again
                    print("Invalid Non Originality Index. Try again.")

            except ValueError:
                # Meaning that the value a user is using returns an error if it is incorrect, sees if there is an error in try loop

                # It prints an error and makes the user try again
                print("Invalid Non Originality Index. Try again.")

        hearing_code = ['NCA', 'AMWW', 'AMREDC', 'AMREPC',
                        'AMREPU', 'AMFU', 'AMREPS or AMREPY', 'AMTER']
        # These are the list of the Poor Academic Pratice which the user can choose from

        while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

            for value in hearing_code:  # Forloop

                print('{}\n'.format(value))  # Prints all of the hearing codes in the list

            code_selection = input("Choose hearing code: ")
            # code_selection = input, allows the user to enter the hearing code

            if code_selection not in hearing_code:  # Checks if the the input was correct

                # It prints an error and makes the user try again
                print("Invalid option, please try again. ")

            else:  # Body of else is executed

                break  # Break = just ends loop

        while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

            am_hearing = input("Has an appeal been lodged? (Y/N): ")
            # am_hearing = input, allows the user to enter Yes or No for the appeal

            if (am_hearing.upper() != ('Y' or 'N')):
                # If the entered something other than 'Y' or 'N', then the code will not continue

                # It prints an error and makes the user try again
                print("Option not valid. Please try again. ")

            else:  # Body of else is executed

                am_hearing = am_hearing.upper()  # That is changing what the user inputted in the upper case

                break  # Break = just ends loop

        while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

            if code_selection == 'NCA':  # If the user enters 'NCA' then that part is complete

                ami_complete == 'Y'

                break  # Break = just ends loop

            else:  # Body of else is executed

                ami_complete = input("Is case closed? (Y/N): ")
                # ami_complete = input, allows the user to enter 'Y' or 'N', whether the case is closed

                if (ami_complete.upper() != ('Y' or 'N')):
                    # If the entered something other than 'Y' or 'N', then the code will not continue

                    # It prints an error and makes the user try again
                    print("Option not valid. Please try again. ")

                else:  # Body of else is executed

                    ami_complete = ami_complete.upper()

                    break  # Break = just ends loop

        temp[6] = non_originality_index  # Update values

        temp[8] = code_selection  # Update values

        temp[9] = am_hearing  # Update values

        temp[10] = ami_complete  # Update values

        data.append(temp)  # Update values

        file = open("cwksampledata.csv", "w", encoding='utf-8-sig')
        # This will connect the Excel file to the user in order to edit the students

        for i in range(0, len(data)):

            file.write("{},{},{},{},{},{},{},{},{},{},{}".format(
                data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10]))
            # Writes to the file

        file.close()  # Closes the file


def deleteStudent():  # This option will apear to the user to delete students in the Excel file

    displayStudents()  # This will display all students

    file = open("cwksampledata.csv",  "r", encoding='utf-8-sig')
    # This will connect the Excel file to the user in order to delete a student

    data = []  # Data is a list

    for row in (file):  # For each role in the file, split the row by a comma, then adds items in role through data list

        terms = row.split(",")  # Split the row by a comma

        data.append(terms)  # Adds each item to the data list

    # student_id = int, allows the user to enter the Student ID
    student_id = int(input("Enter student ID: "))

    for i in range(0, len(data)):

        if data[i][4] == str(student_id):

            found = data[i]  # If the student ID is found, the process will go ahead

    if (i > len(data)):  # If the length goes beyond the limit then the student will not be found

        print("Student not in database")  # It will print that the student is not in the database

    else:  # Body of else is executed

        data.remove(found)  # Removes found data

        file = open("cwksampledata.csv", "w", encoding='utf-8-sig')
        # This will connect the Excel file to the user in order to delete a student

        for i in range(0,
                       len(data)):

            file.write("{},{},{},{},{},{},{},{},{},{},{}".format(
                data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8], data[i][9], data[i][10]))
            # Writes to the file

        file.close()  # Closes the file


def displayStudents():  # This option will apear to the user to display all students in the Excel file
    file = open("cwksampledata.csv",  "r", encoding='utf-8-sig')
    # This will connect the Excel file to the user in order to find a student

    for row in (file):  # For each role in the file, split the row by a comma, then adds items in role through data list

        terms = row.split(",")  # Split the row by a comma

        print(" | ".join(terms))

    file.close()


def main():  # Main function, where everything will run from

    try:  # implements expection handling, means if you have any errors it can handle it and counter it with a different thing

        # This will connect the Excel file to the user
        file = open("cwksampledata.csv",  "r", encoding='utf-8-sig')

        data = []  # Data is a list

        for row in (file):  # For each role in the file, split the row by a comma, then adds items in role through data list

            terms = row.split(",")  # Split the row by a comma

            data.append(terms)  # Adds each item to the data list

    except FileNotFoundError:  # If file does not exist, create file

        # This will connect the Excel file to the user
        file = open("cwksampledata.csv", "w", encoding='utf-8-sig')

    file = open("cwksampledata.csv",  "r", encoding='utf-8-sig')

    data = []  # Data is a list

    for row in (file):  # For each role in the file, split the row by a comma, then adds items in role through data list

        terms = row.split(",")  # Split the row by a comma

        data.append(terms)  # Adds each item to the data list¬

    while(True):  # keeps looping until it meets end condition. True always evalutes to boolean "True"

        menu = int(input('''
    1. Add student
    2. Find student
    3. Edit student
    4. Delete student
    5. Display all students
    6. Exit
    > '''))    # This is the menu which the user will first see

        if menu == 1:  # If the user clicks on 1, then they will add a student

            addStudent()

        elif menu == 2:  # If the user clicks on 2, then they will find a student

            if data[1][0] != "":  # If the database is not empty, execute function

                findStudent()

            else:  # Body of else is executed

                # It will print database is empty if the student is not found
                print("Database is empty")

        elif menu == 3:  # If the user clicks on 3, then they will edit a student

            if data[1][0] != "":  # If the database is not empty, execute function

                editStudent()

            else:  # Body of else is executed

                # It will print database is empty if the student is not found
                print("Database is empty")

        elif menu == 4:  # If the user clicks on 4, then they will delete a student

            if data[1][0] != "":  # If the database is not empty, execute function

                deleteStudent()

            else:  # Body of else is executed
                # It will print database is empty if the student is not found
                print("Database is empty")

        elif menu == 5:  # If the user clicks on 5, then it will display all students

            if data[1][0] != "":  # If the database is not empty, execute function

                displayStudents()

            else:  # Body of else is executed

                # It will print database is empty if the student is not found
                print("Database is empty")

        else:  # Body of else is executed

            file.close()  # It will close the flie

            quit()  # It will close the program


if __name__ == "__main__":  # Run the main function, when the program starts

    main()
