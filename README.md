## Genesis
##### This repository is for Genesis DevOps School

Link to Tech Task:
 * https://github.com/amomama/devops-school

### Ansible

The ansible playbooks for deploy WordPress in Docker. 

The home work for this playbook is in [README_Task.md](README_Task.md)

The playbooks are in [playbooks](/playbooks/) subdirectory.

The roles are in [roles](/roles/) subdirectory.


### Requirements
* ansible verison >= 2.9
* python >= 3.7

### Supported OS
* Ubuntu >= 18

### Description

The domain variable is in [all.yml](/inventory/group_vars/all.yml)

* [wordpress.yml](/roles/wordpress/tasks/wordpress.yml)           - deploy wordpress: copy files and run docker-compose  
* [checksite.yml](/roles/wordpress/tasks/checksite.yml)           - check health  
* [install_docker.yml](/roles/wordpress/tasks/install_docker.yml) - install docker and docker-compose in Ubuntu
* [ufw.yml](/roles/wordpress/tasks/ufw.yml)                       - disable ufw in ubuntu  
* [main.yml](/roles/wordpress/tasks/main.yml)                     - the main playbook with include all tasks  

* [wordpress-nginx.j2](/roles/wordpress/templates/wordpress-nginx.j2)  - the template for nginx  
* [docker-compose.j2](/roles/wordpress/templates/docker-compose.j2)   - the template for docker-compose.yml  

* [main.yml](/roles/wordpress/defaults/main.yml)                      - variables

The env file with passwords in [files](/roles/wordpress/files/.env)  
There is encrypted by ansible vault. The password is "genesis"

