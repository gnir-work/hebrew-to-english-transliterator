# Hebrew Transliteration python wrapper example
This is a simple repo to demonstrate how to use the Hebrew Transliteration via  python wrapper.
The repo contains two main sections:
* `js_code` - a simple node package with installs the `hebrew-transliteration` package exposes it as a very simple cli tool.
* `python_code` - a simple python wrapper for the `hebrew-transliteration` package. The python code executes the js cli with `subprocess`.

## Installation
### Prerequisites
* [Node.js](https://nodejs.org/en/download/) - v12.18.3
* [Python](https://www.python.org/downloads/) - v3.8.5
* [pip](https://pip.pypa.io/en/stable/installing/) - v20.2.3

### Installation steps
1. Clone the repo
```bash
git clone git@github.com:charlesLoder/hebrew-transliteration.git
```
2. Install and build the node package
```bash
# From the root of the repository
cd js_code
npm install
npm run build
```
3. Validate that the js package works
```bash
# From the root of the repository
cd js_code
npm run execute -- "שלום עולם"
```
4. Validate that the python code works
```bash
# From the root of the repository
cd python_code
python usage_example.py "שלום עולם"
```