import qrcode
import io

def generate_qr_code_from_hash(hash_string):
    # Create QR code from the hash
    img = qrcode.make(hash_string)

    # Save the QR code to a bytes buffer
    buffer = io.BytesIO()
    img.save(buffer)

    # Seek to the beginning of the buffer
    buffer.seek(0)

    return buffer

