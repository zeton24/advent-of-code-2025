import re

# with open('data/test-day2.txt', 'r') as f:
with open('data/day2-input.txt', 'r') as f:
    ranges = f.read().split(',')

invalid_ids = []
ranges = [i for i in ranges if len(i.split('-')) == 2]
for r in ranges:
    ids = list(range(int(r.split('-')[0]), int(r.split('-')[1])+1))
    for i in ids:
        i = str(i)

        # part 1
        if i[0:len(i)//2] == i[len(i)//2:]:
            invalid_ids.append(int(i))
            continue

        # part 2
        # matched = re.search(r'(\d+)\1+', i) ## to z jakiegos powodu nie łapie 2121212121 (5x21)
        matched = re.search(r'(\d+)\1{2,}', i)
        if matched and len(matched.group(0)) == len(i):
            invalid_ids.append(int(i))
        else:
            matched = re.search(r'(\d+)\1{5,}', i)
            if matched and len(matched.group(0)) == len(i):
                invalid_ids.append(int(i))



## answer
answer = sum(invalid_ids)
# print(invalid_ids)
test_answer = 4174379265
print("answer: ", answer) #, "won?:", answer==test_answer, test_answer-answer)

# 11323661261