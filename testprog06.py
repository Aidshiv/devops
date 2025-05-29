'''
1. Jenkins Job Setup Overview
Build Maven project from Git repo.

Archive generated JAR artifact.

Post-build step: Run Ansible playbook to deploy artifact.

Verify deployment success.
'''

#**************hosts.ini**************

[local]
localhost ansible_connection=local


#**************deploy.yml**************

- name: Deploy Maven Artifact
  hosts: local
  become: yes
  tasks:
    - name: Copy the artifact to the deployment directory
      copy:
        src: "/var/lib/jenkins/workspace/HelloMavenCI/target/HelloMaven-1.0-SNAPSHOT.jar"
        dest: "/opt/deployment/HelloMaven.jar"


#5. Summary: Jenkins Maven Job Steps
New Item → Freestyle Project → Name it (e.g., HelloMaven-CI)
Source Code Manageme
Git
Repository URL: https://github.com/yourusername/HelloMaven.git
Credentials if private repo
Build:
Add build step → Invoke top-level Maven targets
Goals: clean package
Post-build Actions:
Archive the artifacts → target/*.jar
Execute shell → ansible-playbook -i /path/to/hosts.ini /path/to/deploy.yml
Save and run job.




#6. Verify Deployment

ls -l /opt/deployment/


ansible-playbook -i /path/to/hosts.ini /path/to/deploy.yml

