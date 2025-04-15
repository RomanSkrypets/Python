def show_messages(messages):
    for message in messages:
        msg = f"There is {message.upper()}"
        print(msg)

messages = ['big pack', 'small pack', 'medium pack', 'strange pack']
show_messages(messages)