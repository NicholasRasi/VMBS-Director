import yaml
import sys
import subprocess
import json
import argparse
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/<command>', methods=['POST'])
def post_command(command):
    req = request.get_json()
    provider = req["provider"]
    id = req["id"]
    if provider == "AWS":
        region = req["region"]
        aws(command, region, [id])
        return {"msg": "ok"}, 200
    elif provider == "AZURE":
        if command == "stop":
            command = "deallocate"
        azure(command, az_resource_group_name, [id])
        return {"msg": "ok"}, 200

def aws(command, region, ids):
    cli_command = ["aws", "ec2", command + "-instances", "--region", region, "--instance-ids"]
    for id in ids:
        cli_command.append(id)
    json_response = subprocess.check_output(cli_command)
    print_json(json_response)


def azure(command, resource_group, names):
    for name in names:
        cli_command = ["az", "vm", command, "--output", "json", "--no-wait", "-g", resource_group, "--name", name]
        json_response = subprocess.check_output(cli_command)
        print(json_response)


def print_json(json_string):
    try:
        json_string = json_string.decode("utf-8")
        json_object = json.loads(json_string)
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
    except Exception as e:
        print(json_string)


if __name__ == "__main__":
    # open config file
    with open("config_vms_manager.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    # read config variables
    az_resource_group_name = None
    if "az_resource_group_name" in cfg:
        az_resource_group_name = cfg["az_resource_group_name"]

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', dest='server', action='store_true')
    parser.add_argument('--start', dest='start', action='store_true')
    parser.add_argument('--stop', dest='stop', action='store_true')
    parser.add_argument('--port', type=int, default=8083)
    parser.add_argument('--providers', nargs='+', required=False)
    parser.set_defaults(server=False, start=False, stop=False)
    args = parser.parse_args()

    if args.server:
        # start server version
        app.run(debug=True, host='0.0.0.0', port=args.port)
    else:
        command = None
        if args.start:
            command = "start"
        elif args.stop:
            command = "stop"
        print("Executing " + command)
        print("Providers: " + " ".join(args.providers))

        # execute command
        providers = cfg["providers"]
        for provider in providers:
            if provider == "aws" and provider in args.providers:
                for region in providers[provider]:
                    print(command + " for " + provider + " region " + region)
                    ids = providers[provider][region]
                    aws(command, region, ids)
            elif provider == "azure" and provider in args.providers:
                for resource_group in providers[provider]:
                    print(command + " for " + provider + " resource group " + resource_group)
                    names = providers[provider][resource_group]
                    if command == "stop":
                        az_command = "deallocate"
                    else:
                        az_command = command
                    azure(az_command, resource_group, names)
