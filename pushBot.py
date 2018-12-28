"""
This script keeps track of users who are pushing and who is in the queue to push next.
It will remind users who are pushing if they are taking longer than usual to do so.
It will alert users who are next in the queue when it is their turn to push.
"""

alertFlag = False
queue = []

attempts = 0
while attempts < 4:
    name = raw_input("Who ya?\n>>")
    input = raw_input("What are you doing?\n>>")
    if "push" in input:
        if alertFlag == True:
            queue.append(name)
            print("Someone is already pushing. I'll add you to the queue, lil homey")
        alertFlag = True
        print("Push it!")
    elif "next" in input or "q" in input:
        if alertFlag != True:
            print("You can go ahead and print")
        else:
            queue.append(name)
            print("You're in the queue, fam")
    elif "done" in input:
        print("Thanks for letting us know, chief")
        if queue.count > 0:
            next = queue.pop(0)
            print("Hey @" + next + ", you're up. Time to fix merge conflicts and push!")
    else:
        print("What was that?")
    attempts += 1
