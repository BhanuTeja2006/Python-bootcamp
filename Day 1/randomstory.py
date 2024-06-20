import random

while True :
    when = ('Few years ago','Yesterday','Today')
    where = ('at wankhede','at Lords','at Eden Gardens')
    who = ('Ms Dhoni','Sachin Tendulkar','VVS Laxman')
    what = ('scored 91 in world cup final','scored 228 runs in test match','scored 125 runs')
    print(random.choice(when),random.choice(where),random.choice(who),random.choice(what))
    opt = input('Do you want another story (y/n) : ')
    if opt == 'n' :
        break
print('Thank you !')