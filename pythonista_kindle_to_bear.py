import appex
import webbrowser
import urllib

import kindle_export_parser.converter as converter


def postToBear(text):
    text_encoded = urllib.parse.quote(text)

    # see: https://bear.app/faq/X-callback-url%20Scheme%20documentation/#create
    bear_url = 'bear://x-callback-url/create?text={}'.format(text_encoded)

    webbrowser.open(bear_url)


def main():
    if not appex.is_running_extension():
        print('Running in Pythonista app, using test data...\n')
        html_file = 'tests/files/sample-export-simple.html'
    else:
        html_file = appex.get_text()

    text = converter.convert_kindle_html_to_md(html_file)

    postToBear(text)


if __name__ == '__main__':
    main()

