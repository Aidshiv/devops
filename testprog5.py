CONFIGURATION MANAGEMENT WITH ANSIBLE

───────────────────────────────
1. INSTALL ANSIBLE ON UBUNTU
sudo apt update
sudo apt upgrade -y
sudo apt install ansible -y
ansible --version

───────────────────────────────
2. CREATE INVENTORY FILE (hosts.ini)
nano hosts.ini

Add:
[local]
localhost ansible_connection=local

Save and exit

───────────────────────────────
3. CREATE PLAYBOOK FILE (setup.yml)
nano setup.yml

Add:

---
- name: Basic Server Setup
  hosts: local
  become: yes
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install curl
      apt:
        name: curl
        state: present

Save and exit

───────────────────────────────
4. RUN THE PLAYBOOK
ansible-playbook -i hosts.ini setup.yml
