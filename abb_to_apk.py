import os

output = os.popen('java -jar bundletool.jar build-apks --bundle=app.aab --output=app.apks --mode=universal --ks-key-alias=tomcat --ks=C:/H5SH/OtherImpStuff/keystore.jks --ks-pass=pass:1234hello1234').read()
if output == '':
    os.popen('java -jar bundletool.jar extract-apks  --apks=app.apks --output-dir=app --device-spec=deviceSpec.json')
else:
    print("Error")

