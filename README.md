# Furniture Creator (Technical challenge)
This command line application for a simplified furniture production facility is
created for a technical challenge. It can be run in a Docker container and
accepts *product designs* and *parts* as input through standard input (see
**Usage** below) and outputs *products* whenever one can be created from the
current parts in stock.  

For the full challenge, see [CHALLENGE.md](CHALLENGE.md).

## Requirements
You will need to have Docker installed to run this application as is intended in
a Docker container. Although it can be run without Docker.  
Required packages will be installed during the Docker build process.  

## Usage
Build the Docker image:  

    $ docker build -t furniturecreator .

Run the image, supplying a file as input:  

    $ cat samples/long1.txt | docker run -i --rm furniturecreator

Or run the image to paste (or type) in the input below. Close by
pressing `Ctrl+D` (possibly twice):  

    $ docker run -it --rm furniturecreator

Run the tests (*unittest*: unit testing framework; *mypy*: static type checker)  

    $ docker run --rm furniturecreator python -m unittest
    $ docker run --rm furniturecreator mypy furniturecreator

### Without Docker

If you want to run furniture creator without Docker, you will need to have
Python ^3.8 installed. Install required python packages with pip:

    $ pip install -r requirements.txt

Supplying a file as input:  

    $ cat samples/long1.txt | python -m furniturecreator

Run tests:

    $ python -m unittest
    $ mypy furniturecreator

### Input
The input stream should follow this structure:  
```xml
<product_design1>
<product_design2>
<empty_line>
<part1>
<part2>
<part3>
...
```  
**Example:**  
```
[Table]S2a5c7j20
[Table]L9d7g8u30

aS
dL
gL
uL
jS
...
```

### Output
The application outputs products whenever one of the provided *product designs*
can be created from the current parts in stock.  

## License
This project is under the MIT license. See `LICENSE` for more information.  
