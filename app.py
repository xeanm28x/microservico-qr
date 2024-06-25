from flask import Flask, request, jsonify, send_file
import qrcode
import io
from qrcode.image.pil import PilImage
import base64

app = Flask(__name__)

@app.route('/gerar_qr_code', methods=['POST'])

def gerar_qr_code():

    data = request.json

    if not data or 'valor' not in data or 'id_livro' not in data:
        return jsonify({'message': 'Dados inválidos. Valor e livro são obrigatórios.'}), 400
    
    valor = data['valor']
    id_livro = data['id_livro']

    pix_payload = f"00020126440014BR.GOV.BCB.PIX0136+556199999999220820000014520400005303986540{valor:.2f}5802BR5913Nome Recebedor6008Brasilia62280515ID12345678901234-1" + str(id_livro)

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(pix_payload)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # return send_file(buffer, mimetype='image/png', as_attachment=False, download_name='qrcode.png')
    return jsonify({'qr_code_base64': img_base64})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')