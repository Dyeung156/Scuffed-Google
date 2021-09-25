import wit

access_token = 'LYPS4NQHJ3JZ3HE223LB6XZEEEAX2QR7'
client = wit.Wit(access_token)

response = client.message("What time is it?")
print(response)

