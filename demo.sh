# stop script on error
set -e

# run pub/sub sample app using certificates downloaded in package
printf "\nRunning pub/sub sample application...\n"
python device_sim.py -d pyandroid15 -e a3a13fa4bs6nw5-ats.iot.us-west-2.amazonaws.com -r ./root-CA.crt -c ./IoTTestDevice.cert.pem -k ./IoTTestDevice.private.key
