import random
import string

def create_password(length, lowercase=True, uppercase=True, numbers=True, symbols=True):
  """
# Helps u choose password and customize it as per ypur needs

  Args:
    length: How long you want the password to be.
    lowercase:  Do you want lowercase letters? (True by default)
    uppercase: Do you want uppercase letters? (True by default)
    numbers: Do you want numbers in your password? (True by default)
    symbols: Do you want symbols like !@#$%? (True by default)

  Returns:
    Your shiny new random password!
  """

  # Start with an empty bucket for our characters
  all_chars = ""  
  if lowercase:
    all_chars += string.ascii_lowercase  # Throw in lowercase letters
  if uppercase:
    all_chars += string.ascii_uppercase  # Add some uppercase letters
  if numbers:
    all_chars += string.digits  # Don't forget the numbers
  if symbols:
    all_chars += string.punctuation  # Sprinkle in some symbols for good measure

  # Oops! Did you forget to pick any character types? 
  if not all_chars:
    return "Hold on! You need to pick at least one type of character." 

  # Now, let's build that password!
  password = ''.join(random.choice(all_chars) for _ in range(length)) 
  return password

if __name__ == "__main__":
  # Let's get started! How long do you want your password to be?
  while True:
    try:
      length = int(input("Tell me how long you want your password to be: "))
      if length > 0:
        break  # Got a good length, let's move on!
      else:
        print("A password needs to be at least one character long, right?")
    except ValueError:
      print("Hmm, that doesn't look like a number. Try again!")

  # Okay, now let's customize it. What kinds of characters do you want?
  lowercase = input("Do you want lowercase letters? (y/n): ").lower() == 'y'
  uppercase = input("How about some uppercase letters? (y/n): ").lower() == 'y'
  numbers = input("Should we throw in some numbers? (y/n): ").lower() == 'y'
  symbols = input("And finally, any symbols? (y/n): ").lower() == 'y'

  # Alright, let's put it all together!
  password = create_password(length, lowercase, uppercase, numbers, symbols)
  print("Ta-da! Here's your new password:", password)