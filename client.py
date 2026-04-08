import socket

# Replace with your Replit server URL if needed
HOST = "0.0.0.0"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))

    username = input("Enter your username: ")
    client.send(username.encode())

    response = client.recv(1024).decode()
    print(response)

    if "Vote" in response:
        vote = input("Enter your vote (A/B/C): ")
        client.send(vote.encode())

        result = client.recv(1024).decode()
        print(result)

except:
    print("Unable to connect to server")

finally:
    client.close()
