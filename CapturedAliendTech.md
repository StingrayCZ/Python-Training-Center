```Py
# By DUZA 2021

import xlwt
import calendar
from xlwt import Workbook
from _datetime import datetime
from duza_external_fce_xls import *

menopriezvisko = ""
rok = 2021
cas_prichodu = "8:30"
cas_odchodu = "17:00"
print (rok, end=" ")
#zoznam sviatkov
vsetky_sviatky= [ [0], \
                 [1], \
                 [0], \
                 [0], \
                 [2,5], \
                 [1, 8], \
                 [0], \
                 [5,6], \
                 [0], \
                 [28], \
                 [28], \
                 [17], \
                 [24,25,26 ] ]
czmesiace = ['Leden','Únor','Březen','Duben','Květen','Červen','Červenec','Srpen','Září','Říjen','Listopad','Prosinec']
kniha = Workbook(encoding='utf-8')
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 1 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)

#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 2 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 3 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 4 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 5 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 6 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 7 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 8 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 9 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 10 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 11 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)
#######################################################################################################################
### Novy mesiac
#######################################################################################################################
indexmesiac = 12 # 1= Leden; 12= Prosinec
mesiac = czmesiace[indexmesiac-1]
print (mesiac, end=" ")

sheet = kniha.add_sheet(mesiac, cell_overwrite_ok=True)

st = xlwt.easyxf('pattern: pattern solid;') #'pattern: pattern solid;'
st.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

ohranicenie = xlwt.Borders()
ohranicenie.left = 1
ohranicenie.right = 1
ohranicenie.top = 1
ohranicenie.bottom = 1

stbold = xlwt.easyxf('pattern: pattern solid; font: bold on')
stbold.pattern.pattern_fore_colour = 1 # 0=cierna(default), 1=biela, 45=ružova pre sviatok

stbold_ram = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black, bold on; align: horiz left; \
                        borders: right 1, left 1, top 1, bottom 1")

stcenter = xlwt.easyxf("pattern: pattern solid, fore_color white; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
#stcenter.borders = ohranicenie

stcenterpink = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcenterpinkbold = xlwt.easyxf("pattern: pattern solid, fore_color 45; font: color black, bold on; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")
stcentergrey = xlwt.easyxf("pattern: pattern solid, fore_color 22; font: color black; align: horiz center; \
                        borders: right 1, left 1, top 1, bottom 1")

# vytlac hlavicku celu
hlavicka(sheet, st, stbold)
sheet.write(0, 5, menopriezvisko, stbold)

maxdni = calendar.monthrange(rok, indexmesiac)[1]
print(maxdni)
arrayofdays = range(1, maxdni+1)
print(list(arrayofdays))

# čísla dni v stlpci
for indexrow in range(maxdni):
    blank = 0 # 0 pracovny den, 1 vikend, 2 sviatok
    sheet.write(4 + indexrow, 0, indexrow + 1, stcenter)
    print( (indexrow + 1), end=" ")

    # VIKENDY prepis bunku sedou farbou
    aday = datetime(rok, indexmesiac, indexrow + 1)
    if aday.isoweekday() > 5:
        blank = 1
        sheet.write(4 + indexrow, 0, indexrow + 1, stcentergrey)
        print(" vikend", end=" ")
        fce_riadok_vikend(sheet, stcentergrey, indexrow)

    # SVIATKY prepis bunku ruzovou farbou
    if (indexrow + 1) in vsetky_sviatky[indexmesiac]:
        blank = 2
        sheet.write(4 + indexrow, 0, indexrow + 1, stcenterpink)
        print(" sviatok", end=" ")
        fce_riadok_sviatok(sheet, stcenterpink, stcenterpinkbold, indexrow)
    print() # odriadkuj

    # PRACOVNE HODINY
    if blank == 0:
        # Príchod
        sheet.write(4 + indexrow, 1, cas_prichodu , stcenter)
        # Odchod
        sheet.write(4 + indexrow, 2, cas_odchodu , stcenter)
        # Prestávka Príchod
        sheet.write(4 + indexrow, 3, "11:30", stcenter)
        # Prestávka Odchod
        sheet.write(4 + indexrow, 4, "12:00", stcenter)
        # Prerušenie Príchod
        sheet.write(4 + indexrow, 5, " ", stcenter)
        # Prerušenie Odchod
        sheet.write(4 + indexrow, 6, " ", stcenter)
        #
        sheet.write(4 + indexrow, 7, " ", stcenter)
        #
        sheet.write(4 + indexrow, 8, " ", stcenter)
        # Odpracovane hodiny
        sheet.write(4 + indexrow, 9, "8:00", stcenter)
        # Presčas
        sheet.write(4 + indexrow, 10, " ", stcenter)



kniha.save('dochazka_'+menopriezvisko +'_'+ str(rok) +'.xls')
```
