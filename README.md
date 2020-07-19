# Word Permutation 

This repo is a simple dockerized python application that uses recursion to return: 

- number of possible word combinations 
- all unique word combinations 

## Dependencies
Before you start, you first will need the following dependencies installed:

-   [Install Docker](http://docs.docker.com/installation/)
-   [Install Docker Compose](http://docs.docker.com/compose/install/)

## Build & Run  

First step is to build: start by typing in your terminal the following command: 
(remember to be in the project directory)

    docker build -t permutations .

Then to get our container running: 

    docker run -it permutations 

(here we have to add the -it command together, we need to make it interactible so you can enter whatever word you would like to see the combinations)


## License

MIT License

Copyright (c) 2019 carlalmadureira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
