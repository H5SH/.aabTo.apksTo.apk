# .aabTo.apksTo.apk

## Needed Things

- .aab can be obtained from expo.dev using eas build in case of react native expo
- bundletool.jar
- java sdk

## To Genrate Apks

java -jar bundletool.jar build-apks --bundle=app.aab --output=app.apks --mode=universal --ks-key-alias=tomcat --ks=C:/H5SH/OtherImpStuff/keystore.jks --ks-pass=pass:1234hello1234 

## TO Get apk from apks

java -jar bundletool.jar extract-apks  --apks=app.apks --output-dir=app --device-spec=deviceSpec.json