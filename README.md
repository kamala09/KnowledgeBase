# AWS Knowledge Base Deletion Script

<!-- This script deletes all AWS knowledge bases in Amazon Bedrock where the status is `Failed`. It uses the Boto3 library to interact with AWS and the `python-dotenv` library to manage environment variables from a `.env` file. -->

## Prerequisites

<!-- 1. **Python**: Make sure you have Python installed on your machine. This script is compatible with Python 3.x.
2. **Boto3**: The AWS SDK for Python. Install it using pip if you don't already have it:
    ```bash
    pip install boto3
    ```
3. **python-dotenv**: A library to load environment variables from a `.env` file. Install it using pip:
    ```bash
    pip install python-dotenv
    ``` -->

## Setup
<!-- 
1. **Clone the Repository**: Clone this repository to your local machine.

2. **Create a `.env` file**: In the root directory of your project, create a file named `.env` and add your AWS credentials and region:
    ```plaintext
    AWS_ACCESS_KEY_ID=your_access_key_id
    AWS_SECRET_ACCESS_KEY=your_secret_access_key
    AWS_DEFAULT_REGION=your_default_region
    ```

3. **Update the `.env` File**: Replace `your_access_key_id`, `your_secret_access_key`, and `your_default_region` with your actual AWS credentials and the default region for your resources. -->

## Usage
<!-- 
1. **Run the Script**: Execute the script to delete the knowledge bases with a `Failed` status:
    ```bash
    python your_script_name.py -->
    ```

### Script Overview
<!-- 
- **Environment Variables**: The script loads AWS credentials and region information from the `.env` file.
- **Boto3 Client Initialization**: Initializes the Boto3 Bedrock client using the loaded environment variables.
- **Function Definitions**:
    - `delete_knowledge_base(kb_id)`: Deletes the specified knowledge base.
    - `list_knowledge_bases()`: Lists all knowledge bases.
    - `delete_failed_knowledge_bases()`: Deletes all knowledge bases with a status of `Failed`. -->
