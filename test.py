import requests

s = requests.Session()

login = s.get('http://localhost:8080/api/login')
print("1:", login.text)

out = s.get('http://localhost:8080/api')
print("2: ", out.text)


while True:
    query = input("Human: ")
    payload = { "query": query }
    output = s.post( "http://localhost:8080/api/query", json = payload )
    print(f"Assistant: {output.text}")
