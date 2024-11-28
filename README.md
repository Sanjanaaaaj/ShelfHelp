SHELF HELP
This application is made using python, flask and html. 
Originally hosted on vercel platform 
Find the link below:
(https://shelf-help.vercel.app/)

Features : 
It gives you a catalogue of books which are organized based on genre 
It also allows you to get recommendations by genres .
Data is scraped from Google reads (Sanjana J's account) 
Used pickle files instead of a typical database.
Html with jinja templates for frontend has been used.
The application runs on flask on backend due to its efficient and simple working with python. 


(Steps to deploy on vercel : 
Prerequisites- Make sure project is structured properly i.e. main application, dependencies , templates etc . 
Include a vercel.json file for vercel to access your project .
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```
Create a repository on github (recommended)
Login to vercel account -> new project -> import repository -> deploy
Vercel will provide a public URL once deployed : https://shelf-help.vercel.app/ )



How to run this application on your browser:

Ensure you have the following installed on your system:
- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)

Clone the Repository 
   Open a terminal and run the following command to clone the repository:
  ```bash
     git clone https://github.com/Sanjanaaaaj/ShelfHelp.git
  ```
Install dependencies:
```python
pip install -r requirements.txt
```
and run the application using:
``` python
    python app.py
```
Open your web browser and navigate to 
```html
http://127.0.0.1:5000/
```




