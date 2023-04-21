import os
import subprocess
import sys

JS_CODE_PATH = os.path.join('..', 'js_code', 'dist', 'main.js')


def transliterate_english_to_hebrew(text):
    return (subprocess.check_output(['node', JS_CODE_PATH, text])).decode('utf-8').strip()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python usage_example.py "text to transliterate"')
        sys.exit(1)
    output = transliterate_english_to_hebrew(sys.argv[1])
    print(output)
