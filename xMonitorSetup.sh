#!/usr/bin/env bash

# automatically set up the monitors as I usually use them, uses X window system
# my configurations:
#
# home office:
#    [laptop] - [screen 1 (regardless of port))]
# office:
#    [laptop] - [screen 1 (HDMI)] - [screen 2 (DP/USB-C)]

laptopMonitor='eDP-1'
monitor1='HDMI-1'
monitor2='eDP-2'

monitor1Connected=0
monitor2Connected=0

xrandrOutput="$(xrandr)"

if [[ $xrandrOutput == *"$monitor1 connected"* ]]; then
    monitor1Connected=1
    echo 'monitor 1 is connected'
fi

if [[ $xrandrOutput == *"$monitor2 connected"* ]]; then
    monitor2Connected=1
    echo 'monitor 2 is connected'
fi

# debug
echo $monitor1Connected
echo $monitor2Connected

if [[ $monitor1Connected ]] && [[ $monitor2Connected -eq 0 ]]; then
    echo 'Dual monitor setup finished'
    exec xrandr --output $monitor1 --auto --right-of $laptopMonitor
elif [[ $monitor1Connected -eq 0 ]] && [[ $monitor2Connected ]]; then
    echo 'Dual monitor setup finished'
    exec xrandr --output $monitor2 --auto --right-of $laptopMonitor
elif [[ $monitor1Connected ]] && [[ $monitor2Connected ]]; then
    echo 'Three monitor setup finished'
    exec xrandr --output $monitor1 --auto --right-of $laptopMonitor --output $monitor2 --right-of $monitor1
else
    echo "No external monitors detected no ports $monitor1 and $monitor2"
fi

echo 'Done'

