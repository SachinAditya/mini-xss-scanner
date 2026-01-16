import requests
import argparse
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

PAYLOAD = "<script>alert(1)</script>"

def scan(url):
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)

    if not params:
        print("[-] No parameters found in the URL.")
        return

    print(f"[i] Scanning: {url}\n")

    for param in params:
        test_params = params.copy()
        test_params[param] = PAYLOAD

        new_query = urlencode(test_params, doseq=True)
        test_url = parsed_url._replace(query=new_query)
        final_url = urlunparse(test_url)

        try:
            response = requests.get(final_url, timeout=10)

            if PAYLOAD in response.text:
                print(f"[+] XSS FOUND in parameter: {param}")
                print(f"    Payload: {PAYLOAD}")
                print(f"    URL: {final_url}\n")
            else:
                print(f"[-] Not vulnerable: {param}")

        except requests.exceptions.RequestException as e:
            print(f"[!] Error scanning parameter {param}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Mini XSS Scanner")
    parser.add_argument("-u", "--url", required=True, help="Target URL with parameters")

    args = parser.parse_args()
    scan(args.url)

if __name__ == "__main__":
    main()
