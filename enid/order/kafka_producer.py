from confluent_kafka import Producer
from django.conf import settings
import json

class KafkaProducer:
    def __init__(self):
        self.bootstrap_servers = settings.KAFKA_BOOTSTRAP_SERVERS
        self.producer = Producer({'bootstrap.servers': self.bootstrap_servers})

    def delivery_report(self, err, msg):
        """Función de callback para manejar los informes de entrega del productor."""
        if err is not None:
            print(f'Error al enviar el mensaje: {err}')
        else:
            print(f'Mensaje enviado a {msg.topic()} [{msg.partition()}] @ offset {msg.offset()}')

    def produce_message(self, topic, key, value):
        """Función para enviar un mensaje al topic especificado."""
        self.producer.produce(topic, key=key, value=value.encode('utf-8'), callback=self.delivery_report)
        self.producer.poll(0)

    def flush(self):
        """Espera a que se confirmen todos los mensajes enviados."""
        self.producer.flush()

    def close(self):
        """Cierra el productor de Kafka."""
        self.producer.close()