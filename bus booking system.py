import re
class Bus:
    s,r,required,g,p={},{},{},{},{}
    f,f1,store,name_gen=[],[],[],[]
    start,tim1,mon,proof,name,y,k,v,s_gender='','','','','','','','',''
    time,time1=0,0
    def __init__(self,a):
        self.a=a
    def book(self):
        n = int(input('How many  number of seat which you want to book  '))

        for i in range(1, n + 1):
            while True:

                print('********************************')
                self.name = input('enter the name of the person : ')
                self.a = int(input('enter the seat number  :  '))
                age = int(input('enter the age of the person'))
                o.gender()
                o.Id_proof()
                print('********************************')
                if self.a > 50:
                    print('please enter the seat number with in 1-50')
                else:
                    self.s[self.a] = self.name
                    self.r[self.a] = age
                    self.g[self.a]= self.s_gender
                    self.p[self.a] = self.proof[-2::1]
                    break
        print('_______________________________')
        print('The data is added successfully')

        print('______to remove a seat ____')
        print('********************************')
        q = input('Say (yes/no) to remove any seat ')
        if q == 'yes':
            print('********************************')
            while True:
                print(f'The  names and the seat number {self.s} ')

                v = int(input('How many number of seat want to remove '))
                print('********************************')
                if len(self.s)<=v:
                    print("Don't exceed the number")
                else:
                    for i in range(0, v):
                                while True:
                                    print(f'The  names and the seat number {self.s} ')
                                    print('________________________________')

                                    w = int(input('enter the seat number to remove '))

                                    if w not in (self.s):
                                        print('________________________________')

                                        print('The seat number is not present ,which is you are trying to remove ')
                                        print('________________________________')

                                    else:
                                        self.s.pop(w)
                                        self.r.pop(w)
                                        break

                    print('_______________________________')
                    print('The data is removed successfully')
                    break
    def gender(self):
        while True:
            self.s_gender = input('enter the gender (male/female/other) : ').lower()
            if (self.s_gender=='male') or (self.s_gender=='female') or (self.s_gender=='other'):
                break
            else:
                print('please fill correctly (male/female/other)')


    def details(self):
        print('THE BUS WITH 50 SEATS ONLY ')
        print('*********\n'
              'The seat no 1,4,7,10,13,16,19,24,27,30,33,36,39,42 are window seat\n'
              'The seat no 3,6,9,12,15,18,21,22,25,28,31,34,37,40 are corner seat\n'
              'the seat no from 43 to 50 are back seat')
        print('*****************************************')
        print('*******************\n'
              'For the payment \n'
              '****** If age is less than or equal to 10 then the cost of seat is 100/person \n'
              '****** If age is greater than 10 then the cost of seat is 200/person \n'
              )

    def Id_proof(self):
        while True:
            self.proof = (input('enter the id_proof(Aadhar card) '))
            self.out = re.findall('[0-9]{12}', self.proof)
            print('********************************')
            if self.proof.isdigit() and self.out:
                print('Id proof is valid')
                break
            else:
                print('please enter exactly 12 digit')

    def Id(self):
        for i,j in zip(self.s,self.p.values()):
            print(f'The seat number and Id_proof of the person {i} XXXXXXXXXX{j}')

    def res(self):
        if  not (self.s or self.f or  self.g):
            print('Fill the complete details ,which is in option 2 ')

        else:

            print('________________________________')

            print(f'The names and the  ages of the people are ***********************')
            o.name_age()
            print('________________________________')

            o.name_seat()
            print('________________________________')
            print(f'The names and the  gender of the people are ***********************')
            o.name_gender()
            # print(f'The names and there gender {self.name_gen}')
            print('________________________________')
    def name_age(self):
        self.f = list(self.s.values())
        self.f1 = list(self.r.values())
        self.store1 = list(zip(self.f, self.f1))
        for i in self.store1:
            # self.store += i
            print(f'{i}')



    def name_seat(self):
        for i,j in self.s.items():
            print(f'The {j} is booked with the seat number {i}')

    def name_gender(self):
        self.f = list(self.s.values())
        self.f1 = list(self.g.values())
        self.store1 = list(zip(self.f, self.f1))
        for k in self.store1:
            # self.name_gen += i
            print(f'{k}')




    def bal(self):
        print('________________________________')
        o.res()
        print('________________________________')
        o.seat()
        print('________________________________')

        if not (self.start) or not (self.time or self.time1 or self.tim1):
            print('Fill the complete details ,which is in option 4 ')
        else:
            print('________________________________')
            if self.start <= '0':
                print('Please enter the valid date')
            elif self.start == '1':
                print(f'The Journey Date start from {self.start}st {self.mon}')
            elif self.start == '2':
                print(f'The Journey Date start from {self.start}nd {self.mon} ')
            elif self.start == '3':
                print(f'The Journey Date start from {self.start}rd {self.mon} ')
            else:
                print(f'The Journey Date start from {self.start}th {self.mon}  ')


            print('________________________________')
            print('The timing is ', self.time, ':', self.time1, self.tim1)
            print('________________________________')

    def seat(self):
        self.w = {1, 4, 7, 10, 13, 16, 19, 24, 27, 30, 33, 36, 39, 42}
        self.c = {3, 6, 9, 12, 15, 18, 21, 22, 25, 28, 31, 34, 37, 40}
        self.b = {43, 44, 45, 46, 47, 48, 49, 50}
        self.required = set(self.s)
        for i in self.required:
            if i in self.w:
                print(f'The seat number {i} is window seat')
            elif i in self.c:
                print(f'The seat number {i} is corner seat')
            elif i in self.b:
                print(f'The seat number {i} is back seat')
            else:
                print(f'The seat number {i} is middle seat')

    def available(self):
        total_seat={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50}
        self.required = set(self.s)
        result=total_seat-self.required
        if not self.required:
            print('Fill the complete details ,which is in option 2 ')
        else:
            print(f'The seats which you booked {self.required}')
        o.seat()
        print(f'The available seats are {result}')
    def payment(self):
        c=list(self.r.values())
        c1,c2=0,0
        for i in c:
            if i<=10:
                c1+=1
            elif i>=11:
                c2+=1
        cost=(c1*100)+(c2*200)


        if cost==0:
            print('Fill the complete details ,which is in option 2 ')
            bus()
        else:
            print(f'The total cost is {cost}')
            print('If once payment is done you will exit from the menu')
            while True:
                total_cost = int(input('enter the total cost : '))
                if cost == total_cost:
                    print(f'The payment with the Rs.{cost} is done ')
                    print('Thank you for the payment Your are existing from the menu')
                    print('HAPPY JOURNEY')
                    exit()
                else:
                    print('please enter the correct amount')

    def cancel(self):
        print(' You have cancelled the seat and your existing from the menu')
        exit()
    def month(self):

        while True:
            self.mon = input('Enter the month : ').upper()
            self.month = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER',
                          'OCTOBER',
                          'NOVEMBER', 'DECEMBER']
            if  self.mon.isalpha() and self.mon  in self.month:

                break
            else:
                print('please enter the correct month in alphabets')
    def dates(self):
        self.start = input('Enter the Start Date : ')
        o.month()
        print('The Start date and month as been updated successfully')

    def datetim(self):
        o.dates()

        self.time=int(input('The timing in Hour :'))
        while True:
            self.time1 = int(input('The timing in min :'))
            if self.time1<60 and self.time1>=00:
                break
            else:
                print('enter the min less than 60 ')



        if self.time<12:
            self.tim1='AM'
        else:
            self.tim1='PM'
        print('The Timing as updated succesfully')

