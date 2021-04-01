# Fuzzy Logic Algorithm without numpy skfuz for learning and training
# It is based on case study watering system in "CII-2M3 Pengantar Kecerdasan Buatan Pokok Bahasan 07.ppt"

suhu = int(input("Masukan suhu: "))
print("Suhu = {}°C\n".format(suhu))
kelembaban = int(input("Masukan kelembaban: "))
print("Kelembaban = {}%\n".format(kelembaban))

#Fuzzification

cold = cool = normal = warm = hot = dry = moist = wet = 0
if suhu <= 0:
    cold = 1
elif suhu > 0 and suhu < 3:
    cold = (3 - suhu) / 3
    cool = suhu / 3
elif suhu >= 3 and suhu <= 12:
    cool = 1
elif suhu > 12 and suhu < 15:
    cool = (15 - suhu) / 3
    normal = (suhu - 12) / 3
elif suhu >= 15 and suhu <= 24:
    normal = 1
elif suhu > 24 and suhu < 27:
    normal = (27 - suhu) / 3
    warm = (suhu - 24) / 3
elif suhu >= 27 and suhu <= 36:
    warm = 1
elif suhu > 36 and suhu < 39:
    warm = (39 - suhu) / 3
    hot = (suhu - 36) / 3
elif suhu >= 39:
    hot = 1

print("CEK")
print("Cold: ", cold)
print("Cool: ", cool)
print("Normal: ", normal)
print("Warm: ", warm)
print("Hot: ", hot)
print("")

if kelembaban <= 10:
    dry = 1
elif kelembaban > 10 and kelembaban < 20:
    dry = (20 - kelembaban) / 10
    moist = (kelembaban - 10) / 10
elif kelembaban >= 20 and kelembaban <= 40:
    moist = 1
elif kelembaban > 40 and kelembaban < 50:
    moist = (50 - kelembaban) / 10
    wet = (kelembaban - 40) / 10
elif kelembaban >= 50:
    wet = 1

print("CEK2")
print("Dry: ", dry)
print("Moist: ", moist)
print("Wet: ", wet)
print("")

# Fuzzy Inference

durasi = []

def inferenceShort(var_suhu, var_kelembaban):
    if var_suhu != 0:
        if var_kelembaban != 0:
            hasil = min(var_suhu, var_kelembaban)
            durasi.append([hasil, 20])

def inferenceMedium(var_suhu, var_kelembaban):
    if var_suhu != 0:
        if var_kelembaban != 0:
            hasil = min(var_suhu, var_kelembaban)
            durasi.append([hasil, 40])

def inferenceLong(var_suhu, var_kelembaban):
    if var_suhu != 0:
        if var_kelembaban != 0:
            hasil = min(var_suhu, var_kelembaban)
            durasi.append([hasil, 60])

# Sugeno Inference
inferenceMedium(warm, moist)
inferenceMedium(hot, moist)
inferenceLong(warm, dry)
inferenceLong(hot, dry )

durasi.sort()
now = durasi[0][1]
nowIdx = durasi[0]
sugeno = []

for i in range(len(durasi)):
    if durasi[i][1] == now:
        sugeno.append(max(nowIdx, durasi[i]))
    now = durasi[i][1]
    nowIdx = durasi[i]

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

sugenoNew = unique(sugeno)
print("Durasi: ", durasi)
print("Sugeno: ", sugenoNew)


# Defuzzification
pembilangIndex = penyebutIndex = pembilangHasil = penyebutHasil = 0

for i in range(len(sugenoNew)):
    pembilangIndex = sugenoNew[i][0]*sugenoNew[i][1] 
    penyebutIndex = sugenoNew[i][0]
    pembilangHasil = pembilangHasil + pembilangIndex
    penyebutHasil = penyebutHasil + penyebutIndex

duration = pembilangHasil / penyebutHasil
print("Perhitungan rata-rata berbobot menghasilkan durasi penyiraman air = ", duration)

# By Imam Rafiif Arrazaan
# Reference: https://www.youtube.com/watch?v=XKj8kL1t0Sc&ab_channel=FarhannaMar%27i