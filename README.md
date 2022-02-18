## Genesis  
#### This repository is for Genesis DevOps School  
Link to Tech Task: https://github.com/amomama/devops-school or you can find in [README_Task.md](README_Task.md) 

### Ansible
The ansible playbooks for deploy WordPress (run Docker Compose project). It consists of 3 separate containers running: MySQL, WordPress, Nginx

### Directory tree
```bash
├── inventory
|   ├── group_vars
|   |   └── all.yml
|   └── host_vars
|       └── ub.local.yml
|
├── playbooks
|   └── wordpress.yml
|
├── roles
|   └── wordpress
|       ├── defaults
|       |   └── main.yml
|       ├── files
|       |   └── .env
|       └── tasks
|           ├── checksite.yml
|           ├── install_docker.yml
|           ├── main.yml
|           ├── ufw.yml
|           └── wordpress.yml
├── ansible.cfg
|
├── README_Task.md
|
└── README.md
```
### Description
The playbooks are in [playbooks](/playbooks/) subdirectory.  
The roles are in [roles](/roles/) subdirectory.  

* [wordpress.yml](/roles/wordpress/tasks/wordpress.yml)           - deploy wordpress: copy files and run docker-compose  
* [checksite.yml](/roles/wordpress/tasks/checksite.yml)           - check health  
* [install_docker.yml](/roles/wordpress/tasks/install_docker.yml) - install docker and docker-compose in Ubuntu
* [ufw.yml](/roles/wordpress/tasks/ufw.yml)                       - disable ufw in ubuntu  
* [main.yml](/roles/wordpress/tasks/main.yml)                     - the main playbook with include all tasks  
* [wordpress-nginx.j2](/roles/wordpress/templates/wordpress-nginx.j2)  - the template for nginx  
* [docker-compose.j2](/roles/wordpress/templates/docker-compose.j2)   - the template for docker-compose.yml  
* [main.yml](/roles/wordpress/defaults/main.yml)                      - variables
* [all.yml](/inventory/group_vars/all.yml)                            - the group variables. The domain is included to file.
* [files](/roles/wordpress/files/.env)                                - the env file with passwords, it is encrypted by ansible vault. The password is: **genesis** 

### Requirements
There are packages below that should be installed on the (local) host where you'll be running this playbook on:
* Ansible >= 2.9  
* python >= 3.7  

The Linux user that can be used by Ansible to access the host. Default is **ubuntu** (to support AWS, GCP, Openstack), however feel free to use any other user. Make sure to update the 'ansible_user' variable inside [ub.loacl.yml](/inventory/host_vars/ub.local.yml)  
```
system_user: "{{ ansible_user }}"
```
### Supported OS
* Target linux instance should have Ubuntu >= 18

### Installation instructions  

**1. Get source code for install project:**  
```
git clone https://github.com/spytliak/Genesis.git
```
**2. Update hosts inventory file `/inventory/host_vars/ub.local.yml` [ub.local.yml](/inventory/host_vars/ub.local.yml) with your instance(server) Public IP and user:**  
```
ansible_ssh_host: 192.168.10.57
ansible_user: ubuntu
```
**3. Run playbook, using hosts inventory file if need (see ansible.cfg) (Vault password: genesis) :**
```
ansible-playbook playbooks/wordpress.yml -K --ask-vault-pass
```
### Output
Link to example with full output: https://gist.github.com/spytliak/763d94346869efcc49897c0c43275db6