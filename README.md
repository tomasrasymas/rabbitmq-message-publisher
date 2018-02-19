# Publish messages to RabbitMQ service

Publishes any number of messages (with set timeout) to RabbitMQ service.

### Usage
```
usage: rabbitmq_message_publisher.py [-h] -u URL -e EXCHANGE -r ROUTING_KEY -m
                                     MESSAGE [-n NUM_OF_MESSAGE] [-t TIMEOUT]
                                     [-v]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Url of RabbitMQ server
  -e EXCHANGE, --exchange EXCHANGE
                        Exchange to bind
  -r ROUTING_KEY, --routing_key ROUTING_KEY
                        Routing key
  -m MESSAGE, --message MESSAGE
                        Message to post
  -n NUM_OF_MESSAGE, --number_of_message NUM_OF_MESSAGE
                        Number of messages to post
  -t TIMEOUT, --timeout TIMEOUT
                        Number of seconds to wait after publishing message
  -v, --verbose         Verbose
```

Command example:
```
python rabbitmq_message_publisher.py -u 'amqp://john:johnpassword@rabbit.john.com:5672/johnvhost?heartbeat=10' -e clients -r 'tmp.prices' -v -m '{"price": "12.3"}' -n 1000 -t 0.1
```
