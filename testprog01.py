 Working with Maven – Create Project, Understand POM, Manage Dependencies, and Use Plugins

Step 1: Create a Maven Project
- Open Terminal.
- Run:
  mvn archetype:generate -DgroupId=com.example -DartifactId=MyMavenApp -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

Step 2: Move into Project Directory
- Run:
  cd MyMavenApp

Step 3: Project Structure Overview
- You will see:
  MyMavenApp/
  ├── pom.xml
  └── src/
      ├── main/java/com/example/App.java
      └── test/java/com/example/AppTest.java

Step 4: Understand and create 
--------------------------------------------
pom.xml
--------------------------------------------
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>MyMavenApp</artifactId>
  <version>1.0-SNAPSHOT</version>

  <properties>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.13.2</version>
      <scope>test</scope>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.1</version>
        <configuration>
          <source>11</source>
          <target>11</target>
        </configuration>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>2.22.2</version>
      </plugin>
    </plugins>
  </build>
</project>

--------------------------------------------
App.java
--------------------------------------------
package com.example;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}

--------------------------------------------
AppTest.java
--------------------------------------------
package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    @Test
    public void testApp() {
        assertTrue(true);
    }
}

--------------------------------------------
Step 5: Compile Project
- Run:
  mvn compile

Step 6: Run Unit Tests
- Run:
  mvn test

Step 7: Package Application into JAR
- Run:
  mvn package
- Output JAR at: target/MyMavenApp-1.0-SNAPSHOT.jar

Step 8: Clean Build Files
- Run:
  mvn clean

Result:
- Maven builds, tests, and packages Java app using dependencies and plugins defined in pom.xml.
