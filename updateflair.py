import redditclient
import logging


def configure_logging():


    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    logger.addHandler(ch)

configure_logging()

client = redditclient.RedditClient()
client.log_in()

csvdata = list()
while True:
    messages = client.get_messages()

    empty = True
    for (user,cssclass) in client.get_messages():
        csvdata.append((user, '', cssclass))
        empty = False

    if empty:
        break

print csvdata
if len(csvdata) > 0:
    client.flaircsv('sports', csvdata)
