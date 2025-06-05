Step 1: Uninstall Jenkins if already installed

sudo apt purge jenkins  
sudo apt autoremove

Step 2: Install Java (Jenkins needs Java to run)

sudo apt update  
sudo apt install openjdk-17-jdk

Verify Java installation:
java -version

Step 3: Add Jenkins GPG key

curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null

Step 4: Add Jenkins repository

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

Step 5: Update package list

sudo apt update

Step 6: Install Jenkins

sudo apt install jenkins

Step 7: Start Jenkins service

sudo systemctl start jenkins

Step 8: Check Jenkins status

sudo systemctl status jenkins

Step 9: Enable Jenkins to start at boot

sudo systemctl enable jenkins

Step 10: Open Jenkins in browser

http://localhost:8080

Step 11: Get initial admin password

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

Step 12: Complete Jenkins setup

Paste the password into the browser page, install suggested plugins, and create an admin user.
