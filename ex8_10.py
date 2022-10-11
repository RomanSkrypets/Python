def show_messages(text_mess, sent_messages):                    # 3 
    while text_mess:                                            #
        current_message = text_mess.pop()                       # 4 get our last element in text_mess
        print(f"Current message: {current_message}")            # 5 print our each element from the end to start  
        sent_messages.append(current_message)                   #6 add each last element to sent_messages list-|
                                                                #                                              |
def send_messages(sent_messages):                               #7 call our list send_messages --------------->|
    print("\nAll new message:")                                 #                                              |
    for delivered_message in sent_messages:                     #8 For each element whose add in sent_messages |
        print(f"Hi, {delivered_message}")                       # print this element                           |
                                                                #                                              |
                                                                #                                              |
                                                                #                                              |
text_mess = ['Hello','Two','Short']                             # 1 List of our non-sent messages              |
sent_messages = []                                              #   Empty list of sent messsages               <

show_messages(text_mess, sent_messages)                         # 2 We invoke our non-sent list & empty list 
send_messages(sent_messages)