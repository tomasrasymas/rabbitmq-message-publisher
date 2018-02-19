from argparse import ArgumentParser
import time
import pika


def execute_publisher(url, exchange, routing_key, message, num_of_messages, timeout, verbose):
    connection = pika.BlockingConnection(pika.URLParameters(url))
    channel = connection.channel()

    msg_count = 0

    while msg_count < num_of_messages:
        if channel.basic_publish(exchange=exchange,
                                 routing_key=routing_key,
                                 body=message,
                                 properties=pika.BasicProperties(delivery_mode=1)):

            if verbose:
                print(msg_count + 1, 'Published', message)
        else:
            if verbose:
                print(msg_count + 1, 'FAIL', message)

        msg_count += 1

        time.sleep(timeout)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-u', '--url', dest='url', type=str, required=True, help='Url of RabbitMQ server')
    parser.add_argument('-e', '--exchange', dest='exchange', type=str, required=True, help='Exchange to bind')
    parser.add_argument('-r', '--routing_key', dest='routing_key', type=str, required=True, help='Routing key')
    parser.add_argument('-m', '--message', dest='message', type=str, required=True, help='Message to post')
    parser.add_argument('-n', '--number_of_message', dest='num_of_message', type=int, required=False,
                        help='Number of messages to post', default=100)
    parser.add_argument('-t', '--timeout', dest='timeout', type=float, required=False,
                        help='Number of seconds to wait after publishing message', default=2)
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', required=False,
                        default=False, help='Verbose')

    args = parser.parse_args()

    if args.verbose:
        print('*' * 50)
        for i in vars(args):
            print(str(i) + ' - ' + str(getattr(args, i)))

        print('*' * 50)

    execute_publisher(args.url, args.exchange, args.routing_key, args.message,
                      args.num_of_message, args.timeout, args.verbose)
