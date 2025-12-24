print ("Enter 6 test score:")
Scores = []

for i in range(6) :
   
   num = int(input(f"Enter score {i+1}: "))
   Scores.append(num)

print("\n You entered:", Scores)
print("The highest score is:" , max(Scores))
print("The lowest score is:" , min(Scores))
print("The total of all scores is:" , sum(Scores))
average = sum(Scores)/len(Scores)
print("The average score is:" , average)

if average < 35 :
       print("Grade F ; 😒 You failed")
elif average < 50 :
         print("Grade D ; 😐 You can do better!")
elif average < 70 :
      print("Grade C ; 🙂 Good Job, Hope you do better next time")
elif average < 90 :
      print("Grade B ; ☺️ Great Work.")
else :
      print("Grade A ; 🤩 Excellent Work,Keep it up!")