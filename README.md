# UberConnectivityApp
A python project using REST apis to book cabs available at your location

This project uses Flask framework in python to create APIs for searching, selecting and
booking cabs at your location.

The intended use is to use the uber-rides SDK but as the server access token is not available for all users,
the APIs do not work without the token.

So, mock data has been created in the folder /mock_data_jsons/ for these APIs, using the sample data from uber-documentation which can be found at:
https://developer.uber.com/docs

The dependencies for the code to work are listed in the requirements.txt file and can be installed with the command-

	pip install -r requirements.txt

Once the requirements have been installed, just run:

    python app.py

This will start the service.
The service is hosted on port 5000, so you can hit the homepage at localhost:5000/

A Dockerfile has also been added. To run in a docker environment, just follow the simple steps given below:
    
    Step 1:
    docker build -t uber_connectivity_app .
    
    Step 2:
    docker run --name uber_connectivity -p 5000:5000 -d uber_connectivity_app

    or, to view the interactive shell use:

    docker run --name uber_connectivity -p 5000:5000 -it uber_connectivity_app


You can also pull the image from docker-hub:

    docker pull ararora2/uber_connectivity_app:latest

Or to simply run  

    docker run -p 5000:5000 ararora2/uber_connectivity_app:latest

