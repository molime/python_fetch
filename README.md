This repository is a simple Flask app with a local SQL DB

To run the app you should have Docker installed in your computer.
The app has a simple Dockerfile with the necessary instructions to run the app

Start Docker on your local computer and follow these instructions:

1. Build the image:

    ```
    docker build --tag python-fetch .
    ```

2. Run the image:

    ```
    docker run --publish 5000:5000 python-fetch
    ```

This will start the app in a Docker container that can be reached through port 5000. The following is the correct way to send requests to the app:

http://127.0.0.1:5000/receipts/process

http://127.0.0.1:5000/receipts/1/points