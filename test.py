def WordSplit(strArr):
    arr1=[]
    arr2=[]
    result=[]
    var1=strArr[0]
    var2=strArr[1].split(',')
    for count1 in range(len(var2)):
        aux=var1.split(var2[count1]) #aux get array's value and format from string "hellocat"
        if len(aux)==2: #verify if aux contains two objects inside
            add=aux[0]+aux[1] #"add" variable get aux value
            arr1.append(add) 
    for i in range(len(arr1)):
        if var2.count(arr1[i])!=0: #verify how many times words exist in array
            arr2.append(arr1[i]) #write in "arr2" variable if exist in "var2" 
        else:
            result='not possible' #if it is not exist words in array throws a message
    if arr2: #use "arr2" variable to verify if words exist to continue
        result.append(arr1[0])
        result.append(arr1[1])

    return result

print(WordSplit(["hellocat","apple,bat,cat,goodbye,hello,yellow,why"]))
