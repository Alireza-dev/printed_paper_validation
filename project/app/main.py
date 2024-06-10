from flask import Flask, render_template, send_file, request

from module import generate_hash
from module1 import generate_qr_code_from_hash
from module2 import add_image_to_pdf


app = Flask(__name__)



@app.route('/')
def qr_code():
    return render_template('qrCodeReader.html')

@app.route('/download_file',  methods=['POST'])
def download_pdf(): 
    # Example usage
    input_string = request.form.get('user_input')
    print(input_string)
    hash_string = generate_hash(input_string)
    buffer = generate_qr_code_from_hash(hash_string)
    print(buffer)

    # Example usage
    input_pdf = "../data/pdf/form_template.pdf"
    buffer_image = buffer
    x = 247  # X position where you want to place the image
    y = 580  # Y position where you want to place the image

    pdf_buffer = add_image_to_pdf(input_pdf, buffer_image, x, y)

    return send_file(
        pdf_buffer,
        download_name="document.pdf",
        as_attachment=True,
        mimetype="application/pdf",
    )

if __name__ == "__main__":
    app.run(debug=True)