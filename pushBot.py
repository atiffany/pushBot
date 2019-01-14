from slackclient import SlackClient
import time

class slackCommunication(object):
    def __init__(self):
        self.slack_client = SlackClient("xoxb-513177741924-513252573923-nHARsKDPzRK0O4MfRapVKS3O")
        self.appName = "pushbot"

    def slackConnect(self):
        return self.slack_client.rtm_connect()

    def slackReadRTM(self):
        return self.slack_client.rtm_read()

    def parseInput(self, input, botID):
        bot_at_id = "<@"+botID+">"
        if input != [] and 'text' in input[0]:
            print(input)
            user = input[0]['user']
            message = input[0]['text']
            channel = input[0]['channel']
            return [str(user), str(message), str(channel)]
        else:
            print("Not this\n")
            print(input)
            return [None, None, None]

    def getBotID(self, botName):
        api_call = self.slack_client.api_call("users.list")
        users = api_call["members"]
        for user in users:
            if 'name' in user and botName in user.get('name') and not user.get('deleted'):
                return user.get('id')

    def writeToSlack(self, channel, message):
        return self.slack_client.api_call("chat.postMessage", channel = channel, text = message, as_user = True)

class mainFunction(slackCommunication):
    def __init__(self):
        super(mainFunction, self).__init__()

    def determineIfResponseIsNeeded(self, input):
        if input:
            user, message, channel = input
            return self.writeToSlack(channel, message)

    def run(self):
        self.slackConnect()
        BOT_ID = self.getBotID(self.appName)
        while True:
            self.determineIfResponseIsNeeded(self.parseInput(self.slackReadRTM(), BOT_ID))
            time.sleep(1)

if __name__ == "__main__":
    instance = mainFunction()
    instance.run()

"""
This script keeps track of users who are pushing and who is in the queue to push next.
It will remind users who are pushing if they are taking longer than usual to do so.
It will alert users who are next in the queue when it is their turn to push.
"""
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

    """
