from main.ds.stack.Stack import Stack

diction = {"[": "]", "{": "}", "(": ")", "<": ">"}

openingChars = list(diction.keys())
closingChars = list(diction.values())


class DelimiterMatch:

    def __init__(self, userInput):
        self.userInput = userInput

    def isValid(self):
        userInput = self.userInput
        stack = Stack(len(userInput))

        for i in range(len(userInput)):

            char = userInput[i]

            if self.isOpening(char):
                stack.push(char)
            elif self.isClosing(char):
                if stack.isEmpty():
                    return False
                else:
                    openingChar = stack.pop()
                    if not self.isProperlyMatch(openingChar, char):
                        return False

        return stack.isEmpty()

    def getClosingChar(self, openChar):
        return diction[openChar]

    def isOpening(self, char):
        return char in openingChars

    def isClosing(self, char):
        return char in closingChars

    def isProperlyMatch(self, openChar, closingChar):
        closing = self.getClosingChar(openChar)
        return closing == closingChar
