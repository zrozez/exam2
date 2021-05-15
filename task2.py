txt = 'Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless. But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.'

txt1 = txt.lower()

def count(letter, tt):
    count_of_letter = 0
    for i in tt:
        if i==letter:
            count_of_letter +=1
    print(f'Количество буквы {letter} в тексте - {count_of_letter}') 

count('s', txt1)
count('t', txt1)

lst_of_txt = txt1.split()

for i in lst_of_txt:
    if i.startswith('advert'):
        word = i.upper()
        print(word)