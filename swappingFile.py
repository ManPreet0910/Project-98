def swapFileData():
    file_name1=input("Which files data do you want to be copied?")
    file_name2=input("Which file do you want the data to be transfered to?")

    with open(file_name1, 'r') as a:
        data_a = a.read
    with open(file_name2, 'r') as b:
        data_b = b.read

    with open(file_name1) as a:
        a.write(data_b)
    with open(file_name2) as b:
        b.write(data_a)

swapFileData()