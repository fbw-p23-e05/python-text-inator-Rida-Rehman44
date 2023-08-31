string = input("Enter any word: ")
if (string[-1:]== 'a'or string[-1:]== 'e'or string[-1:]== 'i'or  string[-1:]== 'o'or string[-1:]== 'u'):
    print(string + "-inator " +str(len(string))+ "000")
else :
    print(string + "inator " +str(len(string))+ "000")    