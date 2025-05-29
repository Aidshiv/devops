#*************setup.yml*************

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


#*************hosts.ini*************
[local]
localhost ansible_connection=local


**********How to run:***********
ansible-playbook -i hosts.ini setup.yml
