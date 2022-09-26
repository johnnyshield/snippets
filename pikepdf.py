from io import BytesIO
import pikepdf
from reportlab.pdfgen import canvas

def generate_stamp(msg, xy):
    x, y = xy
    buf = BytesIO()
    c = canvas.Canvas(buf)
    c.setFont("Courier", 8)
    c.setFillColorCMYK(0, 0, 0, 0, alpha=0.7)
    # c.rect(0, 0, 200, 200, stroke=0, fill=1)
    c.setFillColorCMYK(0, 0, 0, 100, alpha=1)
    c.drawString(x, y, msg)
    c.save()
    buf.seek(0)
    return buf

stamp = generate_stamp('Goods Received by William Nomates 31/05/2022 10:12:35 --- Approved by John Shield 01/06/2022 10:36:02', (10, 10))

with pikepdf.open('C:\Temp\pdf\doca.pdf') as pdf_orig, pikepdf.open(stamp) as pdf_text:
    formx_text = pdf_orig.copy_foreign(pdf_text.pages[0].as_form_xobject())
    
    formx_page = pdf_orig.pages[0]
    formx_name = formx_page.add_resource(formx_text, pikepdf.Name.XObject)    
    stamp_text = pdf_orig.make_stream(b'q 1 0 0 1 0 0 cm %s Do Q' % formx_name)
    pdf_orig.pages[0].contents_add(stamp_text)

    pdf_orig.save('C:\Temp\pdf\pike2.pdf')