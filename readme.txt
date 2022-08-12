







Coursework 1 – Individual Coding Assignment

Student Name: Petar Antonijevic

Module: An Academic Misconduct (AM) Administration Software Application
Submission deadline: Friday 3rd April 2020, by 11:55pm
Module leader: Paul Carden 
Student ID: 3805999








Contents
Introduction	3
Section 1, Data Fields:	3
Section 2, Validation Requirements:	3
Notification Date	3
Module Name	4
Student Name	4
Non-Originality Index	4
Summary	5
Categories of academic investigation	5
AM Hearing	6
AMI Process complete	6
Section 3, Menu:	7
Bibliography	7


Table of figures 
Figure 1	3
Figure 2	3
Figure 3	4
Figure 4	4
Figure 5	4
Figure 6	5
Figure 7	5
Figure 8	6
Figure 9	6
Figure 10	7


Introduction 
This assignment’s aim is to design and implement an academic misconduct administration software application, which will manage Academic Misconduct Investigation (AMI). The programming language used to complete the objective will be by using Python (3.8.1), all of the python concepts learnt so far by the author will be used. A few notable examples would be python collections, functions and files, they will be used to help achieve the objective. 

Section 1, Data Fields:
The author will be using the sample Excel data file, which has 5 records of students. This data will be manipulated in order to test if the codes run correctly. The data consisted in the Excel file will be the following: 
* A Case Number which is a LSBU unique AM record ID
* The Notification Data which is when the student was informed of plagiarism
* Module Code – LSBU module code, CSI-x-yyy
* Module Name
* Student Name
* Non-Originality Index – the level of non-originality as a percentage (Coursework), if 0% (Exam-related)
* Summary – Brief statement of case
* Categories of academic investigation (AMI)
* AM Hearing – Has an appeal been requested or not
* AMI Process complete
This can also be seen in Figure 1, which highlights what the database consists of the following (the data has been entered from the console): 
Section 2, Validation Requirements: 
Notification Date
The first validation requirement would be the notification date which is when the student was informed of the case. The user must enter a date in the format of dd/mm/yy, this is located in the addStudent function. The code below demonstrates the notification date which the author has programmed, the user will be allowed to enter the notification date in ‘dd/mm/yy’ format only. By using a slash (“/”), the date can be split into dd/mm/yy, the datetime checks if the datetime is valid in the try loop. If the user inputs the correct notification date then they will proceed to the next input. However, this may not be the case always and thus the user will be presented with an error “Invalid date, try again. ” and the user will be able to repeat the notification date (codevscolor, 2020). 
date = input("Enter notification date in 'dd/mm/yy' format: ")
      try:  
          day, month, year = date.split("/")  
          datetime.datetime(int(year), int(month), int(day))
          break  
      except ValueError:
          print("Invalid date, try again. ")
Figure 2 demonstrates the user interface output of the code working.
Module Name
The second validation requirement is the module name, the code below demonstrates the module name which the author has programmed. The user must enter the module name and Module_name = input, will allow the user to enter module name. The while(True) keeps looping until it meets the end condition (stackoverflow, 2020).  
           module_name = input("Enter module name: ")
      while(True):  
Figure 3 demonstrates the user interface output of the code working.

Student Name
Student name is another validation requirement, the code below highlights the way in which the user will input a student name. The first line demonstrates how the user is allowed to enter a student name. There are only allowed characters and thus the second line is used to filter out integers or other special symbols which are not allowed. If the user inputs a valid student name then the process will continue and will break, which will end the loop. However, if the user enters an invalid student name, it will print an error “Invalid student name. Try again”) and will make the user try again (stackoverflow, 2016). The while(True) keeps looping until it meets the end condition (Saxena, 2020).  
student_name = input("Enter student name: ")
           if all(x.isalpha() or x.isspace() for x in student_name):
              break  
           else:  
               print("Invalid student name. Try again.")
       while(True):  
           try:  
Figure 4 demonstrates the user interface output of the code working.



