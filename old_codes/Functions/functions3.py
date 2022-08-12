#8.9
messages = ["hello there", "general kenobi", "how civilised"]
def show_messages(message):
	for message_1 in message:
		print(message_1.title())
show_messages(messages)

#8.10
messages = ["hello there", "general kenobi", "how civilised"]
messages_sents = []

def print_messages(messages, messages_sents):
	while messages:
		message = messages.pop()
		print(f"Sending: {message.title()}!")
		messages_sents.append(message)
def sent_messages(messages_sents):
	print(f"following messages are sent:")
	for message_sent in messages_sents:
		print(message_sent.title())

print_messages(messages, messages_sents)
sent_messages(messages_sents)
print(messages)
print(messages_sents)
