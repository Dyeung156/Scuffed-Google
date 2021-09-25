import wit, json

def response_handler(resp_message):
    pass

access_token = 'LYPS4NQHJ3JZ3HE223LB6XZEEEAX2QR7'
client = wit.Wit(access_token)

response = client.message("hey lol")
client.interactive()

