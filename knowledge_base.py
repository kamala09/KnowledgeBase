# ******************************************************************************************
# * Name: knowledge_base                                                                    *
# * Description: knowledge Base delete base on status                                       *
# * AuthurName           Version              Date               Ticket Number              * 
# * Kamalakanta           V1.0               15-07-2024           HR1- 87                   *
# *******************************************************************************************/

import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError

# Load environment variables from .env file
load_dotenv()
# Initialize clients for all bedrock related services
# services = ['bedrock', 'bedrock-agent', 'bedrock-agent-runtime', 'bedrock-runtime']
# for service in services:
#     print(f"Methods for {service}:")
#     client = boto3.client(service)
#     print(dir(client))
#     print("\n")
# Initialize the bedrock-agent client
client = boto3.client('bedrock-agent')

# Function to delete a knowledge base
def delete_knowledge_base(kb_id):
    try:
        response = client.delete_knowledge_base(knowledgeBaseId=kb_id)
        print(f"Deleted knowledge base {kb_id}")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'ResourceNotFoundException':
            print(f"Knowledge base {kb_id} not found.")
        else:
            print(f"Error deleting knowledge base {kb_id}: {error_code} - {e}")
    except Exception as e:
        print(f"Error deleting knowledge base {kb_id}: {e}")

# Function to list all knowledge bases with pagination
def list_all_knowledge_bases():
    knowledge_bases = []
    try:
        # Handling paginate requirement
        paginator = client.get_paginator('list_knowledge_bases')
        for page in paginator.paginate():
            knowledge_bases.extend(page.get('knowledgeBaseSummaries', []))
    except ClientError as e:
        print(f"Error listing knowledge bases: {e}")
    except Exception as e:
        print(f"Error listing knowledge bases: {e}")
    return knowledge_bases

# Main function to delete knowledge bases with status 'FAILED'
def delete_failed_knowledge_bases():
    knowledge_bases = list_all_knowledge_bases()
    for kb in knowledge_bases:
        if kb.get('status') == 'FAILED':
            delete_knowledge_base(kb.get('knowledgeBaseId'))

if __name__ == "__main__":
    delete_failed_knowledge_bases()
