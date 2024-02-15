import os 
import sys

def create_ansible_project(project_dir):
    """
    Creates the basic Ansible project directory structure with detailed help instructions.

    Args:
        project_dir (str): Path to the desired project directory.
    """

    # Create the main project directory
    os.makedirs(project_dir, exist_ok=True)

    # Group and host variables directories
    vars_dirs = ["group_vars", "host_vars"]
    for dir_name in vars_dirs:
        os.makedirs(os.path.join(project_dir, dir_name), exist_ok=True)

        # Create README.md files with instructions
        readme_path = os.path.join(project_dir, dir_name, "README.md")
        with open(readme_path, "w") as readme:
            readme.write(f"# {dir_name} Directory\n\n")

            if dir_name == "group_vars":
                readme.write(
                    "Store variables here to configure groups of hosts dynamically.\n\n"
                    "* `all` file: Common variables for all groups.\n* `[group_name]` files: Variables specific to a group.\n\n"
                    "**Example:** Define `db_version: 11.8` in `all` for all databases, or customize database IPs for a specific group in `webservers`.\n"
                )
            elif dir_name == "host_vars":
                readme.write(
                    "Store variables here to configure individual hosts with unique settings.\n\n"
                    "* `[hostname]` files: Define variables specific to a host.\n\n"
                    "**Example:** Set specific user credentials for the database master host in `db-master`.\n"
                )

    # Inventory and roles directories
    inv_dirs = ["hosts", "inventory", "roles"]
    for dir_name in inv_dirs:
        os.makedirs(os.path.join(project_dir, dir_name), exist_ok=True)

        # Create README.md files or comments with instructions
        if dir_name == "hosts":
            open(os.path.join(project_dir, dir_name, "inventory"), "w").write(
                "# Inventory file: Define your managed hosts here.\n\n"
                "Use groups to organize hosts like:\n\n"
                "[webservers]\n192.168.1.10\n192.168.1.20\n\n"
                "[databases]\n192.168.1.30\n192.168.1.40\n"
            )
        elif dir_name == "inventory":
            open(
                os.path.join(project_dir, dir_name, "README.md"), "w"
            ).write("# Use this directory for alternative inventory formats (JSON, INI).")
        else:
            readme_path = os.path.join(project_dir, dir_name, "README.md")
            with open(readme_path, "w") as readme:
                readme.write(f"# {dir_name} Directory\n\n")
                readme.write(
                    "Organize reusable tasks and variables into roles for modularity.\n\n"
                    "**Example:** Create a `webserver` role with:\n* `tasks/main.yml`: Install Apache/Nginx, configure virtual hosts, and start the service.\n* `vars/main.yml`: Define web server-specific variables like document root and port.\n* `defaults/main.yml`: Set default values for variables that can be overridden in playbooks.\n* `handlers/main.yml`: Define actions to take upon task completion or errors (e.g., restarting the service).\n"
                )

    # Playbooks directory and optional library
    os.makedirs(os.path.join(project_dir, "playbooks"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "library"), exist_ok=True)


    # Ansible configuration file (continued)
    open(os.path.join(project_dir, "ansible.cfg"), "w").write(
        "[defaults]\n"
        "inventory = hosts\n"
        "\n# Customize other settings if needed:\n"
        "# * ansible_connection: Specify default connection method (ssh, local).\n"
        "# * private_key_file: Define path to your private SSH key.\n"
        "# * ask_vault_pass: Prompt for Vault password interactively.\n"
        "# * verbosity: Set verbosity level (0-5, where 0 is silent and 5 is very verbose).\n"
        "\n# Example:\n"
        "# ansible_connection = ssh\n"
        "# private_key_file = ~/.ssh/id_rsa\n"
    )

    print(f"Ansible project directory structure created at: {project_dir}")


# Example usage (corrected)
if __name__ == "__main__":  # Ensure the code runs only when executed directly
    project_dir = sys.argv[1]
    create_ansible_project(project_dir)