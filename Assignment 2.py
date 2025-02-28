booking = [
    ["unmute","nations cup"],  # name
    ["7 pm", "8pm"],  # time
    ["7 april", "19 may"],  # date
    ["hall 1", "sport hall"],  # venue
    ["concert", "sport competition"]   # decription
]

allAttendees = [[], []]

attendees, ID = allAttendees[0], allAttendees[1]


while True:
    print("***********************************")
    print("        Event Managing System      ")
    print("***********************************")
    print("Options:")
    print("1. Adding an Event")
    print("2. Update Event Details")
    print("3. Delete an Event")
    print("4. Manage Attendees")
    print("5. Print Event Schedule")
    print("6. Exit")
    print("***********************************")

    option = (input("Please select an option:"))

    if option == "4":
     details = [[], [], [], [], []]
    name, time, date, venue, allAttendees = details[0], details[1], details[2], details[3], details[4]
    allAttendees = [[], []]
    attendees, ID = allAttendees[0], allAttendees[1]

    while True:
        print("***********************************")
        print("          Manage Attendees         ")
        print("***********************************")
        print("Options:")
        print("1. Add Attendees")
        print("2. Update Attendee Information")
        print("3. Delete Attendee Information")
        print("4. Print All Attendee Information")
        print("5. Quit")
        print("***********************************")

        choice = input("Please select an option:")

        if choice == "1":
            leave=True
            while leave==True:
                add_att = input('Add Attendee: ')
                while leave:
                    add_ID = input('Add Attendee ID: ')
                    if add_ID.isdigit and len(add_ID)==8:
                        attendees.append(add_att)
                        ID.append(add_ID)
                        print("Attendee:", attendees[-1], "ID:", ID[-1])
                        break
                    else:
                        print ("Invalid ID")
                        print ("ID consists of 8 numbers")
                        print ()      
                    attendees.append(add_att)
                    ID.append(add_ID)

                while True:
                    decide = input("Do you want to add another attendee?(Y/N):")
                    if decide.lower()== 'y':
                        break
                    elif decide.lower()=='n':
                        leave = False
                        break
                    else:
                        print("Invalid Input")

            index = 0
            while index < len(attendees):
                print(attendees[index], ID[index])
                index += 1

        elif choice == "2":
            while True:
                print("***********************************")
                print("    Update Attendee Information    ")
                print("***********************************")
                print("Options:")
                print("1. Update Name")
                print("2. Update ID")
                print("3. Quit")
                print("***********************************")
                option = input("What would you like to change?")
                if option=="1":
                    print("Which attendee's name whould you like to change?")
                    att_ID = input ("Please enter attendee ID:")
                        
                    if att_ID in ID:
                        index = ID.index(att_ID)
                        new_name = input('Enter new name: ')
                        attendees[index] == new_name
                        yesno = input("Are you sure? (Y/N): ")
                        if yesno.lower() == 'y':
                            attendees[index] == new_name
                            attendees.append(new_name)
                            print("Attendee name successfully updated!")
                            print("Attendee:", attendees[-1], "ID:", ID[-1])
                                
                        elif yesno.lower() == 'n':
                             pass
                        else:
                            print("Please select (Y/N)")
                    else:
                        print("Attendee not found")

                elif option=="2":
                     
                    print("Which attendee's student ID would you like to change?")
                    att_name = input ("Please enter attendee name:")
                    if att_name in attendees:
                        attendees == att_name.lower()
                        index = attendees.index(att_name)
                        new_ID = input('Enter the new ID: ')

                        if new_ID.isdigit() and len(new_ID) == 8:
                            yesno = input("Are you sure? (Y/N): ")
                            
                            if yesno.lower() == 'y':
                                if new_ID.isdigit() and len(new_ID) == 8:
                                    ID[index] == new_ID
                                    ID.append(new_ID)
                                    print("Attendee ID successfully updated.")
                                    print("Attendee:", attendees[-1], "ID:", ID[-1])
                                
                                else:
                                    print("Invalid ID")
                                    print("ID consists of 8 numbers")
                                    
                            elif yesno.lower() == 'n':
                                 pass
                        else:
                            print ("Attendee not found.")
                        
                elif option=="3":
                    break
                    
                else:
                    print("Invalid Option")
                    print("Please select between (1-3).")

        elif choice == "3":
            
            print(attendees[index], ID[index])
            print("Which attendee would you like to delete?")
            delete_attendee = input("Please enter attendee name:")
            
            for attendee in attendees:
                if attendee.lower() == delete_attendee.lower():
                    index = attendees.index(attendee)

                    yesno = input("Are you sure?(Y/N): ")

                    if yesno.lower() == 'y':
                        if index == attendees.index(delete_attendee):
                            del attendees[index]
                            del ID[index]
                            print("Attendee successfully deleted")
                            print("Attendee List:")
                            print("Attendee:", attendees[-1], "ID:", ID[-1])
                        else:
                             print("Attendee not found")
                    elif yesno.lower()=='n':
                        pass
                    else:
                        print("Please select (Y/N)")
        elif choice=="5":
            break
