🧪 EXPERIMENT 8: JENKINS CI PIPELINE FOR MAVEN + ANSIBLE DEPLOYMENT

───────────────────────────────
1. PREPARE MAVEN PROJECT (if not already)
cd path/to/HelloMaven
git init
git add .
git commit -m "Initial commit of HelloMaven project"
# Push to your remote Git repo

───────────────────────────────
2. SETUP JENKINS JOB
- Open Jenkins → New Item → Name: HelloMaven-CI → Freestyle project → OK
- Source Code Management: Git
  Repository URL: https://github.com/yourusername/HelloMaven.git
  (Add credentials if private)
- Build Step: Add "Invoke top-level Maven targets"
  Goals: clean package
- Post-build Action: Archive the artifacts
  Files to archive: target/*.jar
- Post-build Action: Execute shell
  Command:
    ansible-playbook -i /path/to/hosts.ini /path/to/deploy.yml
- Save the job

───────────────────────────────
3. CREATE ANSIBLE INVENTORY (if not already)
nano hosts.ini

Content:
[local]
localhost ansible_connection=local

───────────────────────────────
4. CREATE DEPLOYMENT PLAYBOOK
nano deploy.yml

Content:
---
- name: Deploy Maven Artifact
  hosts: local
  become: yes
  tasks:
    - name: Copy the artifact to deployment directory
      copy:
        src: "/var/lib/jenkins/workspace/HelloMavenCI/target/HelloMaven-1.0-SNAPSHOT.jar"
        dest: "/opt/deployment/HelloMaven.jar"

Save and exit

───────────────────────────────
5. RUN AND VERIFY
- In Jenkins, click "Build Now" for HelloMaven-CI job
- Check Console Output for success:
  Maven build success, artifact archived, ansible-playbook ran
- Verify artifact on deployment machine:
  ls -l /opt/deployment/
