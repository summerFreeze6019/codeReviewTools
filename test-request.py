import requests

s = requests.Session()

login = s.get('http://localhost:8080/api/login')
print("1:", login.text)
print(login.headers.keys())
print(login.headers['Set-Cookie'])

#out = s.get('http://localhost:8080/api')
#print("2: ", out.text)
#
#
#while True:
#    query = input("Human: ")
#    payload = { "query": query }
#    output = s.post( "http://localhost:8080/api/query", json = payload )
#    print(f"Assistant: {output.text}")
