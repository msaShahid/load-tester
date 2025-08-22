Here's an updated version of the **README** that includes clear instructions for **cloning the repository** and then setting up and running Locust for load testing, step-by-step:



# **Load Testing with Locust**

This repository provides the steps to set up **Locust** in a Python virtual environment for load testing a website. It will guide you through setting up a virtual environment, installing necessary dependencies, configuring environment variables, and running load tests on your site.



### **Table of Contents**

1. [Cloning the Repository](#cloning-the-repository)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)

   * [Step 1: Create and Activate a Virtual Environment](#step-1-create-and-activate-a-virtual-environment)
   * [Step 2: Install Locust and python-dotenv](#step-2-install-locust-and-python-dotenv)
   * [Step 3: Create .env File](#step-3-create-env-file)
   * [Step 4: Generate requirements.txt](#step-4-generate-requirementstxt)
   * [Step 5: Run Locust from the Virtual Environment](#step-5-run-locust-from-the-virtual-environment)
   * [Step 6: Deactivate the Virtual Environment](#step-6-deactivate-the-virtual-environment)
4. [Folder Structure](#folder-structure)
5. [Additional Notes](#additional-notes)
6. [Troubleshooting](#troubleshooting)




### **Cloning the Repository**

To get started, clone this repository to your local machine. You can use the following command:

```bash
git clone https://github.com/your-username/load-testing-locust.git
```

Replace `your-username` with your GitHub username or the appropriate username for the repository.

Once cloned, navigate into the project folder:

```bash
cd load-testing-locust
```

Now, you're ready to set up the virtual environment and start the load testing.



### **Prerequisites**

Before you begin, ensure the following:

* **Python 3.x** installed on your machine.
* **Git** installed (for cloning the repo).
* Basic understanding of Python and terminal usage.

### **Setup Instructions**

#### **Step 1: Create and Activate a Virtual Environment**

Create a **virtual environment** to isolate the project’s dependencies.

Run the following commands to create and activate the virtual environment:

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Once activated, your terminal prompt will display `(venv)` indicating that the virtual environment is active.



#### **Step 2: Install Locust and python-dotenv**

With the virtual environment active, install **Locust** (for load testing) and **python-dotenv** (for loading environment variables).

Run the following command:

```bash
pip install locust python-dotenv
```

This installs Locust and the dotenv library inside your virtual environment.



#### **Step 3: Create .env File**

Create a `.env` file in the project directory to store your website URL and other configuration settings.

Example `.env` file:

```
HOST_URL=https://yourwebsite.com
```

Make sure to replace `https://yourwebsite.com` with the actual URL of the website you want to load test.

#### **Step 4: Generate requirements.txt**

To make it easier for others to set up the environment on their machine, generate a `requirements.txt` file that lists all installed dependencies.

Run:

```bash
pip freeze > requirements.txt
```

This will create a `requirements.txt` file in your project folder.



#### **Step 5: Run Locust from the Virtual Environment**

Now you are ready to start the load testing with Locust.

In your terminal, run:

```bash
locust
```

This will start a web UI at `http://localhost:8089`. In the UI, you can configure:

* **Number of users to simulate** (e.g., 100 users)
* **Spawn rate** (e.g., 10 users/sec)
* **Host**: The base URL (e.g., `https://yourwebsite.com`)

Click **Start swarming** to begin the load test.



#### **Step 6: Deactivate the Virtual Environment**

Once you're done with the load testing, deactivate the virtual environment:

```bash
deactivate
```

This will return you to your global Python environment.


### **Folder Structure**

Here’s what your project directory should look like:

```
/load-testing-locust
  ├── locustfile.py        # Locust load testing script
  ├── .env                 # Environment variables (e.g., website URL)
  ├── .venv/               # Virtual environment folder
  ├── requirements.txt     # List of Python dependencies
  └── README.md            # This README file
```

### **Additional Notes**

* **Environment Variables**: You can store other configurations such as authentication tokens, API keys, or specific paths in the `.env` file.

* **Scaling Tests**: If you want to simulate higher traffic, increase the **number of users** and **spawn rate** in the Locust web UI. For example, simulating 1,000 users with a spawn rate of 50 users/sec will test the website’s performance under more significant load.

* **Monitoring Performance**: Use the Locust web interface to monitor:

  * Response times
  * Requests per second (RPS)
  * Failure rates
  * Percentile-based response time distributions

### **Troubleshooting**

* **Locust Not Starting**: Ensure that your virtual environment is activated and that all dependencies are installed. You can run `pip install -r requirements.txt` to ensure everything is up-to-date.

* **404 or Connection Errors**: Double-check the `HOST_URL` in your `.env` file to make sure it's correct. Verify that the target website is running and accessible.

* **Slow Response Times**: If you encounter high latency or errors, consider profiling the server or checking for bottlenecks in your backend, databases, or third-party services.



