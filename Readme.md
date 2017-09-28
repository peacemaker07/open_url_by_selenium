Open URL by selenium
====

Open URL in text in Chrome and output Chrome's console log

## Description

## Demo

## Requirement

* chromedriver

## Usage

* Move

```
$ cd open_url_by_selenium
```

* Make input file (one URL per line)

```
$ vi exsample_url.txt
```
```exsample_url.txt
https://www.yahoo.co.jp/
https://www.google.co.jp/
・
・
・
```

* Activate

```
$ source env/bin/activate

```

* Run

```
$ python open_url_with_output_console_log exsample_url.txt > log.txt
```

## Install

```
$ brew install chromedriver
$ git clone https://github.com/peacemaker07/open_url_by_selenium.git
$ cd open_url_by_selenium
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Contribution

## Licence

## Author

[chinoppy](https://github.com/peacemaker07/)
