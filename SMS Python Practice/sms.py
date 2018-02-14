"""Interactive console
run: Run the main interactive loop.
"""
from student import StudentsandCourses

def run():
    """ (NoneType) -> NoneType

    Run the main interactive loop.
    """
    Classes = StudentsandCourses()
    commandlist = []
    while True:
        command = input('')

        if command == 'exit':
            break
        elif 'undo' in command:
            if len(commandlist) ==0:
                print('ERROR: No commands to undo.')
            elif len(command.split()) == 1:
                command = command.split()
                if len(command) == 1:
                    #undoes the last command
                    if commandlist[-1][0] == 'create':
                        Classes.studentlist.pop()
                        commandlist = commandlist[:-2]
                    elif commandlist[-1][0] == 'enrol':
                        Classes.CourseDict[commandlist[-1][2]].pop()
                        commandlist = commandlist[:-2]
                    elif commandlist[-1][0] == 'drop':
                        Classes.Coursedict[commandlist[-1][2]].append\
                            (commandlist[-1][1])
                        commandlist = commandlist[:-2]
            else:
                #finds the command index and then undoes everything succeeding it
                command = command.split()
                if (command[1] is float) or (command[1] <=0):
                    print('ERROR: <' +str(command[1] + '> is not a positive natural number.'))
                else:
                    n = command[1]
                    i = 0
                    while (i < n) and (len(commandlist) != 0):
                        if commandlist[i -1][0] == 'create':
                            Classes.studentlist.pop()
                            commandlist = commandlist[:n-2]
                            n -= 1
                            i += 1
                        elif commandlist[i-1][0] == 'enrol':
                            Classes.CourseDict[commandlist[i-1][2]].pop()
                            commandlist = commandlist[:n-2]
                            n -= 1
                            i += 1
                        elif commandlist[i-1][0] == 'drop':
                            Classes.Coursedict[commandlist[i-1][2]].append\
                                (commandlist[i-1][1])
                            commandlist = commandlist[:n-2]
                            n -= 1
                            i += 1
        else:
            #runs through the list of commands in the assignment
            command = command.split()
            if (command[0] == 'create') and (command[1] == 'student'):
                if Classes.Student(command[2]) == None:
                    commandlist.append(command)
                else:
                    print(Classes.Student(command[2]))

            elif command[0] == 'enrol':
                if Classes.course(command[2], command[1]) == None:
                    Classes.course(command[2], command[1])
                else:
                    print(Classes.course(command[2], command[1]))
                    Classes.course(command[2], command[1])
                commandlist.append(command)

            elif command[0] == 'drop':
                if Classes.dropcourse(command[2], command[1]) == None:
                    Classes.dropcourse(command[2], command[1])
                else:
                    print(Classes.dropcourse(command[2], command[1]))
                    Classes.dropcourse(command[2], command[1])
                commandlist.append(command)

            elif command[0] == 'list-courses':
                print(Classes.givecourses(command[1]))

            elif command[0] == 'common-courses':
                print(Classes.commoncourses(command[1], command[2]))

            elif command[0] == 'class-list':
                print(Classes.classlist(command[1]))

            else:
                print('Unrecognized command!')


if __name__ == '__main__':
    run()
