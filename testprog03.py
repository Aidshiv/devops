Experiment 4: Build and Run a Java Application with Maven, then Migrate to Gradle

Part A: Build and Run a Java Application with Maven

Step 1: Create the Maven Project
- Open your Terminal.
- Generate the Maven project using Quickstart Archetype:
  mvn archetype:generate -DgroupId=com.example -DartifactId=HelloMaven -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
  (This creates a new Maven project with basic Java app and sample test.)

Step 2: Change directory into the newly created project
  cd HelloMaven

Step 3: Explore the Maven project structure
  - You should see:
    HelloMaven/
    ├── pom.xml
    └── src
        ├── main/java/com/example/App.java
        └── test/java/com/example/AppTest.java

Step 4: Build the Maven Project
  mvn package
  (Compiles code, runs tests, packages app into target/HelloMaven-1.0-SNAPSHOT.jar)

Step 5: Run the Maven Application
  java -cp target/HelloMaven-1.0-SNAPSHOT.jar com.example.App
  (Output should be "Hello World!")

---

Part B: Migrate the Application to Gradle

Step 1: Create a new Gradle project
- Open a new terminal window or go back to workspace.
- Create a new directory for Gradle project:
  mkdir HelloMavenGradle
  cd HelloMavenGradle
- Initialize Gradle project with Java application type:
  gradle init --type java-application

Step 2: Adjust the Gradle project to use the same code
- Copy App.java from Maven project:
  (From HelloMaven/src/main/java/com/example/App.java)
- Create package folders if not present:
  mkdir -p src/main/java/com/example
- Move or copy App.java to Gradle project:
  mv src/main/java/App.java src/main/java/com/example/
- Do the same for tests if needed.

Step 3: Update Gradle build script
- Open build.gradle:
  nano build.gradle
- Modify or add the application block to set main class:
  application {
    mainClass = 'com.example.App'
  }
- Save and exit.

Step 4: Build and run the Gradle application
- Build the project:
  gradle build
  (Look for "BUILD SUCCESSFUL")
- Run the application:
  gradle run
  (Output should be "Hello World!")

---

End of Experiment 4.
