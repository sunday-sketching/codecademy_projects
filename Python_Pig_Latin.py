empty_string = ""
if len(empty_string) > 0:
  # Run this block.
  # Maybe print something?
else:
  # That string must have been empty.

# .isalpha(): returns False since the string contains non-letter characters.

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print original
else:
  print "empty"

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha(): # right
  word = original.lower() # right
  first = word[0]         # r
  new_word = word + first + pyg # right + r + ay
  new_word = new_word[1:len(new_word)] # ight
  print new_word # ight+r+ay
else:
    print 'empty'