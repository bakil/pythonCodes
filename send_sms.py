from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC791f622a0067edc458dfd31c090f48b8"
# Your Auth Token from twilio.com/console
auth_token  = "240511aea1e6dcd9b162cb95b917f428"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+601162319354", #your phone number
    from_="+17479008179", # twilio phone no
    body="Hello from Python!")

print(message.sid)
