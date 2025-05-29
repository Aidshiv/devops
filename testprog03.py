Maven:

mvn archetype:generate -DgroupId=com.example -DartifactId=HelloMaven -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
cd HelloMaven
mvn package
java -cp target/HelloMaven-1.0-SNAPSHOT.jar com.example.App


Gradle:
mkdir HelloMavenGradle
cd HelloMavenGradle
gradle init --type java-application
mkdir -p src/main/java/com/example
cp ../HelloMaven/src/main/java/com/example/App.java src/main/java/com/example/
nano build.gradle   # Add mainClass = 'com.example.App'
gradle build
gradle run
