
# Web Scraping with BeautifulSoup

This project demonstrates how to scrape product information from a web page using Python's `requests` library and `BeautifulSoup` for HTML parsing.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup4 library

## Installation

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

Replace the `url` variable with the link of the product you want to scrape.

```python

url="https://www.game.es/ACCESORIOS/AURICULARES/PC-GAMING/GAME-HX500-RGB-71-PRO-GAMING-HEADSET-PC-PS4-AURICULARES-AURICULARES-GAMING/169628"

headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
