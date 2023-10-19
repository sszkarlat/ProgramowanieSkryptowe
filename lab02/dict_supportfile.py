import re


def regex_function(inputData):
    Regex = re.compile(r"\w*[^\s:\(\)]")
    return Regex.findall(inputData)


def user_dictionary(inputData, dictionaries):
    for data in inputData:
        dataList = regex_function(data)
        user_name = dataList[0]

        # Sprawdź, czy użytkownik już istnieje w słownikach
        user_exists = False
        for dictionary in dictionaries:
            if dictionary["user"] == user_name:
                user_exists = True
                break

        if not user_exists:
            newDictionary = {"user": user_name}
            for i in range(1, len(dataList), 2):
                newDictionary[dataList[i]] = int(dataList[i + 1])
            dictionaries.append(newDictionary)
        else:
            for dictionary in dictionaries:
                if dictionary["user"] == user_name:
                    for i in range(1, len(dataList), 2):
                        if dataList[i] in dictionary:
                            dictionary[dataList[i]] += int(dataList[i + 1])
                        else:
                            dictionary[dataList[i]] = int(dataList[i + 1])


inputData = "sell Jan_Kowalski:Komputer(1):Laptop(5) Anna_Nowak:Komputer(2)"
dictionaries = []
user_data = inputData.split(" ")[1:]
print(user_data)
user_dictionary(user_data, dictionaries)
print(dictionaries)
user_dictionary(user_data, dictionaries)
print(dictionaries)
