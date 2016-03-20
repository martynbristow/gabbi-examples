# HTTP Testing with Gabbi by Example

[Gabbi](http://gabbi.readthedocs.org) is a simple HTTP testing framework developed in Python, with tests written as simple YAML file, these tests can be extended with Python setUp and tearDown methods.

I'm developing a Web Application, with a series of pages presenting data and reports, and a simple REST API.
I needed to develop a set of functional end-to-end tests and learned about gabbi from a colleague, but the documentation is sparese, so I have written a tutorial and some examples.
The web app I have written is a POS manager [MyPOS](http://martynbristow.co.uk/wordpress/portfolio/mypos/) for the open source solutions ChromisPOS & UnicentaPOS.

I hope they are of use to you, if I've missed something then please let me know, or submit a pull request.
[Gabbi HTTP Testing](http://martynbristow.co.uk/wordpress/blog/gabbi-http-testing/)

This tutorial and examples are written to be fairly accesible, I don't assume you have much software testing experience or knowledge of Python to get started, but you will need to be famililar with working on the command line.

## Contents
 * samples - Some very simple tests
 * tutorials - This is an empty folde for you to store your tutorials in
 * api - Minimal set of tests to run against an API

## Setting Up
First you need to install the Gabbi package, the easiest way is through pip:
`pip install gabbi --user`

## Tutorial
### Test
We want to peform the following test:
Check that the website [example.com](http://example.com) is a valid website.
We want to open the following url and check that we are given a HTTP Success that the page exists
### Manual Test
The following command will work on any linux or OSX system (with curl installed), you can alternatly just use a browser.
`curl -v -oexample.com example.com`
HTTP Headers
```
> GET / HTTP/1.1
> Host: example.com
> User-Agent: curl/7.43.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Accept-Ranges: bytes
< Cache-Control: max-age=604800
< Content-Type: text/html
< Date: Sun, 20 Mar 2016 01:55:31 GMT
< Etag: "359670651"
< Expires: Sun, 27 Mar 2016 01:55:31 GMT
< Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
< Server: ECS (ewr/15BD)
< Vary: Accept-Encoding
< X-Cache: HIT
< x-ec-custom-error: 1
< Content-Length: 1270
< 
```
We performed a GET on example.com
```
> GET / HTTP/1.1
> Host: example.com
```
The responce included:
 * HTTP/1.1 200 OK
 * Content-Type: text/html
 * Content-Length: 1270

### Simple Tests
Ok, so we know example.com is valid, why should I continue reading:
1. That was a very simple check, opening a webpage
2. We didn't actually test anything
3. It isn't very automated

So lets write and run a simple HTTP Test with gabbi on the same resource
In the folder tutorials, create a new file example.yaml, this will be our first test.
```
# Test 'example.com' is working ok
tests:

- name: <test name>
  desc: <test description>
  method: <HTTP Method>
  url: <URL>
  status: <Response Status>
```
### Running Tests
Gabbi tests can be run with
gabbi-run < <testfile>.yaml
python <testrunner>.py
### Testing Google

## Recipes
### Authentication

