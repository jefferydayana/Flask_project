
from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io
app=Flask(__name__)


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", size=14)
        self.cell(0,10," ", ln=True, align="C")



@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        user_text=request.form['text']
        
        font_size=int(request.form.get("font_size", 14))

        pdf=PDF()
        pdf.add_page()

        

    
        pdf.add_font("NotoSans", "", "NotoSansDisplay-Regular.ttf", uni=True)
        pdf.set_font("NotoSans", size=font_size)
       
        pdf.multi_cell(0,10, txt=user_text)
        pdf_buffer = io.BytesIO()
        pdf.output(pdf_buffer)
        pdf_buffer.seek(0)

        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name="file.pdf",
            mimetype="application/pdf"
        )

        
    
    return render_template("form.html")



    

