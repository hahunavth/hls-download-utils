#!/bin/bash

VERSION=124.0.6367.91

wget https://storage.googleapis.com/chrome-for-testing-public/$VERSION/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
rm chromedriver-linux64.zip

wget https://storage.googleapis.com/chrome-for-testing-public/$VERSION/linux64/chrome-linux64.zip
unzip chrome-linux64.zip
rm chrome-linux64.zip
