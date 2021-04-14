import shutil
import os
import FileUtil

# 1-) drawable folderlarin bulundugu mevcut destinationa terminalden geliyoruz.
current_path = input("Enter images folder path: ")
print('Current Path is ' + current_path)
os.chdir(current_path)

# 2-) Bir tane destination path vericez.
destination_path = input("Enter destination path: ")

if not type(destination_path) is str:
    raise TypeError("You should enter string value ")

if not os.path.exists(destination_path):
    print("Destination path doesn't exist")
else:
    print("Destination path exists")

# 3-) Destination path icinde her bir drawable folder ini once buluyoruz yoksa da yaratiyoruz.
if not os.path.exists(destination_path + "/drawable-xxxhdpi"):
    os.mkdir(destination_path + "/drawable-xxxhdpi")

if not os.path.exists(destination_path + "/drawable-xxhdpi"):
    os.mkdir(destination_path + "/drawable-xxhdpi")

if not os.path.exists(destination_path + "/drawable-xhdpi"):
    os.mkdir(destination_path + "/drawable-xhdpi")

if not os.path.exists(destination_path + "/drawable-hdpi"):
    os.mkdir(destination_path + "/drawable-hdpi")

if not os.path.exists(destination_path + "/drawable-mdpi"):
    os.mkdir(destination_path + "/drawable-mdpi")

if not os.path.exists(destination_path + "/drawable"):
    os.mkdir(destination_path + "/drawable")

# 4-) Ilk once drawable-xxxhdpi folderin icine bakiyoruz, sirasiyla drawable-xxhdpi .....
for entry in os.listdir(current_path):
    dest_path = ""
    if entry == 'drawable':
        dest_path = destination_path + "/drawable"
    elif entry == 'drawable-mdpi':
        dest_path = destination_path + "/drawable-mdpi"
    elif entry == 'drawable-hdpi':
        dest_path = destination_path + "/drawable-hdpi"
    elif entry == 'drawable-xhdpi':
        dest_path = destination_path + "/drawable-xhdpi"
    elif entry == 'drawable-xxhdpi':
        dest_path = destination_path + "/drawable-xxhdpi"
    elif entry == 'drawable-xxxhdpi':
        dest_path = destination_path + "/drawable-xxxhdpi"
    else:
        print("I don't know what is this folder")
        continue

    FileUtil.move_all_files_to_dest(current_path + "/" + entry, dest_path)

# 5-) Buldugumuz drawable folderlarin icindeki file'larin png mi, svg mi yoksa webp mi oldularini ogreniyoruz.

# 6-) Destination icin verilen projenin structure folderinda gerekli drawable folderlari mevcut mu degil mi diye
# kontrol ediyoruz. Eger bu folderlar mevcut degilse yaratiyoruz.

# 7-) Basliyoruz tek tek file lari bu folderlarin iclerine yazmaya. shutil.move() komutu

# 8-) Eger problemler ile karsilasma durumlarinda console'dan mesajlar bastirmaliyiz.

# 9-) svg leri direk drawable folder icine atiyoruz. PNG ve WEBP olanlari -dpi folderlarinin altina.

# 10-) Ekstra eklenebilecekler, mesela rename olayi yapilabilir. her bir dosya icin.
