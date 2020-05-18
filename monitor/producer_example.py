from kafka import KafkaProducer
import json
import time

from monitor.results import get_result
from monitor.logging import logger


def producer_example(service_uri, ca_path, cert_path, key_path, checked_url):
    producer = KafkaProducer(
        bootstrap_servers=service_uri,
        security_protocol="SSL",
        ssl_cafile=ca_path,
        ssl_certfile=cert_path,
        ssl_keyfile=key_path,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    while True:
        result = get_result(checked_url)
        logger.info("Sending: {}".format(result))
        producer.send("python_example_topic", result)

        # Wait for all messages to be sent
        producer.flush()
        time.sleep(5)
