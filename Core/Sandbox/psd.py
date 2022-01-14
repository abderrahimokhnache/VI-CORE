from photoshop import Session
import photoshop.api as psi
import os
from tempfile import mkdtemp
from utilities import spark
def discription():

	discription_dict = {
            "tag": "playsound",
            "patterns": ["photoshop","edit image","editing"],
            "responses": ["Done " , "Got it"]
        }
	return discription_dict 

class Psdcon :
	def new_doc(self):
		app = psi.Application()
		docRef = app.documents.add(1920, 1080, 72.0, "My New Document")

def execute(term="") :
	spark.Talk("loading ps controller")
	while True :
		output = spark.Listen()
		psdcon = Psdcon()
		if "new document" in output :
			psdcon.new_doc()
			spark.Talk("New Document has been created")
		if 'fill' in output:

			with Session() as ps:
			    document = ps.active_document
			    # Create color object of color red.
			    fillColor = ps.SolidColor()
			    fillColor.rgb.red = 222
			    fillColor.rgb.green = 0
			    fillColor.rgb.blue = 0
			    # Add a new layer called Background.
			    layer = document.artLayers.add()
			    layer.name = "Background"
			    # Select the entire layer.
			    document.selection.selectAll()
			    # Fill the selection with color.
			    document.selection.fill(fillColor)
			    # Deselect.
			    document.selection.deselect()
		if "new layer" in output:
			spark.Talk('what would you name it !')
			bn = spark.Listen()
			document = ps.active_document
			layer = document.artLayers.add()
			layer.name = bn
			document.selection.deselect()
		if 'save as pdf' in output :
			with Session() as ps:
			    option = ps.PDFSaveOptions(jpegQuality=12, layers=True, view=True)
			    pdf = os.path.join(mkdtemp(), "output.pdf")
			    ps.active_document.saveAs(pdf, option)
		if 'open' in output :	
			spark.Talk('Make sure the file is in the clipboard')
			app = psi.Application()
			app.load("your/psd/or/psb/file_path.psd")