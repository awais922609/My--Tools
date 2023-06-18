import requests
from bs4 import BeautifulSoup
import re


def print_banner(text):
    banner_width = 60
    banner_text = f" {text} "
    banner = banner_text.center(banner_width, "*")
    print("\n" + banner + "\n")


def fetch():
    with open("urls.txt", "r") as urls:
        for url in urls:
            url = url.strip()
            if not url:
                continue
            print_banner("Footprint Report for " + url + " Web Server")
            req = requests.get(url)
            result = dict(req.headers)
            for item, value in result.items():
                print(f"{item}: {value}")

            # This is the creative part
            soup = BeautifulSoup(req.content, "html.parser")
            print_banner("Links Found")
            for link in soup.find_all("a"):
                print("Link: " + link.get("href"))

            # This is the new and creative part
            print_banner("Script Hrefs Found")
            for script in soup.find_all("script"):
                script_content = script.get_text()
                hrefs = re.findall(r"href=\"(.*?)\"", script_content)
                for href in hrefs:
                    print("Script href: " + href)

            # Here's the additional creative feature
            print_banner("Forms Found")
            for form in soup.find_all("form"):
                form_action = form.get("action")
                form_method = form.get("method")
                print("Form Action: " + form_action)
                print("Form Method: " + (form_method if form_method else "None"))
                print("--------------")

            # This is the new and creative part
            print_banner("Hidden Fields Found")
            for form in soup.find_all("form"):
                for input in form.find_all("input"):
                    if input.get("type") == "hidden":
                        hidden_value = input.get("value")
                        if hidden_value is not None:
                            print("Hidden Field Name: " + input.get("name"))
                            print("Hidden Field Value: " + hidden_value)

            # This is the creative and awesome part
            print_banner("Potential Vulnerabilities Found")
            for form in soup.find_all("form"):
                if form.get("action") == "/admin":
                    print("Potential vulnerability: Admin page found")
                if form.get("method") == "POST":
                    if form.find_all("input", {"name": "password"}):
                        print("Potential vulnerability: Password field found in POST form")

            print("\n" + "*" * 60 + "\n")


fetch()
