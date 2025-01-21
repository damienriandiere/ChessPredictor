1. Create & activate a virtual environment
Create a virtual environment with the following command :
```bash
python -m venv virtualenv
```
Then, activate the virtual environment :
Windows :
```bash
.\virtualenv\Scripts\activate
```
Linux :
```bash
source virtualenv/bin/activate
```

Additional step : You can update requirements.txt. To do this, you must replace all == by >= in the file.
Windows:
```bash
(Get-Content requirements.txt) -replace '==', '>=' | Set-Content requirements.txt
``` 
Linux:
```bash
sed -i 's/==/>=/g' requirements.txt
```

Then, you can run the following commands :
```bash
pip install -r requirements.txt --upgrade
pip freeze > requirements.txt
```
