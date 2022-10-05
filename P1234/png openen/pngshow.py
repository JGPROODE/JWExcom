def show():

    file = 'C:\Python38\P2-3\png openen\02n.png' #raw_input("What is the name of the image file? ")

    picture = Image(file)

    width, height = picture.size()

    pix = picture.getPixels()
