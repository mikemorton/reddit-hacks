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

messages = client.get_messages()

for (user,cssclass) in client.get_messages():
    csvdata.append((user, '', cssclass))
    
csvdata.reverse()

print csvdata
for i in xrange(0, len(csvdata), 100):
    client.flaircsv('sports', csvdata[i:i+100])