Non-Originality Index
Non-originality index is another validation requirement, the code below highlights the way in which the user will input the non-originality index. The first line demonstrates how the user can input the non-originality index, the second line checks that the non-originality entered is a positive integer and is between 0 to 100. The third line changes the integer value to a string, if the user entered a valid non-originality index then the break will end the loop. However, if the user enters an invalid non-originality index then the program will print an error and makes the user try again. ‘Except ValueError’ means that the value a user is using, returns an error if it is incorrect in the try loop and keeps looping until the user inputs a valid integer. 
non_originality_index = int(input("Enter Non Originality index: "))
            if (0 <= non_originality_index <= 100):  
                non_originality_index = str(non_originality_index)
                break  
            else
                print("Invalid Non Originality Index. Try again.")
        except ValueError:  
            print("Invalid Non Originality Index. Try again.")
Figure 5 demonstrates the user interface output of the code working.


Summary
The summary is the brief statement of the case, however if there are commas in the field, it may break the data record for an incident. Thus, the code below replaces the comma with a special character such as a dollar sign ($). The first line allows the user to replace a comma, if used for a dollar sign ($). The second line changes the comma to string character in summary (tutorialspoint, 2020). 
summary = input("Enter summary(if comma is used its replaced with $): ")
    for value in summary:  
        if value == ",":
            value == "$"
Figure 6 demonstrates the user interface output of the code working.

