sandwich_orders = ['cheese', 'bacon', 'gourman', 'egg', 'beef']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I'm working your {current_order} sandwich")
    finished_sandwiches.append(current_order)

print("\n")
for finished_sandwich in finished_sandwiches:
    print(f"I made {finished_sandwich.title()} sandwiches done")
