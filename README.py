import os
import sys 

md_content = """
# Ansible Template Directories

Created: February 15, 2024 6:23 PM

## **Enhanced Ansible Project Directory Structure with Detailed Examples**

I've incorporated your feedback to create an even more comprehensive response, providing detailed examples within directory help files and eliminating repetition:

**Directory Structure:**

```markdown
ansible_project/
├── group_vars/ # Group-specific variables
│ ├── all # Common variables for all groups
│ └── <group_name> # Variables specific to a group
├── host_vars/ # Host-specific variables
│ └── <hostname> # Variables specific to a host
├── hosts # Inventory file defining managed hosts
├── inventory/ # Alternative inventory file location
│ └── <inventory_name> # Inventory file with different format
├── playbooks/ # Directory for playbooks
│ ├── site.yml # Playbook for overall site configuration
│ ├── webservers.yml # Playbook for configuring web servers
│ └── databases.yml # Playbook for configuring databases
├── roles/ # Directory for reusable roles
│ ├── common # Role with common tasks and variables
│ ├── webserver # Role for installing and configuring webservers
│ └── database # Role for installing and configuring databases
├── library/ # (Optional) Custom Ansible modules used in playbooks
└── ansible.cfg # Ansible configuration file
```

**Directory Descriptions and Examples:**

**1. group_vars and host_vars:**

- **Purpose:** Define variables for groups or individual hosts to enable dynamic configuration based on environment.
- **Examples:**
  - `group_vars/all`: Set `db_version: 11.8` to apply to all database servers.
  - `group_vars/webservers`: Assign a list of web server IPs for a specific group.
  - `host_vars/db-master`: Define user credentials specific to the database master host.

**2. hosts and inventory:**

- **hosts:**
  - **Purpose:** Main inventory file defining managed hosts and connection details.
  - **Example:** Use groups to organize hosts:
    **YAML**
    ```
    [webservers]
    192.168.1.10
    192.168.1.20

    [databases]
    192.168.1.30
    192.168.1.40

    ```
- **inventory:**
  - **Purpose:** (Optional) Use different inventory formats (JSON, INI) in this directory.

**3. playbooks:**

- **Purpose:** YAML files containing tasks to be executed on managed hosts.
- **Examples:**
  - `site.yml`: Configure basic settings like timezone and user accounts across all hosts.
  - `webservers.yml`: Install and configure a web server software using apt or yum modules.
  - `databases.yml`: Deploy and configure a database service with tasks and variables defined in roles.

**4. roles:**

- **Purpose:** Organize reusable tasks and variables into self-contained directories.
- **Example (webserver role):**
  - `tasks/main.yml`: Install Apache/Nginx, configure virtual hosts, and start the service.
  - `vars/main.yml`: Define web server-specific variables like document root and port.
  - `defaults/main.yml`: Set default values for variables that can be overridden in playbooks.
  - `handlers/main.yml`: Define actions to take upon task completion or errors (e.g., restarting the service).

**5. library (Optional):**

- **Purpose:** Store custom Ansible modules not included in the standard library.

**6. ansible.cfg:**

- **Purpose:** Customize Ansible settings like inventory path and verbosity.

**Key Points:**

- Use `group_vars` and `host_vars` strategically to avoid hardcoding values in playbooks.
- Structure roles for clarity and reusability.
- Explore alternative inventory formats (JSON, INI) in the `inventory` directory.
- Consider using a version control system (Git) to manage your Ansible project.

I hope this enhanced response provides a clear and practical guide to creating well-structured Ansible projects!

---

Here is a template diagram for the common directories and files structure in Ansible:

```markdown
ansible/
├── inventory/
│   ├── hosts # inventory file for defining hosts and groups
│   ├── group_vars/ # variables per group
│   │   └── group1.yml
│   └── host_vars/ # variables per host
│       └── host1.yml
├── playbooks/
│   ├── site.yml # master playbook
│   ├── common.yml # importable playbook
│   └── wordpress.yml # application playbook
├── roles/
│   ├── common/
│   │   └── tasks
│   │       └── main.yml
│   └── wordpress/
│       ├── tasks
│       │   └── main.yml
│       ├── handlers
│       │   └── main.yml
│       ├── templates
│       │   └── wp-config.php.j2
│       ├── files
│       │   └── .htaccess
│       ├── vars
│       │   └── main.yml
│       └── defaults
│           └── main.yml
├── config # inventory config and credentials
└── ansible.cfg # settings config file

```

This shows some of the key directories and files:

- `inventory`: Defines the hosts Ansible can connect to and group them
- `group_vars`, `host_vars`: Variables that apply to groups or single hosts
- `playbooks`: YAML files containing the Ansible tasks
- `roles`: Reusable abstraction layer with tasks/handlers/files organized
- `config`: Central place to manage inventory and credentials
- `ansible.cfg`: Config file with global settings


"""


project_dir = sys.argv[1]

with open(os.path.join(project_dir, "README.md"),"w") as f:
  f.write(md_content)
  f.write("Generated README.md")