Categories of academic investigation
No case to answer is the default value in this field, until a decision is made the learner is ‘innocent until proven otherwise’. The categories of academic investigation are the next validation requirement, they consist of the following, NCA – No Case to Answer. AMWW - Formal written warning. AMREDC - Mark reduction for component involved. Capping of a whole module mark to not lower than a pass mark. AMREPC - Component to be redone for capped mark. AMREPU - Module failed, can be repeated for capped mark. AMFU - Module failed, no possibility to retake. AMREPS or AMREPY - Failure of all modules in sem/year with possibility of repeating for capped marks. AMTER - Referral to Dean for consideration of termination of studies. The first line is the list of the Poor Academic Practise which the user can choose from. The while(True keeps looping until it meets the end condition. The fourth line prints all of the hearing codes in the list and allows the user to enter the hearing code of their choice. Then the code checks if the input was correct, if the input was valid then it will continue the process. However, if the input was invalid then the user will be presented with an error message and makes the user try again, and this is repeated until the condition is met (stackoverflow, 2014). 
hearing_code = ['NCA', 'AMWW', 'AMREDC', 'AMREPC',
                    'AMREPU', 'AMFU', 'AMREPS or AMREPY', 'AMTER']
    while(True):  
        for value in hearing_code:  
            print('{}\n'.format(value))  
        code_selection = input("Choose hearing code: ")
        if code_selection not in hearing_code:  
            print("Invalid option, please try again. ")
        else:  
            break  
Figure 7 demonstrates the user interface output of the code working. 








AM Hearing 
The Am hearing checks if the appeal has been lodged or not, students can appeal the decision and go before a panel to argue their case if the appeal is accepted. ‘Y’ and ‘N’ is an acceptable value, the first line of the code allows the user to enter ‘Y’ for yes and ‘N’ for no, in regards to the appeal. The second line ensure that if the user entered something other than ‘Y’ or ‘N’ then the code will not continue. If the user inputs an invalid input then the code will print an error and makes the user try again. The loop will continue until the user inputs ‘Y’ or ‘N’.
        am_hearing = input("Has an appeal been lodged? (Y/N): ")
        if (am_hearing.upper() != ('Y' or 'N')):  
            print("Option not valid. Please try again. ")
        else:  
            am_hearing = am_hearing.upper()  
            break
Figure 8 demonstrates the user interface output of the code working.



AMI Process complete 
If the user chooses NCA, which stands for no case to answer, then the case will be automatically closed, as everything is ok. Any other option will provide the user the ability to choose whether the case is closed or not, ‘Y’ and ‘N’ is an acceptable value. The first line in the code keeps looping until it meets the end condition. After, if the user enters ‘NCA’ in the second line then that part is complete and moves on to the menu. However, if the user enters otherwise, then the ami allows the user to enter ‘Y’ or ‘N’ depending whether the case is closed. If the user entered something other than ‘Y’ or ‘N’ then the code will not continue and it will print an error message, which will make the user try again. The last stage of the code converts lower case inputs to upper case, for example if the user inputs lower case ‘y’ instead of upper case ‘Y’ then the code will convert it and continue with the process (Weber, 2020). 
while(True):  
        if code_selection == 'NCA':  # If the user enters 'NCA' then that part is complete
            ami_complete = 'Y'
            break  
        else:  
            ami_complete = input("Is case closed? (Y/N): ")         
            if (ami_complete.upper() != ('Y' or 'N')):               
                print("Option not valid. Please try again. ")
            else:  
                ami_complete = ami_complete.capitalize()  
                break  	
Figure 9 demonstrates the user interface output of the code working.


Section 3, Menu:
The menu consists of six parts, the user is able to enter a new AMI incident, remove an existing incident, change/modify the details of an existing incident, search and display the details for a particular student, display all incident count and average non-originality index and can exit the program. The first 6 lines of the code will be presented to the user at the start, if the user clicks on 1, then they will add a student. If the user clicks on 2, then they will find a student, if the database is not empty then the code will execute the function. If the database is empty, the program will print that the student is not found. If the user clicks on 3, then they will edit a student, if the database is not empty then the code will execute the function. If the database is empty, the program will print that the student is not found. If the user clicks on 4, then they will delete a student, if the database is not empty then the code will execute the function. If the database is empty, the program will print that the student is not found. If the user clicks on 5, then it will display all students, if the database is not empty then the code will execute the function. If the database is empty, the program will print that the student is not found. The last piece of the code is exit, if the user inputs 6 it will end the code (stackoverflow, 2015). 
        menu = int(input('''
    1. Add student
    2. Find student
    3. Edit student
    4. Delete student
    5. Display all students
    6. Exit
    > '''))    
        if menu == 1:  
            addStudent()
        elif menu == 2:  
            if data[1][0] != "":  
                findStudent()
            else:               
                print("Database is empty")
        elif menu == 3:  
            if data[1][0] != "":  
                editStudent()
            else:                 
                print("Database is empty")
        elif menu == 4:  
            if data[1][0] != "":  
                deleteStudent()
            else:                  
                print("Database is empty")
        elif menu == 5:  
            if data[1][0] != "":  
                displayStudents()
            else:                  
                print("Database is empty")
        else:  
            file.close()  
            quit()  
Figure 10 demonstrates the user interface output of the code working.





Bibliography
codevscolor, 2020. How to check if a date is valid or not in python. [Online] 
Available at: https://www.codevscolor.com/date-valid-check-python/
[Accessed 05 03 2020].
Saxena, A., 2020. Python String isalpha() and its application. [Online] 
Available at: https://www.geeksforgeeks.org/python-string-isalpha-application/
[Accessed 01 03 2020].
stackoverflow, 2014. I want to have a yes/no loop in my code, but I'm having trouble doing it (python 3.3). [Online] 
Available at: https://stackoverflow.com/questions/22362165/i-want-to-have-a-yes-no-loop-in-my-code-but-im-having-trouble-doing-it-python
[Accessed 15 03 2020].
stackoverflow, 2015. Python: searching csv and return entire row. [Online] 
Available at: https://stackoverflow.com/questions/26082360/python-searching-csv-and-return-entire-row/26082493
[Accessed 27 03 2020].
stackoverflow, 2016. Checking if string is only letters and spaces - Python. [Online] 
Available at: https://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python
[Accessed 10 03 2020].
stackoverflow, 2020. Deleting rows with Python in a CSV file. [Online] 
Available at: https://stackoverflow.com/questions/29725932/deleting-rows-with-python-in-a-csv-file
[Accessed 22 03 2020].
tutorialspoint, 2020. Python - Files I/O. [Online] 
Available at: https://www.tutorialspoint.com/python/python_files_io.htm
[Accessed 28 03 2020].
Weber, B., 2020. realpython. [Online] 
Available at: https://realpython.com/python-main-function/
[Accessed 20 03 2020].


Student ID: 3805999		Petar Antonijevic                   


2


