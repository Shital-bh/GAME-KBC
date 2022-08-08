print('Hello')
print( )
name=input("Enter the Name:- ")
print( )
print(name, 'Welcome to KBC')
print( )
print('Rules=1. You have 13 questions each question have 4 choice and 2 lifefine.2. You have 2 stages at 10,000 and 3,20,000, where you quite the game and win the total prize. 3. lifeline can be used only once. 4. User can quite from game anytime. 5. The total wining price will be displayed after every question. 6. If the user has selected an incorrect aption. The amount will be given according to stage cleared. 7. you can only answer in capital letters. like A,B,C,D. ')
print( )
KBC=[{'Question': 'qus1:-Accoding to a popular saying what does not grow on tree?',
'option':['A. Money','B. fruits','C. leaves','D.flower'],
'Answer': 'A',
'50-50':['A. Money', 'B. fruits'],
'expert':'everyone need it ',
'amount':'you win ₹ 5000'},
{
'Question': 'qus2:-The international literacy day is observed on ?',
'option':['A. 28th November', 'B. 2nd May', 'C. 8th september ', 'D. 22nd september'],
'Answer': 'C',
'50-50':['A. 28th November', 'C. 8th september'],
'expert':'it is the month of teachers',
'amount':'you win ₹10,000'},
{
'Question': 'qus3:-Which of these rivers does not flow from east to west?',
'option': ['A. Tapti', 'B. Ganga',' C. Chambal', 'D. Narmada'],
'Anwser': 'C',
'50-50':['B.Ganga','Chambal'],
'expert':'its name based on some place',
'amount':'you win ₹ 20,000'},
{
'Question':'qus4:-Clod brew,latte, espresso are all example of which beverage?',
'option': ['A. Tea', 'B. fruit juice', 'C. Coffee', 'D. Lassi'],
'Answer': 'C',
'50-50':['D. lassi', 'C. Coffee'],
'expert':'it is very expensive drink ',
'amount':'you win ₹ 40,000'},
{
'Question':'qus5:- Which of these is a non-renewable sourse of energy?',
'option': ['A. Solar power','B. Wind power','C. Hydro power','D. Natural gas'],
'Answer': 'D',
'50-50':['A. Solar power','D. Natural gas'],
'expert':'it is connect with our enviroment',
'amount':'you win ₹ 80,000'},
{
'Question':'qus6:-Which is the single largest internal organ by mass in the human body?',
'option': ['A. liver', 'B. Gall bladder', 'C. kidney','D. Stomach'],
'Answer': 'A',
'50-50':['A. liver','C. kidney'],
'expert':'it is only one part in our body ',
'amount':'you win ₹ 1,60,000'},
{
'Question':'qus7:-Which of the following corresponds to ek bataa do?',
'option': ['A. Pura', 'B. Sawa', 'C. Adha', 'D. parna'],
'Answer': 'C',
'50-50':['A. Pura','C. Adha'],
'expert':'half ',
'amount':'you win ₹ 3,20,000'},
{
'Question': 'qus8:-Which of the following gods in also known as Gauri Nandan?',
'option': ['A. Agni', 'B. Indra', 'C. Hanuman', 'D. Ganesha'],
'Answer': 'D',
'50-50':['A. Agni','D. Ganesha'],
'expert':'everyone knowns as vinayaka ',
'amount':'you win ₹ 6, 40,000'},
{
'Question': 'qus9:-Which of these sports requires you to shout out a word loudly during play?',
'option': ['A. Ludo', 'B. Kho-kho', 'C. Playing cards', 'D. Chess'],
'Anwser': 'B',
'50-50':['A. ludo', 'B. Kho-kho'],
'expert':'it is a game play in the ground',
'amount':'you win ₹12,50,000'},
{
'Question': 'qus10: Which of these spices is the smallest in size?',
'option': ['A. Ajwain', 'B. Jeera', 'C. Saunf', 'D. Meethi seeds'],
'Answer': 'A',
'50-50':['A. Ajwain', 'C.Saunf'],
'expert':'spicy in taste',
'amount':'you win ₹ 25,00,000'},
{
'Question': 'qus11:-Where was the BRICS summit held in 2014?',
'option': ['A. Brazil', 'B. India', 'C. Russia', 'D. China'],
'Answer': 'A',
'50-50':['A. Brazil', 'C. Russia'],
'expert':'it connected with song ',
'amount':'you win ₹ 50,00,000'},
{
'Question': 'qus12:-What is gulab jamun of type of ?',
'option': ['A. A flower', 'B. A fruit', 'C. A tree', 'D. A sweet'],
'Answer': 'D',
'50-50':['C. A tree','D. A sweet'],
'expert':'meetha',
'amount':'you win ₹1 crore'},
{
'Question':'qus13:-Which of these is shorter than 1 inch?',
'option':['A. 2cm',' B. 3cm',' C. 4cm', 'D. 5cm'],
'Answer':' A',
'50-50':['A. 2cm', 'C. 4cm'],
'expert':'....',
'amount':'you win ₹ 2 crore'}]
# used of for loop for print the questtion and option.
#We used count variable for store value
#x is used for print dictionary kyes and value
count=0
for x in KBC:
 print(x['Question'])
 for y in (x['option']):
  print(y)
  #if you want lifeline press 4 . if you don't want then directly put answer
  # if you want quit the game them press 5.
 print('If you want lifeline press(4)')
 print('If you want quit the game press(5)')
 ans=input('Enter the answer: ' )
 sure=input('Are you sure (say yes) : ')
 #you want locked the answer and you sure then say yes
 if sure=='yes':
    print('your answer is locked ')
 #else:
   #print("enter the correct answer ")
 if ans==(x['Answer']):
    print('Congratulation!!!')
    print(x['amount'])
    print( )
 if ans=='5':
   print('Thank you for coming for the game kbc')
   print(x['amount'])
   break
   #choose your lifeline
 if ans=='4':
   print('Choose your lifeline')
   print('1.50-50 Lifeline')
   print('2.expert')
   ans1=input('choose a lifeline from given options: ')
   #count for lifeline if you all used  life then they give only 2 times after its quit the game
   if count==2:
     print("you have used all the lifelines:")

   elif ans1=='1':
      print(x['50-50'])
      count=count+1
   elif ans1=='2':
      print(x['expert'])
      count=count+1
   ans1=input('choose a answer : ')
   if ans1==x['Answer']:
       print('congratulation')
       print(x['amount'])
   else:
      print(' sorry !!! You are wrong')
      print('correct answer is',x["Answer"])
      break