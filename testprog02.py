#***************App.java************
package com.example;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}

#***************AppTest.java************
package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    @Test
    public void testApp() {
        assertTrue(true); // Basic test
    }
}


#************build.gradle***************
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


#***************build.gradle.kts************
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

