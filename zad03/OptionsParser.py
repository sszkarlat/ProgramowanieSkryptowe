from MoveDirection import MoveDirection


class OptionsParser:
    @staticmethod
    def options_parser(stringList):
        resultList = []
        for string in stringList:
            if string == "f":
                resultList.append(MoveDirection["FORWARD"].value)
            elif string == "b":
                resultList.append(MoveDirection["BACKWARD"].value)
            elif string == "l":
                resultList.append(MoveDirection["LEFT"].value)
            elif string == "r":
                resultList.append(MoveDirection["RIGHT"].value)

        return resultList
