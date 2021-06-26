from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import logging, json, os

app = Flask(__name__)

UPLOAD_FOLDER = f"{os.path.dirname(os.path.realpath(__file__))}/logs"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        with open("get_logger.json", 'r') as log_num:
            log_ = json.load(log_num)
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=f'logs/{log_["log"]}.log',
                        filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO) 
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
        logging.info(f"POST request,\nPath: {request.path}\nHeaders:\n{request.headers}\n")
        replacer = {"log": str(int(log_["log"]) + 1)}
        with open("get_logger.json", 'w') as log_replace:
            json.dump(replacer, log_replace)
        return render_template("login.html")    
    else:
        for handler in logging.root.handlers[:]: # Deleting Previous Basic Config from the logger
            logging.root.removeHandler(handler)
        with open("get_logger.json", 'r') as log_num: # Opening the json file in which log file details are stored.
            log_ = json.load(log_num) # Storing Filename in Variable
        logging.basicConfig(level=logging.DEBUG, # Setting up the Basic Config of the logger
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', # Formatting the logger
                        datefmt='%m-%d %H:%M', # Assigning Date Operators
                        filename=f'logs/{log_["log"]}.log', # Setting up the filename of the log file.
                        filemode='w') # Filetype changing to writable format
        console = logging.StreamHandler() # Initialzing Console/Terminal Stream Handler
        console.setLevel(logging.INFO) # Setting the level to INFO
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s') # Formatting the Console Logger       
        console.setFormatter(formatter) # Applying the format
        logging.getLogger().addHandler(console)  # Setting the handler to the logger
        logging.info(f"GET request,\nPath: {request.path}\nHeaders:{request.headers}")
        # logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(request.path), str(request.path))
        replacer = {"log": str(int(log_["log"]) + 1)}
        with open("get_logger.json", 'w') as log_replace:
            json.dump(replacer, log_replace)
        return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        with open("get_logger.json", 'r') as log_num:
            log_ = json.load(log_num)
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=f'logs/{log_["log"]}.log',
                        filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO) 
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
        logging.info(f"POST request,\nPath: {request.path}\nHeaders:\n{request.headers}\nContent: \nEmail: {email}\nPassword: {password}\n")
        replacer = {"log": str(int(log_["log"]) + 1)}
        with open("get_logger.json", 'w') as log_replace:
            json.dump(replacer, log_replace)
        with open("data/users.json", 'r') as users_:
            users = json.load(users_)
        emails = users['email']
        passwords = users['password']
        for _email, _password in zip(emails, passwords):
            if email == _email and password == _password:
                return render_template("index.html")
        return render_template("login.html", wrong=True)
    else:
        for handler in logging.root.handlers[:]: # Deleting Previous Basic Config from the logger
            logging.root.removeHandler(handler)
        with open("get_logger.json", 'r') as log_num: # Opening the json file in which log file details are stored.
            log_ = json.load(log_num) # Storing Filename in Variable
        logging.basicConfig(level=logging.DEBUG, # Setting up the Basic Config of the logger
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', # Formatting the logger
                        datefmt='%m-%d %H:%M', # Assigning Date Operators
                        filename=f'logs/{log_["log"]}.log', # Setting up the filename of the log file.
                        filemode='w') # Filetype changing to writable format
        console = logging.StreamHandler() # Initialzing Console/Terminal Stream Handler
        console.setLevel(logging.INFO) # Setting the level to INFO
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s') # Formatting the Console Logger       
        console.setFormatter(formatter) # Applying the format
        logging.getLogger().addHandler(console)  # Setting the handler to the logger
        logging.info(f"GET request,\nPath: {request.path}\nHeaders:{request.headers}")
        # logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(request.path), str(request.path))
        replacer = {"log": str(int(log_["log"]) + 1)}
        with open("get_logger.json", 'w') as log_replace:
            json.dump(replacer, log_replace)
        return render_template("login.html")

