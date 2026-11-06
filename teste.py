import requests

headers = {
    'Authorization': "Barer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwiZXhwIjoxNzkzODA1MjQ4fQ.xFiKVgRjKw4PwS_iGfsG2nG3KwGVenT18B6bsHran0E"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers = headers)

print(requisicao)
print(requisicao.json())