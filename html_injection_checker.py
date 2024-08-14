# html_injection_checker.py
import sys
from crawler import crawl
from vulnerability_checker import test_forms, test_parameters, PAYLOADS

def main(url):
    print(f"Scanning {url} for HTML Injection vulnerabilities...")

    try:
        # Crawl the URL to get forms and parameters
        data = crawl(url)
        forms = data['forms']
        params = data['params']

        # Test forms
        print("\nTesting forms for HTML Injection...")
        form_results = test_forms(url, forms, PAYLOADS)
        if form_results:
            print("\nHTML Injection vulnerabilities found in forms:")
            for result in form_results:
                print(f"Location: {result['location']}")
                print(f"Method: {result['method']}")
                print(f"Payload: {result['payload']}")
                print(f"Response snippet: {result['response']}\n")
        else:
            print("No vulnerabilities found in forms.")

        # Test GET parameters
        print("\nTesting GET parameters for HTML Injection...")
        param_results = test_parameters(url, params, PAYLOADS)
        if param_results:
            print("\nHTML Injection vulnerabilities found in GET parameters:")
            for result in param_results:
                print(f"Location: {result['location']}")
                print(f"Payload: {result['payload']}")
                print(f"Response snippet: {result['response']}\n")
        else:
            print("No vulnerabilities found in GET parameters.")

    except requests.RequestException as e:
        print(f"Failed to complete request: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python html_injection_checker.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    main(url)
