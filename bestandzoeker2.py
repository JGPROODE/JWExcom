import os

def find_files(filename, search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result
#print(find_files("Bijlage 1 Mogelijke vragen eindgesprek (KD 0730).docx","c:/"))


print(find_files("studenten_2022-09-20_114432.xlsx","c:\\"))
print("klaar")
