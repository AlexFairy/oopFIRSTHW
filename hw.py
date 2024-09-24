# Task#1
import mood_responses

mood = input("How are you feeling today? ")


print(mood_responses.mood_response(mood))

# Task 2
import text_utils

def main():
  while True:
    print("Selection an option")
    print("1. Reverse a string\n2. Capitalize a string\n3. End")
    choice = input("Make selection: ")

    if choice == '1':
      write_string = input("write string: ")
      s = write_string
      print(text_utils.reverse_string(s))

    elif choice == '2':
      write_string = input("Write string: ")
      s = write_string
      print(text_utils.capitalize_string(s))
    
    elif choice == '3':
      break

if __name__ == "__main__":
  main()