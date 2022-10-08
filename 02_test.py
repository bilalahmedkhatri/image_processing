import random
import cv2
import os
from pathlib import Path

class Text:
    
    # @property
    def open_file(self):
        images_formats = ['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG', 'gif', 'GIF']
        images = []
        for l in os.listdir():
            d = r"%s/%s" % (os.getcwd(), l)
            if os.path.isdir(d):
                for img_frt in images_formats:
                    img_format = f"*.{img_frt}"
                    for b in Path(d).glob(img_format):
                        if str(b) not in images:
                            images.append(str(b))
        select_image = random.sample(images, 1)
        return ''.join(select_image)

    def remove_file(self):
        pass
        
        
    def show_image(self):
        open_image = cv2.imread(self.open_file())

        cv2.imshow('original', open_image)

        cv2.waitKey()
        if " " == ord(' '):
            cv2.imwrite(open_image, 'bilal.png')
            cv2.destroyAllWindows()

        
x = Text()

print(x.show_image())