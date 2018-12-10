from os import listdir, getcwd, path, makedirs

Image_folder = "Hiroshige/The Fifty-three Stations of the Tōkaidō"

try:
    # Create target Directory
    makedirs(getcwd() + "/../" + Image_folder)
    print("Directory Created ") 
except FileExistsError:
    print("Directory already exists")

for filename in listdir(getcwd() + "/../Image Content/" + Image_folder + "/"):
    print(filename)
    with open(getcwd() + "/../" + Image_folder + "/" + filename[:filename.find("-")-1] + " - ImagePage.html","w", encoding='utf-8') as f:
        f.write(u'''<!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <link rel="stylesheet" href="../../style.css"/>
            <title>''' + filename + '''</title>
        </head>
        <body style="margin: 0; background-color:rgb(32, 32, 32);">
            <img src="../../Image Content/''' + Image_folder + '''/''' + filename + '''" class="ukiyoe_image" />
        </body>
        </html>''')


