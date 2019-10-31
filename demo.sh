# stop script on error
set -e

# run pub/sub sample app using certificates downloaded in package
printf "\nRunning pub/sub sample application...\n"
python device_sim.py -d pysimulato3 -e a3a13fa4bs6nw5-ats.iot.us-west-2.amazonaws.com -r ../myThings/IoTTestDevice/connect_device_package/root-CA.crt -c ../myThings/IoTTestDevice/connect_device_package/IoTTestDevice.cert.pem -k ../myThings/IoTTestDevice/connect_device_package/IoTTestDevice.private.key

# python device_sim.py -e a3a13fa4bs6nw5-ats.iot.us-west-2.amazonaws.com -id device_3 -r ../myThings/IoTTestDevice/connect_device_package/root-CA.crt -c ../myThings/IoTTestDevice/connect_device_package/IoTTestDevice.cert.pem -k ../myThings/IoTTestDevice/connect_device_package/IoTTestDevice.private.key
