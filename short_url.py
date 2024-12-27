# Mouad Garroud
import requests
def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text 
    else:
        return None  
def main():
    print("URL Shortener using TinyURL API")
    while True:
        long_url = input("Enter the long URL to shorten (or 'exit' to quit): ").strip()
        if long_url.lower() == 'exit':
            print("Exiting URL Shortener.")
            break
        shortened_url = shorten_url(long_url)
        if shortened_url:
            print(f"Shortened URL: {shortened_url}")
        else:
            print("Error occurred while shortening the URL.")
if __name__ == "__main__":
    main()
