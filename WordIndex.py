#WordIndex.py
#Name:Pierce Limbo
#Date: 10/5/2025
#Assignment: Lab 6 

def main():
  textFile = open("fish.txt", 'r')

  with textFile as textFile:
  words = {}
  line_number = 0
  
      for line in textFile:
          line_number += 1
          clean_line = line.strip().lower()
          word_list = clean_line.split()

          for word in word_list:
            if word not in words:
              words[word] = [line_number]
            elif line_number not in words[word]:
              words[word].append(line_number)

print("Word Index:")
      for word in sorted(words.keys()):
        print(f"{word}: {words[word]}")
        


if __name__ == '__main__':
  main()
