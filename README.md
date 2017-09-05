# UnB's moodle scrapper

This project is a small scrapper who takes pdf's files from the courses who you're subscribed at the UnB's moodle (http://aprender.unb.br)

## Getting Started

Clone this repository on your machine, create 2 directories ('file' and 'payload'), and after this
 to go to the 'payload' directory:

```
mkdir file && mkdir payload && cd payload
```

and create a file named 'payload.py' with a python dictionary following this model (with your login information):

```
payload = {
	"username": "YOUR_CPF",
	"password": "YOUR_PASSWORD",
}
```
and run the file 'pegarApre.py'

```
python3 pegarApre.py
```

### Prerequisites

You only need the BeautifulSoup4 package to run this scrapper

```
pip install beautifulsoup4
```
## Built with

[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - The scrapping package used

## Contributing

Just send an issue.

## Author

* **Jefferson Viana** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
Special thanks to [Seninha](https://github.com/Seninha) who inspired me to make this project.
