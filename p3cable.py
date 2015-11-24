 
import os
import base64
import io
from PIL import Image

from jinja2 import Environment, FileSystemLoader
 
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)
 
 
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 
def main():

    jpgfile = "DB9Male.jpg"
    
    
    '''
    img = Image.open("DB9Male.jpg")
    

    png_image_buffer = io.StringIO()
    img.save(png_image_buffer, format="PNG")
    imgdata = "data:image/png;base64," + base64.b64encode(png_image_buffer.getvalue()).decode('utf-8')
    '''
    
    # for automating....  PIL Image.format .....
    imgdata = "data:image/jpeg;base64," + base64.b64encode(open(jpgfile,"rb").read()).decode('utf-8')
    

    fname = "output.svg"
    f = open(fname, 'w')

    context = {
        'templatename': "Hello Simon Huskier......",
        'imgdata': imgdata
    }
    
    html = render_template('SchPCB_template.svg', context)
    
    f.write(html)

########################################
 
if __name__ == "__main__":
    main()
