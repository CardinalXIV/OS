#!/bin/bash
# Create a large file on the USB stick if it doesn't exist
if [ ! -f /media/pi/AABC-2BB1/largefile ]; then
    dd if=/dev/zero of=/media/pi/AABC-2BB1/largefile bs=1M count=1024
fi

# Start SCP tight loop
(
    while true; do
        scp /media/pi/AABC-2BB1/largefile localhost:/media/pi/AABC-2BB1/largefile_copy
        rm /media/pi/AABC-2BB1/largefile_copy
    done
) &

# Start DD tight loop from USB stick to /dev/null
(
    while true; do
        dd if=/media/pi/AABC-2BB1/largefile of=/dev/null bs=4M
    done
) &

# Start multiple DD instances from /dev/zero to /dev/null
for i in {1..50}; do
    nice -n 10 dd if=/dev/zero of=/dev/null bs=4M &
done

# Wait for a signal to terminate
trap "killall scp dd" EXIT

# Keep the script running to allow background jobs to execute
wait