@app.route("/submit-file", methods=["GET", "POST"])
def file_submit():
    if request.method == "POST":
        file = request.files['file']
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        with open("get_logger.json", 'r') as log_num:
            log_ = json.load(log_num)
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=f'logs/{log_["log"]}.log',
                        filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO) 
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
        filename = file.filename
        splitter = filename.split(".") # Extension breaking
        fileformat = splitter[1]
        logging.info(f"POST request,\nPath: {request.path}\nHeaders:\n{request.headers}\nFilename: {filename}\n")
        if fileformat == "6" or fileformat == "0" or fileformat == "1" or fileformat == "2" or fileformat == "3" or fileformat == "4" or fileformat == "5" or fileformat == "7" or fileformat == "8" or fileformat == "9":
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f"{log_['log']}.zip")))
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f"{log_['log']}.{fileformat}")))
        replacer = {"log": str(int(log_["log"]) + 1)}
        with open("get_logger.json", 'w') as log_replace:
            json.dump(replacer, log_replace)
        return render_template("index.html", saved=True)
    else:
        for handler in logging.root.handlers[:]: # Deleting Previous Basic Config from the logger
            logging.root.removeHandler(handler)
        with open("get_logger.json", 'r') as log_num: # Opening the json file in which log file details are stored.
            log_ = json.load(log_num) # Storing Filename in Variable
        logging.basicConfig(level=logging.DEBUG, # Setting up the Basic Config of the logger
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', # Formatting the logger
                        datefmt='%m-%d %H:%M', # Assigning Date Operators
                        filename=f'logs/{log_["log"]}.log', # Setting up the filename of the log file.
                        filemode='w') # Filetype changing to writable format
        console = logging.StreamHandler() # Initialzing Console/Terminal Stream Handler
        console.setLevel(logging.INFO) # Setting the level to INFO
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s') # Formatting the Console Logger       
        console.setFormatter(formatter) # Applying the format
        logging.getLogger().addHandler(console)  # Setting the handler to the logger
        logging.info(f"GET request,\nPath: {request.path}\nHeaders:{request.headers}")
        # logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(request.path), str(request.path))
        replacer = {"log": str(int(log_["log"]) + 1)}
        with open("get_logger.json", 'w') as log_replace:
            json.dump(replacer, log_replace)
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        with open("get_logger.json", 'r') as log_num:
            log_ = json.load(log_num)
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=f'logs/{log_["log"]}.log',
                        filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO) 
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
        logging.info(f"POST request,\nPath: {request.path}\nHeaders:\n{request.headers}\nContent: \nName: {name}\nEmail: {email}\nPassword: {password}\n")
        replacer = {"log": str(int(log_["log"]) + 1)}
        with open("get_logger.json", 'w') as log_replace:
            json.dump(replacer, log_replace)
        with open("data/users.json", 'r') as user_handler:
            users = json.load(user_handler)
        _name = users['name']
        _email = users['email']
        _password = users['password']
        if email in _email:
            return render_template("register.html", wrong=True)
        _name.append(name)
        _email.append(email)
        _password.append(password)
        with open("data/users.json", 'w') as entrier:
            json.dump(users, entrier)
        return render_template("index.html")
    else:
        for handler in logging.root.handlers[:]: # Deleting Previous Basic Config from the logger
            logging.root.removeHandler(handler)
        with open("get_logger.json", 'r') as log_num: # Opening the json file in which log file details are stored.
            log_ = json.load(log_num) # Storing Filename in Variable
        logging.basicConfig(level=logging.DEBUG, # Setting up the Basic Config of the logger
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', # Formatting the logger
                        datefmt='%m-%d %H:%M', # Assigning Date Operators
                        filename=f'logs/{log_["log"]}.log', # Setting up the filename of the log file.
                        filemode='w') # Filetype changing to writable format
        console = logging.StreamHandler() # Initialzing Console/Terminal Stream Handler
        console.setLevel(logging.INFO) # Setting the level to INFO
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s') # Formatting the Console Logger       
        console.setFormatter(formatter) # Applying the format
        logging.getLogger().addHandler(console)  # Setting the handler to the logger
        logging.info(f"GET request,\nPath: {request.path}\nHeaders:{request.headers}")
        # logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(request.path), str(request.path))
        replacer = {"log": str(int(log_["log"]) + 1)}
        with open("get_logger.json", 'w') as log_replace:
            json.dump(replacer, log_replace)
        return render_template("register.html")

app.run(port=8080, debug=True)    