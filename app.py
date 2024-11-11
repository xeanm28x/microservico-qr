from flask import Flask, request, jsonify, send_file
import qrcode
import io
from qrcode.image.pil import PilImage
import base64
import pika
import json
import threading

app = Flask(__name__)

@app.route('/gerar_qr_code', methods=['POST'])
def gerar_qr_code():
    data = request.json

    if not data or 'valor' not in data or 'id_livro' not in data:
        return jsonify({'message': 'Dados inválidos. Valor e livro são obrigatórios.'}), 400

    # Em vez do pix_payload, vamos gerar o QR Code com o link para a tela de confirmação
    url_confirmacao = "https://ava.ufms.br/"  # URL completa para a confirmação

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url_confirmacao)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return jsonify({'qr_code_base64': img_base64})

# Função para processar mensagens da fila RabbitMQ
def processar_mensagem(ch, method, properties, body):
    dados_venda = json.loads(body)
    print(f" [x] Processando venda: {dados_venda}")
    
    # Extraia os valores para gerar o QR code
    valor = dados_venda.get("valor_total")
    id_livro = dados_venda.get("venda", {}).get("id_livro", None)

    if valor and id_livro:
        # Simula uma requisição interna para gerar o QR code
        qr_data = {'valor': valor, 'id_livro': id_livro}
        response = app.test_client().post('/gerar_qr_code', json=qr_data)
        qr_code_result = response.json
        print("QR Code Gerado:", qr_code_result.get('qr_code_base64'))

# Configurar o consumidor RabbitMQ
def iniciar_consumidor():
    conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexao.channel()

    # Declarar a fila caso ainda não exista
    canal.queue_declare(queue='fila_qr_code')

    # Configurar o consumidor
    canal.basic_consume(
        queue='fila_qr_code',
        on_message_callback=processar_mensagem,
        auto_ack=True
    )

    print(' [*] Esperando por mensagens na fila_qr_code. Para sair, pressione CTRL+C')
    canal.start_consuming()

# Iniciar o consumidor RabbitMQ em um novo thread
if __name__ == '__main__':
    consumidor_thread = threading.Thread(target=iniciar_consumidor)
    consumidor_thread.start()
    
    # Iniciar o servidor Flask
    app.run(debug=True, host='0.0.0.0')
