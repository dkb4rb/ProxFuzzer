import requests

def check_proxy(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Respuesta 200 encontrada en la URL: {url}")
        return True
    return False

def main():
    host = "192.168.1.101"
    base_url = "http://192.168.1.101:3668?proxy=http://192.168.1.101:{}/"

    # Rango de puertos a verificar
    start_port = 1
    end_port = 65535

    for port in range(start_port, end_port + 1):
        url = base_url.format(port)
        if check_proxy(url):
            break

if __name__ == "__main__":
    main()
