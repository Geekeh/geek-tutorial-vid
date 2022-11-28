import cloudscraper

class main(object):
    def __init__(self):

        self.scraper = cloudscraper.create_scraper()
        print(self.credits())

    def credits(self):
        return self.scraper.get("https://geekis.dev/").json()['skidder']

if __name__ == "__main__":
    main()