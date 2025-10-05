#WordCount.py
#Name:Pierce Limbo
#Date:10/5/2025
#Assignment: Lab6

def main():
  
  textFile = open("gettysberg.txt", 'r')

  with textFile as TextFile:
    line_count = 0
    word_count = 0
    character_count = 0
  
  for line in textFile:
    print(line)
    line_count += 1
    words = line.split()
    word_count += len(words)
    character_count += len(line)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {character_count}")

  

if __name__ == '__main__':
  main()
