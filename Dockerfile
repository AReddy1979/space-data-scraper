FROM python:3
ADD data_fetcher.py /
ADD space_scraper_CLI.py /
ADD file_parser.py /
ADD SolarFlareFetcher.py /
ADD alerts_backend.py /
RUN pip install requests
RUN pip install beautifulsoup4
ENTRYPOINT ["python", "space_scraper_CLI.py"]