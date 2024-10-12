# Basic "Hello" web service based on SOAP

## Installation guide
```bash
pip install -r requirements.txt
```

## Running the server
```bash
python3 ./soap_server.py
```

## Checking the WSDL of the service
Go to [http://127.0.0.1:8000/hello?wsdl](http://127.0.0.1:8000/hello?wsdl).

Alternatively, execute the follwing cURL command:
```bash
curl http://127.0.0.1:8000/hello?wsdl
```

## Using the service
You can use the valid request `request.xml` in this repository:
```bash
curl -i --request POST \
    --url http://127.0.0.1:8000/hello \
    --header "Content-Type: application/xml" \
    --data @./request.xml
```

You'll get an output similar to this one (this one has been formatted for readability):
```xml
HTTP/1.0 200 OK
Date: Sun, 06 Oct 2024 12:53:16 GMT
Server: WSGIServer/0.2 CPython/3.10.1
Content-Type: text/xml; charset=utf-8
Content-Length: 312

<?xml version='1.0' encoding='UTF-8'?>
<soap11env:Envelope xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="spyne.examples.helloworld">
    <soap11env:Body>
        <tns:say_helloResponse>
            <tns:say_helloResult>Hello, John</tns:say_helloResult>
        </tns:say_helloResponse>
    </soap11env:Body>
</soap11env:Envelope>
```

You can also send a request which is missing the mandatory parameter `name` using `incomplete_request.xml` as your data:
```bash
curl -i --request POST \
    --url http://127.0.0.1:8000/hello \
    --header "Content-Type: application/xml" \
    --data @./incomplete_request.xml
```

You'll get something similar to this:
```xml
HTTP/1.0 500 Internal Server Error
Date: Sun, 06 Oct 2024 12:55:14 GMT
Server: WSGIServer/0.2 CPython/3.10.1
Content-Type: text/xml; charset=utf-8
Content-Length: 488

<?xml version='1.0' encoding='UTF-8'?>
<soap11env:Envelope xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/">
    <soap11env:Body>
        <soap11env:Fault>
            <faultcode>soap11env:Client.SchemaValidationError</faultcode>
            <faultstring>:1:0:ERROR:SCHEMASV:SCHEMAV_ELEMENT_CONTENT: Element '{spyne.examples.helloworld}say_hello': Missing child element(s). Expected is ( {spyne.examples.helloworld}name ).</faultstring>
            <faultactor></faultactor>
        </soap11env:Fault
    ></soap11env:Body>
</soap11env:Envelope>
```
