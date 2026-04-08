import socket

# Use 0.0.0.0 for online platforms like Replit
HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started... Waiting for connections...")

votes = {"A": 0, "B": 0, "C": 0}
voted_users = set()

while True:
    client, addr = server.accept()
    print(f"Connected with {addr}")

    try:
        # Receive username
        username = client.recv(1024).decode()

        if username in voted_users:
            client.send("You have already voted!".encode())
        else:
            client.send("Vote for A, B, or C:".encode())

            vote = client.recv(1024).decode().upper()

            if vote in votes:
                votes[vote] += 1
                voted_users.add(username)
                client.send("Vote submitted successfully!".encode())
            else:
                client.send("Invalid vote!".encode())

        print("Current Votes:", votes)

    except:
        print("Error occurred with client")

    finally:
        client.close()
