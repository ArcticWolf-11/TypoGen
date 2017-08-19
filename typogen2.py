#Takes a password, spits out possible typos
#It does not take into account possible "Shift"errors or CapLock disasters

password = raw_input("Enter password: ")
print password

list0 = "9op[-"
list9 = "8iop0"
list8 = "7uio9"
list7 = "6yui8"
list6 = "5tyu7"
list5 = "4rty6"
list4 = "3ert5"
list3 = "2wer4"
list2 = "1qwe3"
list1 = "`qw2"
lista = "qwsxz"
listb = "fghn v"
listc = "sdfv x"
listd = "werfvcxs"
liste = "234rfdsw"
listf = "ertgbvcd"
listg = "rtyhnbvf"
listh = "tyujmnbg"
listi = "789olkju"
listj = "yuik,mnh"
listk = "uiol.,mj"
listl = "iop;/.,k"
listm = "hjk, n"
listn = "ghjm b"
listo = "890p;lki"
listp = "90-[';lo"
listq = "`12wsa"
listr = "345tgfde"
lists = "qwedcxza"
listt = "456yhgfr"
listu = "678ikjhy"
listv = "dfgb c"
listw = "123edsaq"
listx = "asdc z"
listy = "567ujhgt"
listz = "asx "

list00 = "(OP{_"
list99 = "*IOP)"
list88 = "&UIO("
list77 = "^YUI*"
list66 = "%TYU&"
list55 = "$RTY^"
list44 = "#ERT%"
list33 = "@WER$"
list22 = "!QWE#"
list11 = "~QW@"
listA = "QWSXZ"
listB = "VFGHN "
listC = "XSDFV "
listD = "WERFVCXS"
listE = "@#$RFDSW"
listF = "ERTGBVCD"
listG = "RTYHNBVF"
listH = "TYUJMNBG"
listI = "&*(OLKJU"
listJ = "YUIK<MNH"
listK = "UIOL><MJ"
listL = "IOP:?><K"
listM = "HJK< N"
listN = "BGHJM "
listO = "*()P:LKI"
listP = "()_{"":LO"
listQ = "~!@WSA"
listR = "#$%TGFDE"
listS = "QWEDCXZA"
listT = "$%^YHGFR"
listU = "^&*IKJHY"
listV = "DFGB C"
listW = "!@#EDSAQ"
listX = "ASDC Z"
listY = "%^&UJHGT"
listZ = "ASX "

my_dict = {'0': list0,
           '9': list9,
           '8': list8,
           '7': list7,
           '6': list6,
           '5': list5,
           '4': list4,
           '3': list3,
           '2': list2,
           '1': list1,
           'a': lista,
           'b': listb,
           'c': listc,
           'd': listd,
           'e': liste,
           'f': listf,
           'g': listg,
           'h': listh,
           'i': listi,
           'j': listj,
           'k': listk,
           'l': listl,
           'm': listm,
           'n': listn,
           'o': listo,
           'p': listp,
           'q': listq,
           'r': listr,
           's': lists,
           't': listt,
           'u': listu,
           'v': listv,
           'w': listw,
           'x': listx,
           'y': listy,
           'z': listz,
           
           ')': list00,
           '(': list99,
           '*': list88,
           '&': list77,
           '^': list66,
           '%': list55,
           '$': list44,
           '#': list33,
           '@': list22,
           '!': list11,
           'A': listA,
           'B': listB,
           'C': listC,
           'D': listD,
           'E': listE,
           'F': listF,
           'G': listG,
           'H': listH,
           'I': listI,
           'J': listJ,
           'K': listK,
           'L': listL,
           'M': listM,
           'N': listN,
           'O': listO,
           'P': listP,
           'Q': listQ,
           'R': listR,
           'S': listS,
           'T': listT,
           'U': listU,
           'V': listV,
           'W': listW,
           'X': listX,
           'Y': listY,
           'Z': listZ}
x = 0
for c in password:

    typo = list(password)
    for e in my_dict[c]:

        typo[x] = e
        print ''.join(typo)
    x += 1
