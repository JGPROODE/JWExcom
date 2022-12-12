#x=9
try:
    print("het getal is : "+str(x/0))
except NameError as err:
    print("NameError opgetreden !",err)
except TypeError as err:
    print("TypeError foutopgetreden !")
except ZeroDivisionError:
    print("Zerodiverror foutopgetreden !")
except:
    print("onbekende foutopgetreden !")

