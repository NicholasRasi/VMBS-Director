# VMs Manager
This component manages the VMs and it is designed to:

- initialize a VM with the benchmark dependencies
- execute a command on a VM, for example to turn on or off a machine
- run a suite of benchmarks on a machine

### Available Versions
- Ansible Playbook: it allows to start, stop, initialize VMs
- Python executable: it allows to start and stop VMs

## Requirements
- Providers CLIs:
    - https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
    - https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest
    - https://cloud.google.com/sdk/docs