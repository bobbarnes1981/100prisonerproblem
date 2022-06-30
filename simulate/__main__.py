import random

num_prisoners = 100
limit = 50

def pick_numbers_for_prisoner(boxes, prisoner_num, limit):
    current_num = prisoner_num
    count = 0
    while count < limit:
        next_num = boxes[current_num]
        if next_num == prisoner_num:
            return True
        current_num = next_num
        count += 1
    return False

def process_prisoners(boxes, num_pisoners, limit):
    for prisoner_num in range(0, num_pisoners):
        if pick_numbers_for_prisoner(boxes, prisoner_num, limit) == False:
            return False
    return True

def get_boxes():
    boxes = []
    for box_num in range(0, num_prisoners):
        boxes.append(box_num)
    random.shuffle(boxes)
    return boxes

total_simulations = 10000
success = 0

for i in range(0, total_simulations):
    boxes = get_boxes()
    if process_prisoners(boxes, num_prisoners, limit) == True:
        success += 1

print('total simulations: ', total_simulations)
print('successes: ', success)
print('chance of success: ', success / total_simulations)
