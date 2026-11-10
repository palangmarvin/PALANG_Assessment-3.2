from Array import letters

print("\n=== IV. STACK IMPLEMENTATION (LIFO) ===")
stack = []

print("Pushing letters onto the Stack:")
for letter in letters:
    stack.append(letter)  # PUSH
    print(f"PUSH {letter} | Top -> {stack[::-1]}")

print("\nPopping letters from the Stack:")
while len(stack) > 0:
    popped = stack.pop()  # POP from the end (top)
    print(f"POP {popped} | Remaining Stack (Top -> Bottom): {stack[::-1] if stack else 'Empty'}")

print("Stack is empty\n")