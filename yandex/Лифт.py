opportunity = int(input())
floors = int(input())
people_list = []
while True:
    people = int(input())
    floors -=1
    people_list.append(people)
    if floors <= 0:
        break
ans = 0
"""while sum(people_list) > 0:
    count_of_floors = 0
    for i in range(len(people_list)):
        print(people_list)
        count_of_people = 0
        while count_of_people < opportunity:
            if people_list[i] <= opportunity:
                count_of_people += people_list[i]
                people_list[i] = 0
                count_of_floors += i+1
            else:
                print('e')
                count_of_people += opportunity
                people_list[i] -= opportunity
                count_of_floors += (i+1)*2

    ans += count_of_floors
print(ans)"""

count_of_floors = 0
while sum(people_list) > 0:
    count_of_people = 0
    for i in range(len(people_list)):
        if people_list[i] <= opportunity:
            count_of_people += people_list[i]
            people_list[i] = 0
            count_of_floors += i+1
            print(count_of_floors)
        else:
            count_of_people += opportunity
            people_list[i] -= opportunity
            count_of_floors += (i+1) * 2
    ans += count_of_floors
print(ans)