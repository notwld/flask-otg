# Flask On The Go
A Flask Boilerplate for quick development which uses pyngrok for exposing the local server to the internet.

## Installation
- Clone the repository
- Install the requirements
```bash
pip install -r requirements.txt
```
- Create a ngrok account and get the authtoken from [here](https://dashboard.ngrok.com/get-started/your-authtoken)
- Add the authtoken to the ngrok.yml file
```bash
ngrok config add-authtoken TOKEN
```

- Run the app
```bash
python app.py
```

## Usage
1. Open the ngrok dashboard in the browser (you can get the url from the terminal)
2. Copy the ngrok url and paste it in the browser
3. You can also use the ngrok url in your mobile app

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.