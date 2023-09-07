
import os , sys , time , json , datetime
class CLS(): # clear Console
    def __init__(self):
        os.system("clear") and os.system("cls")
class sp(): # slow print
    def __init__(self , text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
CLS()

Now = str(datetime.datetime.now())
#dbjson = {}

class Database():
    def __init__(self):
        self.dbjson = {}  # تعریف متغیر dbjson به عنوان یک متغیر عضو

    def start(self):
        try:
            with open("XNPDB.json", 'r') as DbFile:
                pass
                #DB = json.load(DbFile)
                #self.dbjson = DB  # به dbjson اطلاعات از فایل می‌خوانیم
        except FileNotFoundError:
            # در صورتی که فایل وجود نداشته باشد، متغیر dbjson خالی می‌ماند
            pass
    def idkdb(self):
        with open("XNPDB.json" , 'r') as DbFile:
            DB = json.load(DbFile)
            print(DB)
    def newinfo(self):
        with open("XNPDB.json", 'w') as DbFile:
            json.dump(self.dbjson, DbFile, indent=4)  # ذخیره dbjson در فایل

db = Database()  # ایجاد یک نمونه از کلاس Database
db.start()  # شروع دیتابیس
        

class delete():
    def __init__(self , Path , sure):
        if sure == True:
            try:
                del db.dbjson[Path]
                sp("Fille remove successfully! \n")
            except:
                sp("File not found!\n")


class search():
    def __init__(self , idt = False , id=000 , FileName="HELL"):
        if idt == True:
            CLS()
            try:
                print(db.dbjson[id])
                global editthis
                editthis = input("\n \nWant to edit this? y/n").upper()
                if editthis == "YES" or editthis =="Y":
                    Add(FileName)
                else:
                    pass
            except:
                sp("File not found!\n")
        if idt == False:
            CLS()
            try:
                print(db.dbjson[FileName])
            except:
                sp("File not found!\n")
class create():
    def __init__ (self , FileName , Content , id , data = Now):
        db.dbjson[FileName] = [Content , id , data]
        Database().newinfo
        sp("File created successfully! \n")
        print(db.dbjson)

class Add():
    def __init__ (self,FileName):
        mn = db.dbjson[FileName]
        print(f"Current content : {mn[1]}")
        ec = input("What should i add? : ")
        cd = mn[1]
        cd += ' ' + ec
        mn[1] = cd
        sp("Done! \n")
#Database.start()
sp("Hello dear! for help , enter Help! \n")
while (True):
    MainInput = input("-> Enter S/C/D/E/L/A/ : ").upper()
    #=("-> e/s/c/d/h : ").upper()
    if MainInput =="C" or MainInput =="CREATE":
        cfnme = input("Enter the file name : ")
        cid = input("Enter the file id : ")
        ccon = input("Enter content : ")
        create(cfnme,ccon,cid)
    elif MainInput== "S" or MainInput=="SEARCH":
        ids = input("Do you want to search by ID ? y/n : ").upper()
        if ids=="YES" or ids=="Y":
            idsin = input("Enter file id : ")
            search(True,ids)
        else:
            fnme = input("Enter file name : ")
            search(False,000,fnme)
    elif MainInput=="D" or MainInput=="DELETE" or MainInput=="REMOVE" or MainInput=="R":
        patf = input("Enter file name : ")
        sure_ = input("Are your sure? True/False : ")
        if sure_ =="True":
            sure_ = True
            delete(patf,sure_)
    elif MainInput=="HELP" or MainInput=="H":
        CLS()
        sp("Hello dear! \n Enter S for search in the files\n Enter D for  delete the files \n Enter A for edit files \n Enter C for create file \n Enter E for exit \n Enter L for view list of files \n")
    elif MainInput=="EXIT" or MainInput=="E":
        exit()
    elif MainInput=="L" or MainInput=="LIST":
        print(db.dbjson)
    elif MainInput=="CLS" or MainInput=="CLEAR":
        CLS()
    else:
        print("Not now!")