import requests
import webbrowser

def request_birds(url_requested):
    response = requests.get(url_requested)
    return response.json()
                    

def build_web_page(birds):

    html = "<html>\n<head>\n\t<title>Pájatos</title>\n</head>\n<body style='text-align: center'>\n\t<ul>\n"
    for bird in birds:
        spanish_name = f'<span>{bird["name"]["spanish"]}</span>'
        english_name = f'<span>{bird["name"]["english"]}</span>'
        html += f"\t\t<li style='display: inline-block; text-align: start'>\n\t\t\t<img src={bird["images"]["thumb"]} alt={bird["uid"]}><br>Nombre en español: {spanish_name}<br>Nombre en inglés: {english_name}\n\t\t</li>\n"

    html += "\t</ul>\n</body>\n</html>"
    with open("index.html", "w") as file:
        file.write(html)

endpoint = "https://aves.ninjas.cl/api/birds"

if __name__ == "__main__":
    birds = request_birds(endpoint)
    build_web_page(birds)
    macos_chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    webbrowser.get(macos_chrome_path).open('index.html')