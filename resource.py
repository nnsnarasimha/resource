import boto3

def list_active_services(account_id):
    config_client = boto3.client('config')

    # Get the list of AWS Config Rules
    config_rules = config_client.describe_config_rules()['ConfigRules']

    # Get the list of AWS Config enabled services
    config_services = set([rule['ConfigRuleName'].split("-")[0] for rule in config_rules])

    print(f"Active AWS Services for Account ID {account_id}:")
    print("---------------------")

    for service in config_services:
        print(service)

def main():
    # Replace 'your_account_id' with the actual AWS account ID
    aws_account_id = 'your_account_id'
    list_active_services(aws_account_id)

if __name__ == "__main__":
    main()
