# .aabTo.apksTo.apk

## To Genrate Apks

java -jar bundletool.jar build-apks --bundle=app.aab --output=fahs.apks --mode=universal --ks-key-alias=tomcat --ks=C:/H5SH/keystore.jks --ks-pass=pass:1
234hello1234. 

## TO Get apk from apks 

java -jar bundletool.jar extract-apks  --apks=apptest2.apks --output-dir=appTest5 --device-spec=deviceSpec.json