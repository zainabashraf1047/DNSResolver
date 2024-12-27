ResolvoNet
This project implements a DNS query resolver that handles both iterative and recursive DNS queries. It allows users to resolve domain names to their corresponding IP addresses using a simple web interface, and it can handle common DNS record types like A, AAAA, MX, CNAME, etc.

Features
Resolves iterative and recursive DNS queries.
Handles DNS record types: A, AAAA, MX, CNAME, etc.
Displays results on a web interface (HTML page).
Designed using Flask for the backend, with Python handling the logic for DNS resolution.
Prerequisites
Make sure you have the following installed on your machine:

Python 3.x: The backend is built with Python, and the required libraries are listed in the requirements file.
Flask: The web framework for building the server.
dnspython: A library to handle DNS resolution in Python.
Installation
Follow these steps to set up and run the project locally.

Clone the Repository

First, clone this repository to your local machine using Git:

bash
Copy code
git clone https://github.com/zainabashraf1047/dns-query-resolver.git
Navigate to the Project Folder

Change into the project directory:

bash
Copy code
cd dns-query-resolver
Create a Virtual Environment (Optional but recommended)

It's a good practice to create a virtual environment for Python projects. Run the following command to create a virtual environment:

bash
Copy code
python3 -m venv venv
Activate the virtual environment:

Windows:

bash
Copy code
venv\Scripts\activate
Linux/macOS:

bash
Copy code
source venv/bin/activate
Install Dependencies

Use pip to install the required dependencies:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file should include necessary libraries like Flask, dnspython, etc.

Example requirements.txt:

plaintext
Copy code
Flask==2.1.0
dnspython==2.1.0
Running the Project
Start the Flask Application

To run the DNS resolver, execute the following command in the project directory:

bash
Copy code
python app.py
This will start the Flask web server, typically accessible at:

arduino
Copy code
http://127.0.0.1:5000/
Access the Web Interface

Open your browser and go to:

Copy code
http://127.0.0.1:5000/
This will display the DNS query resolver interface where you can enter a domain name and select the query type (A, AAAA, MX, etc.).

How to Use the Project
Enter a Domain Name: On the home page, enter a domain name you want to resolve (e.g., www.google.com).

Select a DNS Query Type: You can choose from multiple DNS record types:

A: Resolves to an IPv4 address.
AAAA: Resolves to an IPv6 address.
MX: Mail exchange records.
CNAME: Canonical name for aliasing domain names.
Choose Query Type: Select whether you want to perform an iterative or recursive query.

View Results: Once you click the "Resolve" button, the results will be displayed on the page.

The iterative query shows the resolved IP address.
The recursive query will attempt to resolve the domain from root DNS servers and return the final IP.
Project Structure
graphql
Copy code
dns-query-resolver/
├── app.py                 # Flask application (backend)
├── templates/             # HTML templates for frontend
│   └── index.html         # Home page template
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
app.py: Contains the Flask backend code where DNS queries are processed.
templates/index.html: HTML page that provides the interface for users to input domain names and query types.
Code Explanation
DNS Query Resolver (Backend): The backend uses the dnspython library to handle the DNS query resolution. It performs iterative and recursive queries based on user input.
HTML Interface: The HTML frontend allows users to input their domain and select query options. Upon submission, the results are displayed directly on the page.
Possible Enhancements
Export Results: Add the option to export query results as CSV or JSON files.
Improved UI: Enhance the user interface with better styling and user feedback.
Error Handling: Add more robust error handling for invalid domain names or DNS failures.
Logging: Add logging functionality to keep track of DNS queries and responses.
