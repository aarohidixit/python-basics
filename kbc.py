print("            Welcome to KAUN BANEGA CROREPATI")
questions=['1. National bird of India? A. Crow, B.sparrow C.Peacoak D.pigeon',
           "2. Capital of India? A. Mumbai, B. New Delhi, C. Kolkata, D. Chennai",
           "3. Which planet is known as the Red Planet? A Earth, B. Venus, C. Mars, D. Jupiter",
           "4. Which animal is known as the Ship of the Desert? A. Horse, B. Camel, C. Elephant, D. Donkey",
           "5. Which is the largest ocean in the world? A. Indian Ocean, B. Atlantic Ocean, C. Arctic Ocean, D. Pacific Ocean",
           "6. What is the national flower of India? A. Rose, B. Lotus, C. Sunflower, D. Lily",
           "7. How many continents are there in the world? A. 5, B. 6, C. 7, D. 8",
           "8. Which gas do plants absorb from the atmosphere? A. Oxygen, B. Nitrogen, C. Carbon dioxide, D. Hydrogen",
           "9. Who wrote the Indian national anthem? A. Bankim Chandra Chatterjee, B. Rabindranath Tagore, C. Sarojini Naidu, D. Subramania Bharati",
           "10. How many days are there in a leap year? A. 365, B. 366, C. 364, D. 367"
           ]
answers = ["C", "B", "C", "B", "D", "B", "C", "C", "B", "B"]
c=0
money = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]
for i in range(len(questions)):
    print(questions[i])
    a=input('Enter A/B/C/D :')
    if a==answers[i]:
        c=c+money[i]
        print('Current Point range:',c)
        print('HURRAYYY !!! RIGHT ANSWER')
    else:
        print('OPPPS!! Wrong Answer')
        break
print("Congratulations on winning",c,"POINTS")

# for i in range(len(money)):
#     print('Amount on',i+1,'is',money[i])
    