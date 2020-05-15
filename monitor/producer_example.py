from kafka import KafkaProducer
import json
import requests


def get_result(url="http://google.com"):
    response = requests.get(url)

    return {
        'status_code': response.status_code,
        'reason': response.reason,
        'response_time': response.elapsed.total_seconds(),
        }


def producer_example(service_uri, ca_path, cert_path, key_path):
    producer = KafkaProducer(
        bootstrap_servers=service_uri,
        security_protocol="SSL",
        ssl_cafile=ca_path,
        ssl_certfile=cert_path,
        ssl_keyfile=key_path,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    result = get_result()
    print("Sending: {}".format(result))
    producer.send("python_example_topic", result)

    # Wait for all messages to be sent
    producer.flush()
