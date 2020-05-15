from kafka import KafkaConsumer
import json


def consumer_example(service_uri, ca_path, cert_path, key_path):
    consumer = KafkaConsumer(
        'python_example_topic',
        bootstrap_servers=service_uri,
        auto_offset_reset='earliest',
        security_protocol="SSL",
        ssl_cafile=ca_path,
        ssl_certfile=cert_path,
        ssl_keyfile=key_path,
        client_id="demo-client-1",
        group_id="demo-group",
        consumer_timeout_ms=1000,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    # Call poll twice. First call will just assign partitions for our
    # consumer without actually returning anything
    for _ in range(2):
        raw_msgs = consumer.poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                print("Received: {}".format(msg.value))

    # Commit offsets so we won't get the same messages again
    consumer.commit()
