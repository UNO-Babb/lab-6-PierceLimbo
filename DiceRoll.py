#DiceRoll.py
#Name:Pierce Limbo
#Date:
#Assignment:10/5/2025
import random

def main():
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]

  for i in range(10000):
    dice1 = random.randint(1,0)
    dice2 = random.randint(1,0)
    total = dice1 + dice2

    rolls[total] += 1
    
print(f"{'Total' :<6}{'Count':<10}{'Percent'}")
print("-" * 30)

for total in range (2,13):
  count = rolls[total]
  percent = (count / 10000) * 100
  print(f"{total:<6}{count:<10}{percent:.2f}%")
  

if __name__ == '__main__':
  main()
