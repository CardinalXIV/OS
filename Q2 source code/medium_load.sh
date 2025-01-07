#!/bin/bash
# Create a medium file on the USB stick if it doesn't exist
if [ ! -f /media/pi/AABC-2BB1/mediumfile ]; then
    dd if=/dev/zero of=/media/pi/AABC-2BB1/mediumfile bs=1M count=512
fi

# Start SCP tight loop
(
    while true; do
        scp /media/pi/AABC-2BB1/mediumfile localhost:/media/pi/AABC-2BB1/mediumfile_copy
        rm /media/pi/AABC-2BB1/mediumfile_copy
    done
) &

# Start DD tight loop from USB stick to /dev/null
(
    while true; do
        dd if=/media/pi/AABC-2BB1/mediumfile of=/dev/null bs=1M
    done
) &

# Start multiple DD instances from /dev/zero to /dev/null
for i in {1..10}; do
    nice -n 20 dd if=/dev/zero of=/dev/null bs=1M &
done

# Wait for a signal to terminate
trap "killall scp dd" EXIT

# Keep the script running to allow background jobs to execute
wait
