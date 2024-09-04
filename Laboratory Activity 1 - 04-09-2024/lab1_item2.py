input_str = input("Enter two space-separated characters: ")
char1, char2 = input_str.split()

greater_char = max(char1, char2)

print("-------------------------------------------")
print(f"The character with greater value is: {greater_char}")
print("-------------------------------------------")
print("This part is Optional to include")
print("Showing the ASCII Codes")
print(f"{char1}: {ord(char1)}")
print(f"{char2}: {ord(char2)}")


