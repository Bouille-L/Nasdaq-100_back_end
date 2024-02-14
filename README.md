# Nasdaq-100 ETF Explorer Web App
## Objective:
The objective of this project is to develop a web application that provides users with comprehensive information and interactive charts for Nasdaq-100 ETF (TQQQ, QQQ, SQQQ). The application will empower users to make informed investment decisions and track ETF performance.

The project includes the development of a user-friendly web application that aggregates and displays real-time data, interactive charts, news, and educational content related to Nasdaq-100 ETFs (TQQQ, QQQ, NASDAQ-100, SQQQ).
Exclusions: The project does not cover the development of a mobile application or trading functionality.

Such an application can provide significant value to investors, traders, and anyone interested in the Nasdaq-100 index and its constituent ETFs (TQQQ, QQQ, NASDAQ-100, SQQQ).  It can help users make informed investment decisions and track the performance of these ETFs. While there are existing financial data platforms, creating a new, user-friendly, and innovative interface that specifically focuses on Nasdaq-100 ETFs can offer a unique perspective and features, setting it apart from generic financial websites.
                                                                                           
                                                                   
                                                                                           
                                                                                           
## Architectural Principles and Approach:
Design Philosophy: The architecture is crafted with an emphasis on modularity, scalability, and responsiveness, aiming to deliver a smooth user experience when accessing financial data.

Architectural Style: The application embraces a client-server model, ensuring a distinct separation between the backend (utilizing Django REST) and the frontend (powered by ReactJS).
Frameworks and Technologies:
- Django REST Framework: Selected for its effectiveness and robustness in managing RESTful API services, which are essential for delivering real-time financial data.
- ReactJS: Chosen for the frontend development to facilitate a dynamic and interactive user interface. Its component-based structure enables efficient updates and the rendering of dynamic elements, such as charts and news feeds.
- Chart.js: Employed to provide interactive and responsive chart visualizations, significantly enhancing the data presentation capabilities of the application.

High-Level Structure: The backend is tasked with handling API calls, data processing, and storage operations (such as archiving user messages). The frontend is designed to effectively display data through both static and dynamic components.

                                                                                        

# Nasdaq-100_back_end repository (folder) :
## Introduction :
In this repository, you'll find the backendof the Nasdaq-100 ETF Explorer Application. Our backend is built using Django REST Framework, Chosen for its robustness and efficiency in handling RESTful API services, crucial for serving real-time financial data. We utilize HTTP requests to feed the front end with stock data and market news.

## Overview of system Component in Backend (Django REST) :
This section provides an overview of all components of the back end of the  NASDAQ-100 ETF Explorer web application, each playing a specific role in the application's functionality.
Backend (Django REST Framework): Manages server-side logic, data processing, API management, and database interactions, this is its components:
*	Admin.py: used to log in by admin to check message received from users via contact us form located in frontend.
*	SendEmailAPI_View.py: designed to handle the submission of contact messages from users. It primarily deals with processing 'Contact Us' form submissions from the frontend of the NASDAQ-100 ETF Explorer.
*	Model.py: serves as the data structure for storing user-submitted contact messages. It's an essential component for managing user feedback, inquiries, and communications received through the NASDAQ-100 ETF Explorer's contact form.
*	Views.py: it is responsible for fetching the latest market news  and stock price data. It serves as a bridge between the external API and the frontend of the NASDAQ-100 ETF Explorer.
* Serializers.py: responsible for defining how news data is serialized and deserialized. It plays a crucial role in converting complex data types, like news content fetched from an external API, into Python data types that can then be easily rendered into JSON or XML format for the frontend.
* Api_url.py: Manages the specific URLs for the various API endpoints provided by the application.
* Setting.py: Contains configurations for the Django project, including database settings, middleware, etc.
*	Urls.py: Defines the URL routes for the web application.

## External API (alphavantage.com): Supplies the application with real-time stock prices, which are crucial for the ETF information and chart components.
API Documentation : https://www.alphavantage.co/documentation/

## External API (api.marktaux.com): Provides up-to-date market news, ensuring users have access to the latest financial news relevant to NASDAQ-100 ETFs.
API Documentation : https://www.thenewsapi.com/documentation

## UML Component Diagram : 
To review the UML component diagram, please visit the following repository : https://github.com/Bouille-L/Web-App-UML-Diagram.git

# Installation Instructions: 
This guide provides step-by-step instructions for setting up the backend of the Nasdaq 100 ETF Explorer Project, which utilizes Django REST Framework.

## Prerequisites
Before you begin, ensure you have the following installed on your system:

* Python (3.8 or later)
* pip (Python package manager)
* virtualenv (optional, but recommended for creating isolated Python environments)

Setup
Clone the Repository

First, clone the repository to your local machine using Git:


git clone https://github.com/Bouille-L/Nasdaq-100_back_end.git
cd Nasdaq-100_back_end```

## Create and Activate a Virtual Environment (Optional)

It's recommended to create a virtual environment to keep dependencies required by different projects separate:

On Windows:
```
python -m venv venv
.\venv\Scripts\activate
```

On macOS and Linux:
```
python3 -m venv venv
source venv/bin/activate
Install Dependencies
```

## With the virtual environment activated, install the required packages using pip:

```
pip install -r requirements.txt
```

## Run the Development Server

Start the Django development server:
```
python manage.py runserver
Your backend should now be running locally on http://localhost:8000/.
```



