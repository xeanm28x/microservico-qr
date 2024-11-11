# Micro Serviço de QR Code ⚙️

Este projeto implementa um micro serviço em Flask para gerar QR Codes baseados em dados recebidos, incluindo um link de confirmação de compra ou dados de pagamento.

## Funcionalidades 📶

- Geração de QR Code para simulação de pagamento
- Integração com uma fila RabbitMQ para processar mensagens de vendas
- Retorno de QR Code em base64 para uso em aplicativos front-end

## Tecnologias Utilizadas 👩‍💻

- Python
- Flask
- qrcode (biblioteca Python para geração de QR Codes)
- RabbitMQ (para filas de mensagens)
- Pillow (para manipulação de imagens)

## Instalação 📥

### Pré-requisitos

- Python 3.7 ou superior
- RabbitMQ (configurado e rodando localmente ou em outro servidor)
- Git

### Passos

1. Clone o repositório:

   ```bash
   git clone git@github.com:seu_usuario/microservico-qr.git
   cd microservico-qr
