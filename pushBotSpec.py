import pytest

@pytest.fixture
def slackCommunication():
    from pushBot import slackCommunication
    return slackCommunication()

def test_slackConnect(slackCommunication):
    assert slackCommunication.slackConnect() == True

def test_parseInput_normal(slackCommunication):
    pushBotID = "UF37EGVT5"
    input =[{u'client_msg_id': u'c8acc1d1-e177-4376-920c-39750cbcdc5b', u'event_ts': u'1546291016.002100', u'text': u'<@UF37EGVT5> hello there', u'ts': u'1546291016.002100', u'user': u'UF357MU5A', u'team': u'TF357MTT6', u'type': u'message', u'channel': u'DF4NB3F2A'}]
    assert slackCommunication.parseInput(input, pushBotID) == ["UF357MU5A", "<@UF37EGVT5> hello there", "DF4NB3F2A"]

def test_parseInput_invalid(slackCommunication):
    pushBotID = "UF37EGVT5"
    input =[{u'type': u'hello'}]
    assert slackCommunication.parseInput(input, pushBotID) == [None, None, None]

def test_parseInput_empty(slackCommunication):
    pushBotID = "UF37EGVT5"
    input =[]
    assert slackCommunication.parseInput(input, pushBotID) == [None, None, None]

def test_getBotID(slackCommunication):
    assert slackCommunication.getBotID("pushbot") == "UF37EGVT5"

#@pytest.mark.skip(reason="dont need to test rn")
def test_writeToSlack(slackCommunication):
    channel = "DF4NB3F2A"
    message = "pushBot\'s ability to write to Slack for testing reasons 2.0"
    assert slackCommunication.writeToSlack(channel, message)["ok"] == True

@pytest.mark.skip(reason="not yet implemented fully")
def test_slackReadRTM(slackCommunication):
    slackCommunication.slackConnect()
    print(slackCommunication.slackReadRTM())

##### MAIN FUNCTION TESTS #####

@pytest.fixture
def mainFunction():
    from pushBot import mainFunction
    return mainFunction()

def test_determineIfResponseIsNeeded(mainFunction):
    user = "UF357MU5A"
    message = "message received from user"
    channel = "DF4NB3F2A"
    input = [user, message, channel]
    assert mainFunction.determineIfResponseIsNeeded(input)