def bus():
    while True:
        print('********************************')
        b = input('do want to go back main menu(y/n) for the process : ')
        if b == 'y':
            q = input('******* choose the number 1.to get the details of seat \n'
                      '                         2.To book the seat or remove the seat\n'
                      '                         3.To  Add the seat  \n'
                      '                         4.To set Date and Timing \n'
                      '                         5.Check the available seat \n'
                      '                         6.Check the complete details before proceeding the payment \n'
                      '                         7.To do the payment \n'
                      '                         8.To cancel the seat \n'
                      '                         9.To exit \n'


                      )
            if q=='1':
                o.details()
            elif q == '2':
                o.book()
            elif q == '3':
                o.book()
            elif q=='4':
                o.datetim()
            elif q=='5':
                o.available()
            elif q=='6':
                o.bal()
            elif q=='7':
                o.payment()
            elif q=='8':
                o.cancel()
            elif q == '9':
                exit()
            else:
                print('Please enter valid input')
        elif b=='n':
            print('thankyou ')
            exit()

        else:
            print('please enter (y/n) y->To go to menu for the process ,n->To exit from the menu ')

print('welcome to bus booking center ')
print('********************************')
a=input('Are you willing to book the bus say (yes or no) '
                  'The number of seat are 50 : ').lower()
o=Bus(a)
if a == 'yes':
    print('welcome  ')
    print('********************************')
    bus()
elif a == 'no':
    print('thank you for visiting')

else:
    print('please enter (yes/no) ')


