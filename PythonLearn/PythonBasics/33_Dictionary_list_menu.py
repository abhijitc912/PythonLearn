available_parts = {"1": "cpu",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }
 
current_choice = None                           # We need to choose the vaule of current_choice such that its not equal to zero
                                                # or any entry we should be doing as our choice which might add a comp part
                                                # unintentionally
computer_parts = []  # create an empty list
 
while current_choice != "0":
    if current_choice in available_parts:       # When you use "in" in a list it checks for the items in the list
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:                            # Since computer_parts in a list, we can only match with
                                                                     # items (cpu, monitor, keyboard, etc) and so have to match
                                                                     # with chosen_part which has similar values instead of
                                                                     # current_choice
            # Chosen part already present in list. So remove it
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
        #    print(current_choice,chosen_part,computer_parts)
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        print(f"Current list: {computer_parts}")
    else:
        print("Please add options from the list:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
 
    current_choice = input("> ")
