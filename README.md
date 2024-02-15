# Automatic Ansible Playbook Generator

This project contains a Python script and Bash shell script to automatically generate the file structure for an Ansible playbook.

## Contents

The project contains the following files:

- `README.md` - This readme file
- `Ansible.py` - The main Python script
- `README.py` - Another Python script (unknown purpose)
- `script.sh` - Bash shell script to generate Ansible playbook structure

## Usage

The `script.sh` Bash shell script can be executed to automatically create the recommended Ansible playbook directory and file structure. This includes:

- A `playbooks` folder
- Inside that, subfolders for `group_vars`, `host_vars`, and the playbooks themselves
- Example playbook `.yml` files
- An `inventory` file listing the playbook hosts

To use:

1. Ensure `script.sh`, `Ansible.py` and `README.py` are in the same directory
2. Run `./script.sh`
3. The main playbook folders and files will be generated automatically

The Python scripts `Ansible.py` and `README.py` provide additional functionality for the playbook generation, which is currently undocumented.

## License

This project is unlicensed. Feel free to use or modify the scripts as needed.

Let me know if you would like any sections expanded or have additional questions!
