# WARNING: Use python >= 3.9, < 3.12.. version

## Setup Instructions

This project is designed to be cross-platform and supports Windows, macOS, and Linux environments. Please follow the appropriate instructions below to set up the development environment and run the project successfully.

Create data/output directory in the project folder, store your personal Groq API key in .env file

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/generative-cricket-commentary.git
cd generative-cricket-commentary
```

### 2. Environment Setup

#### For macOS / Linux Users

Modify this line of setup.sh script

```bash
/usr/local/bin/python3.11 -m venv venv
```

Use the path of python3.11 in your machine, you can find the path through command

```bash
where python3.11
```
or
```bash
which python3.11
```

Then run

```bash
[Your python3.11 path] -m venv venv
```

Execute the setup script to create a virtual environment and install dependencies:

```bash
./setup.sh
```

This script will:

* Create a Python virtual environment (`venv`)
* Activate the environment
* Install all required packages listed in `requirements.txt`

After running the script, activate the environment manually (if not already active):

```bash
source venv/bin/activate
```

#### For Windows Users

Set Python 3.11.X as their default python before running setup.bat
Run the batch script to set up the environment:

```bat
setup.bat
```

This script will:

* Create a Python virtual environment (`venv`)
* Activate the environment
* Install all required packages from `requirements.txt`

After setup, activate the environment with:

```bat
venv\Scripts\activate
```

### 3. Configuration

* Rename `.env.example` to `.env` and populate it with necessary environment variables, such as API keys and credentials.

### 4. Running the Application

Once the virtual environment is active, start the application using:

```bash
python main.py
```

### Additional Notes

* The `venv/` directory is excluded from version control via `.gitignore`.
* To update project dependencies, use the following command and commit the updated `requirements.txt`:

```bash
pip freeze > requirements.txt
```
