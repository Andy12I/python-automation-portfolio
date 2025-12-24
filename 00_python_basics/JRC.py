# The QA Bug Logger
while True :
 user_report = input("Describe the bug (or type 'exit'): ")
 # 1.Check for exit First
 if user_report == 'exit':
    break #stop the loop immidiately
  #2. If we didn't break, Then save the data
 with open("bug_report.txt", "a") as file:
    file.write(user_report + "\n") # Added \n to move to the next line

 print("Bug saved.")