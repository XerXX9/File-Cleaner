import os
original_path = []
file_name = []
final_path = []
def script():
    def crawler(parent):
        for root,dir,file in os.walk(parent):
            match root:
                case "C:Pictures" | "C:Pictures\Camera Roll" | "C:Pictures\Saved Pictures" | "C:Pictures\Screenshots":
                    pass
                case _:
                    for x in file:
                        if x.endswith(".png")  or x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".webp"):
                            original_path.append(root+"\\"+x)
                            file_name.append(x)

    def new_path(files):
        target = "C:\\Users\\Admin\\Pictures\\Unsorted\\"
        for a in files:
            final = target + a
            final_path.append(final)   

    def new_path_d(files):
        target = "D:\\Unsorted\\"
        for a in files:
            final = target + a
            final_path.append(final)   

    def replacer(op, fp):
        for i in range(len(op)):
            os.rename(op[i],fp[i])

    def d_replacer(op, fp):
        for i in range(len(op)):
            os.rename(op[i],fp[i])

    crawler("C:Downloads")
    new_path(file_name)
    replacer(original_path, final_path)
    crawler("C:Desktop")
    new_path(file_name)
    replacer(original_path, final_path)
    crawler("D:\Downloads_D")
    new_path_d(file_name)
    d_replacer(original_path, final_path)

script()