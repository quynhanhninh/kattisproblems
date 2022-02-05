def main():
    # Get input
    task = input('Enter a sentence for Encoding (E) or Decoding (D): ')
    text = task[2::] # Create a string with only the sentence to encode/decode

    # Check for Encoding/Decoding mode
    if task[0] == 'E':
        encode(text)
    else:
        decode(text)

def encode(text):
    # Count the repetition of items in text and return a string of letter-number pairs
    result = ''
    for i in range(len(text)):
        item = text[i]
        if result:
            if result[-1] != item: # item is different from previous item
                result += str(count_rep) # add count_rep of previous item to string result
                count_rep = 1
                result += item
                if i == len(text) -1:
                    result += str(count_rep)
            else: # item is repeated
                count_rep += 1
                if i == len(text) -1:
                    result += str(count_rep)
        else: # this is the first item in text
            count_rep = 1
            result += item
            if i == len(text) -1:
                    result += str(count_rep)
    print(result)

def decode(text):
    result = ''
    for i in range(1, len(text), 2):
      result += int(text[i]) * text[i-1]
    print(result)
        
if __name__ == '__main__':
    main()