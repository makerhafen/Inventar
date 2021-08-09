f = "Inventar/InventarListe.md"

content = open(f, "rb").read().decode("utf-8")

rows = content.split("\n")

max_length = {
    "ID" : 0,
    "Name" : 0,
    "Kategorie" : 0,
    "Location" : 0,
    "Image" : 0,
    "Shop" : 0,
}
for row in rows:
    row = row.strip()
    if row.find("|") == -1:
        continue
    cols = row.split("|")
    cols = [col.strip() for col in cols[1:-1]]
    try:
        ID, Name, Kategorie, Location, Image, Shop = cols
    except:
        print("Failed to parse Line:")
        print(row)
        exit(1)
    if len(ID) > max_length["ID"]: max_length["ID"] = len(ID)
    if len(Name) > max_length["Name"]: max_length["Name"] = len(Name)
    if len(Kategorie) > max_length["Kategorie"]: max_length["Kategorie"] = len(Kategorie)
    if len(Location) > max_length["Location"]: max_length["Location"] = len(Location)
    if len(Image) > max_length["Image"]: max_length["Image"] = len(Image)
    if len(Shop) > max_length["Shop"]: max_length["Shop"] = len(Shop)


for row in rows:
    row = row.strip()
    if row.find("|") == -1:
        continue
    cols = row.split("|")
    cols = [col.strip() for col in cols[1:-1]]
    ID, Name, Kategorie, Location, Image, Shop = cols

    x = ("| %s%s | %s%s | %s%s | %s%s | %s%s | %s%s |" % (
        ID, " "*(max_length["ID"]-len(ID)),
        Name, " "*(max_length["Name"]-len(Name)),
        Kategorie, " "*(max_length["Kategorie"]-len(Kategorie)),
        Location, " "*(max_length["Location"]-len(Location)),
        Image, " "*(max_length["Image"]-len(Image)),
        Shop, " "*(max_length["Shop"]-len(Shop)),
    ))
    print(x.encode("utf-8"))
