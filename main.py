import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    params = {"long_url": link}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    params = {"units": -1, "unit": "month"}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(bitly_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Сокращает ссылку и показывает количество кликов по ней')
    parser.add_argument('--url', type=str, help='Введите ссылку')
    args = parser.parse_args()
    token = os.environ['BITLY_TOKEN']
    parsed_url = urlparse(args.url)
    parsed_url = f'{parsed_url.netloc}{parsed_url.path}'
    try:
        if is_bitlink(token, parsed_url):
            print(count_clicks(token, parsed_url))
        else:
            print(shorten_link(token, args.url))
    except requests.exceptions.HTTPError as error:
        print(error)


if __name__ == "__main__":
    main()
