from webScraper import WebScraper
import sys

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
        tags = sys.argv[2]
        className = sys.argv[3]
    else:
        url = 'http://familyguy.fox-fan.tv/'

    webScr = WebScraper(url)
    webScr.get_pages()
    webScr.parse()
        
  

if __name__ == '__main__':
    main()
