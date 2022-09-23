import cv2 as cv
import string
import random
import os

class GetTextFromImage():
    
    def __init__(self, image):
        self.image = image

    @property
    def get_image(self):
        return r"%s/images/%s"%(os.getcwd(), self.image)

    @property
    def GET_FILE_FORMAT(self):
        return self.get_image.split('.')[-1]
    
    def change_color_image(self, grey=None):
        print('color image')
        if grey != "grey":
            read_image = cv.imread(self.get_image, 1)
        else:
            print('grey')
            read_image = cv.imread(self.get_image, 0)
        read_image_color = cv.resize(read_image, (300,300))
        cv.imshow('original', read_image_color)
        wait = cv.waitKey()
        return (read_image_color, wait)
        
    @property
    def random_string(self):
        strings = string.ascii_letters
        return ''.join(random.choice(strings) for x in range(5))

    def save_image(self, grey=None):
        print('save image', self.GET_FILE_FORMAT)
        if self.change_color_image(grey)[1] == ord('s'):
            path = r"{0}/save_images/{1}.{2}".format(os.getcwd(), self.random_string, self.GET_FILE_FORMAT)
            cv.imwrite(path, self.change_color_image()[0])
        else:
            cv.destroyAllWindows()

x = GetTextFromImage("odoo_js.PNG")
print(x.save_image())
    


