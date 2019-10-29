# stop script on error
set -e

# run pub/sub sample app using certificates downloaded in package
printf "\nRunning pub/sub sample application...\n"
python part1.py -e a3a13fa4bs6nw5-ats.iot.us-west-2.amazonaws.com -id 1ad4569c -r ../myThings/IoTTestDevice/connect_device_package/root-CA.crt -c ../myThings/IoTTestDevice/connect_device_package/IoTTestDevice.cert.pem -k ../myThings/IoTTestDevice/connect_device_package/IoTTestDevice.private.key
