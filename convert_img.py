class imageGenerate:

    def __init__(self, path_file): # without extension
        self.path_file = path_file
  # Jpg to Png
    def convertJpgPng(self):
        from PIL import Image

        im1 = Image.open(self.path_file + '.jpg')
        im1.save(self.path_file+'.png')
  # Jpeg to Png  
    def convertJpegPng(self):
        from PIL import Image

        im1 = Image.open(self.path_file + '.jpeg')
        im1.save(self.path_file+'.png')
  # Png to Jpg 
    def convertPngJpg(self):
        from PIL import Image

        im1 = Image.open(self.path_file + '.png')
        rgb_im = im1.convert('RGB')
        rgb_im.save(self.path_file+'.jpg')

  # Pnf to Pdf	
    def convertPngPdf(self):
        from PIL import Image

        im1 = Image.open(self.path_file + '.png')
        rgb_im = im1.convert('RGB')
        rgb_im.save(self.path_file+'.pdf')
