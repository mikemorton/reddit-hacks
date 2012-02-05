import redditclient
import logging
import sys


def configure_logging():


    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    logger.addHandler(ch)

#configure_logging()

username = sys.argv[1]
password = sys.argv[2]


client = redditclient.RedditClient()
if not client.log_in(username, password):
    print "Failed to log in"
    exit()

csvdata = list()

messages = client.get_messages()

for (user,messagebody) in client.get_messages():
    flair = messagebody.split()[0]
    if flair == 'clear':
        flair = ''
    csvdata.append((user, '', flair))
    print "%s %s" % (user, flair)
    
csvdata.reverse()

for i in xrange(0, len(csvdata), 100):
    client.flaircsv('sports', csvdata[i:i+100])

print "\nUpdated %d users" % (len(csvdata))
