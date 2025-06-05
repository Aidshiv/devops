Working with Gradle – Full Project Files

1. Directory Structure:
HelloGradle/
├── build.gradle             ← Groovy DSL (Option A)
├── build.gradle.kts         ← Kotlin DSL (Option B)
├── settings.gradle
├── gradle/
├── gradlew
├── gradlew.bat
└── src/
    ├── main/
    │   └── java/
    │       └── com/
    │           └── example/
    │               └── App.java
    └── test/
        └── java/
            └── com/
                └── example/
                    └── AppTest.java

------------------------------
2. File: build.gradle (Groovy DSL)
------------------------------
plugins {
    id 'java'
    id 'application'
}

group = 'com.example'
version = '1.0'

repositories {
    mavenCentral()
}

dependencies {
    testImplementation 'junit:junit:4.13.2'
}

application {
    mainClass = 'com.example.App'
}

task hello {
    doLast {
        println 'Hello, Gradle!'
    }
}

task greet(dependsOn: build) {
    doLast {
        println 'Build is complete! Time to celebrate!'
    }
}

------------------------------
3. File: build.gradle.kts (Kotlin DSL)
------------------------------
plugins {
    java
    application
}

group = "com.example"
version = "1.0"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("junit:junit:4.13.2")
}

application {
    mainClass.set("com.example.App")
}

tasks.register("hello") {
    doLast {
        println("Hello, Gradle with Kotlin DSL!")
    }
}

tasks.register("greet") {
    dependsOn("build")
    doLast {
        println("Build is complete! Time to celebrate!")
    }
}

------------------------------
4. File: settings.gradle
------------------------------
rootProject.name = 'HelloGradle'

------------------------------
5. File: src/main/java/com/example/App.java
------------------------------
package com.example;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello from Gradle App!");
    }
}

------------------------------
6. File: src/test/java/com/example/AppTest.java
------------------------------
package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    @Test
    public void testApp() {
        assertTrue(true);
    }
}

------------------------------

✅ To Build & Run:
Run: gradle build → Check for BUILD SUCCESSFUL

Run App: gradle run → Should print: Hello from Gradle App!

Run Custom Task: gradle hello → Prints: Hello, Gradle!

Run Greet Task: gradle greet → Builds first, then prints: Build is complete! Time to celebrate!

------------------------------
✅Run:
# STEP 1: Navigate to your project folder
cd HelloGradle

# STEP 2: Make the Gradle wrapper script executable
chmod +x gradlew

# STEP 3: Build the project (compiles code, runs tests, packages JAR)
./gradlew build

# STEP 4: Run the Java application
./gradlew run

# STEP 5: Run the custom task that prints "Hello, Gradle!"
./gradlew hello

# STEP 6: Run the "greet" task (depends on build, then prints message)
./gradlew greet

# EXTRA (optional):
# Clean build artifacts
./gradlew clean

# List all available Gradle tasks
./gradlew tasks

# Run unit tests
./gradlew test

------------------------------
