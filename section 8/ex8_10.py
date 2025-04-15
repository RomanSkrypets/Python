messages = ['big pack', 'small pack', 'medium pack', 'strange pack']
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(f"List of messages: {message}")

def send_messages(messages, sent_messages):
    print("\nThe delivery message: ")
    while messages:
        current_message=messages.pop()
        print(current_message)
        sent_messages.append(current_message)

    
show_messages(messages)
send_messages(messages,sent_messages)

print(f"\nFinal message:")
print(f"Message list: {messages}")
print(f"Sent messages list: {sent_messages}")